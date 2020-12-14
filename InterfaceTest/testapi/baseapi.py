import requests


class BaseApi:
    def baseapi(self,res):
        ret = requests.request(**res)
        return ret