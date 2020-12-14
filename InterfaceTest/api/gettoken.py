import requests


class Get_token:
    def get_token(self):
        data={
            "method":"get",
            "url":" https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid":"wwf77acb09ea98c9b0",
                "corpsecret":"0D3yssZL0S4DyJCXDQXXBRaLJn06AKCH2z4gukb5NRg"
            }
        }
        # ret01 = requests.request(method=data["method"],url=data["url"],params = data["params"])
        ret = requests.request(**data)
        print(ret.json())
