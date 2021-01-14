import pandas as pd
import requests
from bs4 import BeautifulSoup
from  urllib import parse
import json
import datetime 

def input_key(keyword):
    now = datetime.datetime.now()

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36" }

    #ss = requests.Session()

    page = 1
    keyword = parse.quote(str(keyword))

    k = 1
    total = []
    for i in range(150):
        url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword='+str(keyword)+'&order=12&asc=0&page='+str(page)+'&mode=s&jobsource='+str(now.year)+'indexpoc'
        res = requests.get(url,headers = headers)
        soup = BeautifulSoup(res.text,'lxml')
        try:
            h2 = soup.select('h2',{'class':"b-tit"})

            for i in h2:
                try:
                    em = i.select('a',{'class':"js-job-link ",'target':"_blank"})[0]
                    url_notthis = 'http' + em['href']
                    bridge = url_notthis.replace('?','/').split('/')

                    url = 'https://www.104.com.tw/job/ajax/content/'+str(bridge[4])
                    headers = {
                        "Referer": "https://www.104.com.tw/job/"+ str(bridge[4]),
                    }

                    response = requests.get(url = url, headers = headers)
                    js = json.loads(response.text)


                    for i in js:

                        job_name = js['data']['header']['jobName']
                        cust_name = js['data']['header']['custName']
                        workEXP = js['data']['condition']['workExp']
                        edu = js['data']['condition']['edu']
                        skill = js['data']['condition']['skill']
                        #other = js['data']['condition']['other']

                        if len(skill) == 0 :
                            skill.append('不拘')    

                        l = []
                        l.append('職稱:'+ job_name)
                        l.append('公司名稱:'+ str(cust_name))
                        l.append('工作經驗:'+ str(workEXP))
                        l.append('學歷:'+ str(edu))
                        if len(skill) > 1:
                            t = []
                            for i in skill:
                                t.append(i['description'])
                            l.append('所需技能:'+ str(t))
                        #elif len(skill) == 1:
                        #    l.append(skill['description'])
                        else:
                            if type(skill[0]) == dict:
                                l.append('所需技能:'+ str(skill[0]['description']))
                            else:
                                l.append('所需技能:'+ str(skill[0]))
                        #l.append(other)
                        total.append(l)
                        
                        
                        
                        print('新增'+str(k)+'筆資料')
                        k+=1
                except:
                    continue
            page+=1
        except:
            break

    a = pd.DataFrame(total,columns = ['職稱','公司名稱','要求工作經驗','要求學歷','所需技能'])
    a = a.drop_duplicates('職稱')
    a = str(a.values)
    

    return a


if __name__ =="__main__":
    print(input_key("哈哈"))