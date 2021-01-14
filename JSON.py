import requests
import json
import urllib
import ssl

url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'

req = requests.get(url)

json_data = json.loads(req.text)

#取標題
for t in json_data:
    print(t['title'])
    artical_url = 'https://www.dcard.tw/f/game/p/233768081'+str(t['id'])
    print(artical_url)
    
    image_url = [img['url']for img in t['mediaMeta']]
    print(image_url)
    for i in image_url:
        #request.urlretrieve(i)
        res_img  = requests.get(i)
        img_content = res_img.content
        with open('./dcardimg/' + image_url.split('/')[-1],'wb') as f :
            f.write(img_content)
        