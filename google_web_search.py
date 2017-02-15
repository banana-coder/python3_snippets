'''
Python3 Google Search
'''
import requests
from bs4 import BeautifulSoup

parent_url = "https://google.co.in/search?q="

query_string = "Linkin Park Songs"
#query_string = input("Enter search query")
query_string = query_string.replace(" ","+")

def __get_links(max_pages):
    __start = 0;
    get_link_list = [];
    if max_pages > 10:
        max_pages = 10
    while (__start / 10) <= max_pages:
        rebuild_url = parent_url + query_string + "#q=" + query_string + "&start=" + str(__start)
        page_source = requests.get(rebuild_url)
        plain_text_source_code = page_source.text
        soup_obj = BeautifulSoup(plain_text_source_code, "html.parser")
        for each_link in soup_obj.findAll('h3', {"class": "r"}):
            each_link_a = each_link.find("a").get("href").replace("/url?q=", "")
            get_link_list.append(each_link_a)
        __start += 10
    return get_link_list

#display all fetched links
fetched_links = __get_links(1)
for link in fetched_links:
    print(link)
