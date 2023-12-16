import requests
from bs4 import BeautifulSoup
import time

request = requests.Session()

main_url = "https://geogoroda.ru/bukva"

user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
text = request.get(url=main_url, headers=user_agent).text

bs = BeautifulSoup(text, 'lxml')
bukv = str(bs.find_all("h4", {"class": "goroda-bukva"})[0].find_all_next('a'))
bukv = bukv.split('href="')
links_ru = []

def city_zapros(arg):
    start_time = time.time()
    text = request.get(url=main_url.replace("/bukva", f"/rossiya/bukva/{arg}"), headers=user_agent).text
    total = str(round((time.time() - start_time) * 1000, 3)) + " мс"
    bs = BeautifulSoup(text, 'lxml')
    city_name = bs.find_all('td', {'class': 'views-field views-field-title large'})
    city_list_end = []
    for city in city_name:
        try:
            try:
                city_list_end.append(str(city).split('rossiya">')[1].split('<')[0])
            except:
                city_list_end.append(str(city).split('rossiya-0">')[1].split('<')[0])
        except:
            pass
    answer = ""
    count = 0
    for i in city_list_end:
        answer += i + "\n"
        count += 1
    return answer, count, total

def l():
    for i in range(0, len(bukv)):
        if bukv[i].find("/rossiya/bukva/") != -1:
            links_ru.append(bukv[i].split('"')[0])

    for link_end in links_ru:
        text = request.get(url= main_url.replace("/bukva", link_end), headers=user_agent).text
        bs = BeautifulSoup(text, 'lxml')

        city_name = bs.find_all('td', {'class': 'views-field views-field-title large'})
        for city in city_name:
            try:
                try:
                    print(str(city).split('rossiya">')[1].split('<')[0])
                except:
                    print(str(city).split('rossiya-0">')[1].split('<')[0])
            except:
                pass