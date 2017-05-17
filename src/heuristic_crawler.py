import urllib.robotparser
import requests
from bs4 import BeautifulSoup
from collections import deque
import heapq

#max_urls should be 1000?
max_urls = 120

#receives a robots page and a url and verifies if we're
#allowed to fetch this url's content
def checkRobots(robots, url):
    try:
        rp = robotparser.RobotFileParser()
        rp.set_url(robots)
        rp.read()
        return rp.can_fetch("*", url)
    except:
        #no robots? allows everything
        return True

#checks if 'content-type' of a page is valid
def checkContent(content):
    return 'text/html' in content

def heuristic(url):
    return (url.count('-')+url.count('_'))*(-1)

def heuristic_bfs(root):
    queue = []
    visited = []
    heapq.heappush(queue, (heuristic(root), root))

    while queue:
        cur = heapq.heappop(queue)[1]
        if (cur in visited):
            continue
        if (checkRobots(root+"/robots.txt", cur) == False):
            continue

        try:
            page = requests.get(cur)
            content = page.headers.get('content-type')

            if (checkContent(content) == False):
                continue

            try:
                myfile = open(cur.replace('/', '+'), 'w+')
                myfile.write(str(page.content))
                myfile.close()
                urls = open("urls-heuristic", "a")
                urls.write(str(cur+"\n"))
                urls.close()
            except:
                print("error creating file")

            soup = BeautifulSoup(page.content, 'html.parser')
            visited.append(cur)

            print("visiting: "+cur)

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
        except:
            continue

    return visited


urls = ["https://www.onofre.com.br",
        "http://www.ultrafarma.com.br",
        "http://www.farmadelivery.com.br",
        "http://www.farma22.com.br",
        "http://loja.paguemenos.com.br",
        "https://www.farmagora.com.br",
        "http://www.drogariasaopaulo.com.br",
        "https://www.medicamentosbrasil.com.br",
        "http://farmaciacristorei.com.br",
        "https://www.saredrogarias.com.br"]

for site in urls:
    heuristic_bfs(site)
