import requests
from bs4 import BeautifulSoup

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'


ss = requests.session()
print(ss.cookies)

#Session1
res = ss.get(url,headers = headers)
soup = BeautifulSoup(res.text , 'html.parser')
button = soup.select('button',{'class':"btn-big"})[0]
#print(button)
##取得POST DATA
#print(button['name'])
#print(button['value'])
data = {}
data[button['name']]=button['value']
#print(data)
print(ss.cookies)

#Session2
target_url = 'https://www.ptt.cc/ask/over18'
res_target = ss.post(target_url,data = data , headers = headers)
print(ss.cookies)

#Session3
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
final_res = ss.get(final_url,headers = headers)
#print(final_res.text)

#看session內的cookie
print(ss.cookies)