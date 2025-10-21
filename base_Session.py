import json
import logging
from json import JSONDecodeError
import requests
import time

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import Session, Response


def allure_logger(function):
    def wrapper(*args, **kwargs):
        method, url = args[1], args[2]

        with allure.step(f"{method} {url}"):

            response: Response = function(*args, **kwargs)

            allure.attach(body=to_curl(response.request).encode("utf8"), name=f"Request {response.status_code}",
                          attachment_type=AttachmentType.TEXT, extension=".txt")
            try:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"),
                              name=f"Response {response.status_code}", attachment_type=AttachmentType.JSON,
                              extension=".json")
            except JSONDecodeError:
                allure.attach(body=response.text.encode("utf8"), name=f"Response {response.status_code}",
                              attachment_type=AttachmentType.TEXT, extension=".txt")

        return response

    return wrapper


def request_logging(func):
    def wrapper(*args, **kwargs):
        response: Response = func(*args, **kwargs)
        # Сокращённый вариант (без curl-детализации)
        logging.info(f"[{response.status_code}] {response.request.method} {response.url}")
        return response
    return wrapper


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    def _should_retry(self, response: Response) -> bool :
        """Определяем, нужно ли делать ретрай для данного статус-кода"""
        retry_codes = {500, 502, 503, 504, 403, 429}
        return response.status_code in retry_codes

    def request_with_retry(self, method: str, url: str, **kwargs) -> Response :
        """
        Универсальный метод запроса с ретраями
        """
        max_attempts = 3
        attempt = 1

        while attempt <= max_attempts :
            try :
                response = super().request(method, self.url + url, **kwargs)

                if self._should_retry(response) :
                    if attempt <= max_attempts :  # Изменили условие!
                        print(f"⚠️  Попытка {attempt}/{max_attempts}. Status: {response.status_code}. Retrying...")
                        if attempt < max_attempts :  # Спим только если это не последняя попытка
                            time.sleep(2)
                        attempt += 1
                        continue
                    else :
                        response.raise_for_status()

                return response

            except Exception as e :
                if attempt < max_attempts :
                    print(f"⚠️  Попытка {attempt}/{max_attempts}. Ошибка: {str(e)}. Retrying...")
                    time.sleep(2)
                    attempt += 1
                else :
                    print(f"⚠️  Попытка {attempt}/{max_attempts} Все {max_attempts} попыток провалились. Ошибка: {str(e)}")
                    raise

    @request_logging
    @allure_logger
    def request(self, method, url, **kwargs) -> Response:
        """Основной метод запроса с ретраями"""
        with allure.step(f"{method} {url}"):
            return self.request_with_retry(method, url, **kwargs)
