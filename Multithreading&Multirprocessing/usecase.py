'''
Real world exmple: Multithreading for I/O bounds TAsks
Scenrio :Webscraping
Webscraping oftern involves making numerious network requests to fetch web pages.
These tasks are I/O bound beacuse they spend a lot of time waiting for responses from server
multithread can significanly improve the performace by allowing the multiple webpages cuncurrently 

'''
'''
https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/tutorials/
https://python.langchain.com/v0.2/docs/how_to/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/how_to/'
]

def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{(len(soup.text))} characters form {url}')

threads =[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All webpages are fetched')


