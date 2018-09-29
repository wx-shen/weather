#"coding=utf-8"
import requests

def send_message(content):
    url="https://rest-hangzhou.goeasy.io/publish"
    data="appkey=PR-16a3d35420af410fb1ba2035726d7bb8&channel=demo_channel&content=%s"%content
    response=requests.post(url,data)
    print response