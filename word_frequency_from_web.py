import requests
from bs4 import BeautifulSoup
import operator


def get_all_words(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    base_word_list = []
    for div_content in soup.findAll("div", {"class": "esc-lead-snippet-wrapper"}):
        content = div_content.string
        # print(type(content))
        # continue;
        if content is not None:
            base_words = content.lower().split(" ")
            for word in base_words:
                base_word_list.append(word)
    filter_words(base_word_list)


def filter_words(words):
    filtered_word_list = []
    symbols = "~`!@#$%^&*()_-+=;:'\",<.>/?[{]}\|"
    for word in words:
        for i in range(0, len(symbols)):
            clean_word = word.replace(symbols[i], "")
            if len(clean_word) > 0:
                filtered_word_list.append(clean_word)
    count_and_sort(filtered_word_list)


def count_and_sort(words):
    result_set = {}
    for word in words:
        if word in result_set:
            result_set[word] += 1
        else:
            result_set[word] = 1
    final_set = sorted(result_set.items(), key=operator.itemgetter(1))
    print(final_set)

get_all_words("https://news.google.co.in/")
