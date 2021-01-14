import requests
import json
from bs4 import BeautifulSoup


headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

data = {'action': 'fm_ajax_load_more',
        'nonce': 'd8c08f1381',
        'page': '3'}

res = requests.post(url,headers= headers,data = data)

json_data = json.loads(res.text)

soup = BeautifulSoup(json_data['data'],'lxml')

title_list = soup.select('a',{'class':'post-thumbnail nlif'})
for t in title_list:
    print(t['onclick'])
