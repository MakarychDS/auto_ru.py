import requests
import json

def save_json(path, data):
    with open(path, "w", encoding="utf8") as f:
        json.dump(data, f)

url = 'https://auto.ru/-/ajax/desktop/listing/'

headers = '''
Host: auto.ru
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/moskva/cars/kia/all/?output_type=list&page=2&year_from=2014&year_to=2015
x-client-app-version: 202009.16.194507
x-page-request-id: 2ba6076babada85438b1c8036ca26ffd
x-client-date: 1600424090239
x-csrf-token: e99683eb5da8a1a30400fe50056e1ac039dd0b129ce767c8
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
Content-Length: 163
Connection: keep-alive
Cookie: _csrf_token=e99683eb5da8a1a30400fe50056e1ac039dd0b129ce767c8; autoru_sid=a%3Ag5f647fa3282t5i3d5j7ipa6uavh7i2h.d1e476cd808087e88e71e6f8e68a2953%7C1600421795765.604800._sOq5rRQIwCl1IKAnmaBWg.VANcrTRD-ctyKSe6NL0OWukb7iJKyNzA8QmQDaklxsM; autoruuid=g5f647fa3282t5i3d5j7ipa6uavh7i2h.d1e476cd808087e88e71e6f8e68a2953; suid=2431c8f982bf93e7ce5957b6014954fb.465c32b217b819c90e6922bc58f4faf7; from_lifetime=1600424088510; from=direct; yuidcs=1; X-Vertis-DC=sas; crookie=QeS6LfAHif/gHnBcIZG67lM0UplEn5/vCOThtX2gccHsnDpfkWA/jc3F7TFo+Rm3gwebzeOIXWOdkr93MsoeZl4ngns=; cmtchd=MTYwMDQyMTc5ODA2MA==; _ym_uid=1600421799716900976; _ym_d=1600424088; yuidlt=1; yandexuid=437771801600421790; _ym_isad=2
'''.strip().split('\n')

dict_headers = {}

for header in headers:
    key, value = header.split(': ')
    dict_headers[key] = value

offers = []

for x in range(1,21):
    param = {"category": "cars",
              "section": "all",
              "output_type": "list",
              "page": x,
              "year_from": 2014,
              "year_to": 2015,
              "catalog_filter": [{"mark": "KIA"}],
              "geo_radius": 200,
              "geo_id": [213]}

    response = requests.post(url, json=param, headers = dict_headers)
    data = response.json()
    offers.extend(data['offers'])
    print('current page: ', x)



save_json('data.json', offers)