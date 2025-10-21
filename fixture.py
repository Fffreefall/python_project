import os

import pytest
# import selenium
from dotenv import load_dotenv
from selene.support.shared import browser
# from selenium.webdriver.chrome.options import Options

from test_python_mashroom.API.utils.listactivity import UtilityMethods
from test_python_mashroom.API.utils.methods_for_fixture import authorization_at_stand, createactivity_for_test,\
    selenoid_session
from test_python_mashroom.UTILS import attach


load_dotenv()


@pytest.fixture(scope="module")
def activity_api():
    # Переменные для cleanup
    token = None
    user_id = None
    activity_body = None

    try :
        """создает сессию и мероприятие"""
        selenoid_session()

        browser.config.base_url = os.getenv("STEND_URL_UI")
        browser.config.window_width = 1440
        browser.config.window_height = 1200

        """авторизация"""
        authorization = authorization_at_stand(login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
        token = authorization.authorization_token
        user_id = authorization.user_id

        '''создание мероприятия'''
        activity_body = createactivity_for_test(token)

        yield [browser, activity_body]

    except Exception as e :
        print(f"❌ Ошибка в фикстуре: {str(e)}")
        pytest.skip(f"Ошибка при создании фикстуры: {str(e)}")

    finally :
        # Cleanup выполнится ВСЕГДА, даже после skip
        if token and user_id :
            try :
                u_methods = UtilityMethods(2, 3, token, user_id)
                u_methods.listactivity_delete()
                print("\n✅ использован метод удаления мероприятий из фикстуры")
            except Exception as cleanup_error :
                print(f"⚠️ Ошибка при cleanup: {str(cleanup_error)}")


@pytest.fixture(scope="module")
def mashroom_api():
    try:
        """создает только сессию"""
        selenoid_session()

        browser.config.base_url = os.getenv("STEND_URL_UI")
        browser.config.window_width = 1920
        browser.config.window_height = 1080

        authorization = authorization_at_stand(login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))

        return [browser, authorization]

    except Exception as e :
        print(f"❌ Ошибка в фикстуре: {str(e)}")
        pytest.skip(f"Ошибка при создании фикстуры: {str(e)}")


@pytest.fixture(scope="function", autouse=True)
def attach_f():
    attach.add_video(browser)
    yield
    attach.add_screenshot(browser), attach.add_logs(browser), attach.add_html(browser)
    print(" \nприкреплены аттачи из фикстуры attach_f, работающей по function")
