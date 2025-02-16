import requests
import threading
import re
from bs4 import BeautifulSoup as bsp
import time




with requests.Session() as session:
    p = session.get(game,headers=\
                    {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
    
    p2=p.headers['Set-Cookie']

    o = session.post('https://datanodes.to/download',headers=p.cookies,\
                     data={'op':'download1','id': 'njcyil8hkn1k',\
                           'fname': 'CoD_MW3_--_fitgirl-repacks.site_--_.part01.rar','method_free': 'Free Download >>'})

##    l

    kkk = session.post('https://datanodes.to/download',headers=o.cookies,\
                       data={'op':'download2','id':'njcyil8hkn1k','referer':'https://datanodes.to/downloads','method_free':'Free Download >>'})


    ''' just this works fine. '''
kkk = session.post('https://datanodes.to/download',allow_redirects=False,headers=o.cookies,\
                       data={'op':'download2','id':'njcyil8hkn1k'})
"value='502:8fe5ad13ab137236:IST'"
"value='443'"
    ''' much better '''
kkk = session.post('https://datanodes.to/download',allow_redirects=False,\
                   headers={'cf_ob_info':'horsemeat','cf_use_ob':'409'},\
                       data={'op':'download2','id':'njcyil8hkn1k'})





























header = {':path:':'/download',
        ':scheme:':'https',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'en-US,en;q=0.9',
        'Cache-Control':'max-age=0',
        'Content-Type':'application/x-wwww-fomr-urlencoded',
        'Cookie':cookie,
        'Origin':'https://datanodes.to',
        'Priority':'u=0, i',
        'Referer':'https://datanodes.to/download',
        'Sec-Ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'same-origin',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }


def fetch(url,session=None):
    cookie = session.get(url).cookies
    
    for _ in range(3):
        cook.append(cookie)
        post = session.post('https://datanodes.to/download',data= data)
        print(post.status_code)
        cookie = post.cookies
        time.sleep(5)
        
    global p
    p = post
    __import__('sys').exit()



while True:
##    game = input('enter game in fitgirl-repacks.site: ')
    game = 'https://fitgirl-repacks.site/call-of-duty-modern-warfare-3/'
    if game.lower().startswith('https://fitgirl-repacks.site'):
        break
    print('enter correct form of url. e.g: NO WWW. and USE HTTPS://')

req = requests.get(game)
    
if not req.status_code == 200:
    raise Exception('Couldn\'t connect to the website. check connection or url')

soup = bsp(req.text,'html.parser')

link_list = []
for x in soup.find_all('a'):
    try:
        if x.attrs['href'].startswith('https://datanodes.to/'):
            link_list.append(x.attrs['href'])
            print('part got')
    except KeyError:
        pass
link_list = sorted(link_list)

with requests.Session() as session:
    for x in link_list:
        #threading.Thread(target=fetch,args=(x))
        fetch(x,session)
