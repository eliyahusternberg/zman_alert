import requests
import json

def main():
    zipcode =('?cfg=json&geo=zip&zip=11691&b=0&m=72' )
    get_shkia(zipcode)


def get_shkia(zipcode):
    url = 'http://www.hebcal.com/shabbat/''?cfg=json&geo=zip&zip=11691&b=0&m=72'
    response = requests.get(url)
    data = json.loads(response.text)
    from pprint import pprint
    items_list = data['items']

    for item in items_list:
        if 'Candle lighting' in item['title']:
            string1 = item['title']
            print(string1)

            # pprint(data)

            string2 = string1.split(' ')
            print(string2)
            shkia = string2[2]
            print(shkia)
            print('Shkia this week is at {}'.format(shkia))

    return shkia

if __name__ == '__main__':
    main()
