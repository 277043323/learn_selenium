import allure

from InterfaceTest.api.gettoken import Get_token


@allure.feature('test get_token')
class Test:

    def setup(self):
        self.Get_token = Get_token()

    @allure.story("Test get_token")
    def test_get_token(self):
       assert 'ok' == self.Get_token.get_token().json()['errmsg']


