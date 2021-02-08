import requests
from bs4 import BeautifulSoup


# Avoid ConnectionError
headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

def get_url(URL:str) -> str:
    web = requests.get(URL, headers=headers)

    if web.status_code == 200: 
        return web.content

    else:
        print("Couldn't connect")


def find(content:str, name, attr=None) -> list:
    soup = BeautifulSoup(content, 'html.parser')
    sample = soup.find(name, attr)
    return sample

def find_all(content:str, name, attr=None) -> list:
    soup = BeautifulSoup(content, 'html.parser')
    samples = soup.find_all(name, attrs=attr)
    return [sample for sample in samples]

def convert_to_str(samples:list):
    return [sample.text for sample in samples]