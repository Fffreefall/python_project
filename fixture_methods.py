@allure.step("авторизация на стенде")
@api_retry(max_attempts=1, wait_seconds=2)
def authorization_at_stand(login, password):
    json_data = '{"email":"' + login + '","password":"' + password + '"}'
    api_request = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/user/login', data=json_data)
    if api_request.status_code not in [200, 201] :
        raise requests.HTTPError(f"Authorization failed with status: {api_request.status_code}")
    response_body = api_request.json()
    tokens = response_body.get("tokens")
    authorization_token = tokens.get("access")
    user = response_body.get("user")
    user_id = str(user.get("id"))
    user_login = user.get("login")
    user_role = user.get("role")
    browser.open('')
    browser.driver.execute_script(
        'return window.localStorage.setItem("authorization_token", "' + authorization_token + '");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_id", "' + user_id + '");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_login", "' + user_login + '");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_role", "' + user_role + '");')
    authorization_body = AuthorizationObj(
        authorization_token=authorization_token,
        user=user,
        user_id=user_id,
        user_login=user_login,
        user_role=user_role
    )
    print("\n произошла успешная авторизация")
    return authorization_body