#__author:  shenxi-PC
#date:  2018/9/29

import requests
def get_out_ip():
    url = r'http://2018.ip138.com/ic.asp'
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip

print(get_out_ip())