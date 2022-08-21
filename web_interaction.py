import requests
import json

payload={
        'username':'yaoyao',
        'password':'cattle954'
    }
r=requests.get('https://httpbin.org/basic-auth/yaoyao/cattle954',auth=('yaoyao','cattle954'))
print(r.text)
