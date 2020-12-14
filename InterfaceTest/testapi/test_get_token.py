from InterfaceTest.api.gettoken import Get_token


class Test:
    def setup(self):
        self.Get_token = Get_token()
    def test_get_token(self):
        self.Get_token.get_token()
