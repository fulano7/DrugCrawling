import robotparser
import requests
import heapq
from bs4 import BeautifulSoup
from collections import deque

#max_urls should be 1000?
max_urls = 120

def heuristic(url):
    return url.count('-')*(-1)

def heuristic_bfs(root):
    queue = []
    visited = []
    heapq.heappush(queue, (heuristic(root), root))

    while queue:
        cur = heapq.heappop(queue)[1]
        if (cur in visited):
            continue
        # if(checkRobots(root+"/robots.txt", cur) == False):
        #     continue

        print cur

        page = requests.get(cur)
        content = page.headers.get('content-type')

        soup = BeautifulSoup(page.content, 'html.parser')
        visited.append(cur)

        links = []

        for link in soup.find_all('a', href=True):
            if (root not in link['href'] and "http" not in link['href'] and "/" in link['href']):
                links.append(root+link['href'])
            elif (root in link['href']):
                links.append(link['href'])

        for link in links:
            if link not in visited:
                heapq.heappush(queue, (heuristic(link), link))

        global max_urls
        if (len(visited) >= max_urls):
            break

    return visited


heuristic_bfs('http://www.onofre.com.br')
