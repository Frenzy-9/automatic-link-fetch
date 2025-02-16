import requests
import os
import threading
from bs4 import BeautifulSoup as bsp
from json import loads


def fetch(file_id):
    dl = requests.post('https://datanodes.to/download',allow_redirects=False,
                       headers={'user-agent':'Scooby-Doo 1.29.0.1'},
                       cookies={'cf_clearance':clearance},
                       data={'op':'download2','id':file_id,'dl':'1'})
    print(dl)
    dl_link_list.append(loads(dl.text)['url'])
    


while True:
    game = input('Enter the url from fitgirl-repacks.site')
    if game.lower().startswith('https://fitgirl-repacks.site/'):
        break
    print('Enter correct form of url. Input has to start with "https://fitgirl-repacks.site/"')


req = requests.get(game)
req2 = requests.post(headers={'user-agent':'Scooby-Doo 1.29.0.1'},
                     url='https://datanodes.to/cdn-cgi/challenge-platform/h/g/jsd/r/0.3290009728376738:1738883513:5yA11_XhUz7J00YcCXyR3e37qw38pWcs-G75fsh8Q94/90dee9390ec9e34e')

if not req.status_code == 200 or not req2.status_code == 200:
    raise Exception('Couldn\'t connect to the website. check connection or url')

clearance = req2.cookies['cf_clearance']


soup = bsp(req.text,'html.parser')

link_list = []
for x in soup.find_all('a'):
    try:
        if x.attrs['href'].startswith('https://datanodes.to/'):
            link_list.append(x.attrs['href'])
            print('Received {}'.format(x.string.split('/')[-1]))
    except KeyError:
        pass


print('Total parts: {} '.format(len(link_list)),'All datanode links collected')


dl_link_list = []

thread_list = []
for x in link_list:
    thread = threading.Thread(target=fetch,args=(x[21:].split('/')[0],))
    thread_list.append(thread)
    thread.start()
    
for x in thread_list:
    x.join()

dl_link_list = sorted(dl_link_list,key=lambda q: q.split('/')[-1])
##sorted(dl_link_list,key=lambda q: q[re.search('\d',q).span()[0]])


path = os.path.join(os.environ['home'],'Desktop','from fitgirl-repacks.txt')
with open(path,'a') as f:
    f.write('\n'.join(dl_link_list)+'\n\n')

__import__('winsound').MessageBeep()
print('Download links written in path: {}'.format(path))
