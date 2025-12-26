import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.spring.io/spring-ai/reference/api/chatclient.html',
    'https://docs.spring.io/spring-ai/reference/api/index.html',
    'https://modelcontextprotocol.io/docs/learn/architecture',
    'https://modelcontextprotocol.io/docs/learn/client-concepts'
]

def get_content(url):
    content = requests.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')
    print(f"There are {len(soup.text)} characters in {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=get_content, args=(url,)) # Pass url as tuple otherwise it will passed as seuence of characters
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Work done")