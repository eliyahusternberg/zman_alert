import requests
import json


def get_shkia(zipcode):
    url = 'http://www.hebcal.com/shabbat/''?cfg=json&geo=zip&zip={}&b=0&m=72'.format(zipcode)
    response = requests.get(url)
    data = json.loads(response.text)
    from pprint import pprint
    items_list = data['items']
    for item in items_list:
        if 'Candle lighting' in item['title']:
            string1 = item['title']
            #print(string1)

            # pprint(data)

            string2 = string1.split(' ')
            #print(string2)
            shkia = string2[2]
            #print(shkia)


    return shkia
