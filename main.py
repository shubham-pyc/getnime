from cgitb import reset
from config import BASE_URL
import requests
from bs4 import BeautifulSoup
import re
import argparse


# home = requests.get(BASE_URL+"/home")

def make_url(name, episode):
    return BASE_URL + "/watch/"+name+"/"+str(episode)


def make_list_url(name):
    return BASE_URL + "/anime/"+name


def get_anime_list(name):
    list_url = make_list_url(name)
    print(list_url)
    page = requests.get(list_url)
    print(page)
    ret_value = []
    if page:
        soup = BeautifulSoup(page.content, 'html.parser')
        print(page)
        episode_li = soup.select("#episode_related .name")
        ret_value = []
        for li in episode_li:
            text = li.getText()
            episode = re.search(r'\d+', text)
            if episode:
                ret_value.append(episode.group())
            else:
                print("here")

    else:
        print("Error while getting page list: ", page)
        print("Invalid anime")

    return ret_value


def get_anime_url(name, episode):
    url = make_url(name, episode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.select("#playerframe")
    if len(link):
        link = link[0].get('src')
        if "embed" in link:
            return BASE_URL+link
        else:
            return "https:" + link
    else:
        not_found = soup.select(".content_left h1")
        if len(not_found):
            print("Anime not found")
            return not_found[0]
        else:
            return "Unknown"
    # return "https:" + str(link[0].get('src'))


def get_args():
    parser = argparse.ArgumentParser(description="Utility to get anime url")
    parser.add_argument('--episode', type=int,
                        help='custom episode number', required=False, default=-1)
    

    parser.add_argument('--anime', type=str,
                        help='custom episode number', required=False, default='one-piece')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # print(get_path())
    name = args.anime
    episode = args.episode
    
    if episode <  0:
        episode_list = get_anime_list(name)
        if len(episode_list):
            episode = episode_list[-1]


    print(get_anime_url(name, episode))

    # episode_list = get_anime_list(name)

    # latest = episode_list[-1]




main()


# print(home)
