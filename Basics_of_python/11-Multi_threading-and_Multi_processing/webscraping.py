



import threading
import requests
from bs4 import BeautifulSoup

urls=[
    "https://python.langchain.com/v0.2/docs/concepts/#agents",

    "https://python.langchain.com/v0.2/docs/tutorials/",

    "https://python.langchain.com/v0.2/docs/introduction/"
    
]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{(len(soup.text))} character from {url}')
    # print(soup.text)
threads=[]    
for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

print("ALl web pages fetched")    
