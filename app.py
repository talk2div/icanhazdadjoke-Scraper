import requests
from lxml import etree,html
from fake_useragent import UserAgent
from collections import defaultdict
ua = UserAgent()

header = {
    'User-Agent': ua.random
}
def get(numlst):
    try:
        return numlst[-1]
    except IndexError:
        return 1
d = defaultdict(str)
search_term = input("Enter the term you want to search : ")
resp = requests.get(url=f'https://icanhazdadjoke.com/search?term={search_term}',headers=header)
tree = html.fromstring(html=resp.content)
found_result = tree.xpath("//p[contains(@class,'subtitle')]/strong/text()")[0]
num_list = get(tree.xpath("//ul[@class='pagination-list']/li/a/text()"))
nav_list = []
for i in range(1,int(num_list)+1):
    nav_list.append(f"https://icanhazdadjoke.com/search?term={search_term}&page={i}")
def watch_results():
        for i in nav_list:
            resp = requests.get(url=i,headers=header)
            tree = html.fromstring(html=resp.content)
            all_joke = tree.xpath("//table[contains(@class,'table')]/tbody")[0]
            url_list = all_joke.xpath("//table[contains(@class,'table')]/tbody/tr/td[2]/a/@href")
            joke_list = all_joke.xpath(".//tr/td[1]/pre/text()")
            for k, v in zip(joke_list, url_list):
                 d[k] += v
            for key,value in d.items():
                 print(key," ---> ",f"https://icanhazdadjoke.com{value}")
                 print("==============================================================================================")

if int(found_result) > 0:
    print(f"There are {found_result} results found of keyword --> {search_term}")
    watch = input("Do you want to watch the joke found : Press Y/N ")
    if watch.lower() == "y":
        watch_results()
    else:
        print("Thanks for using joke scraping tool !!!!!!")

