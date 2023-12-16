import requests
from bs4 import BeautifulSoup

rq = requests.Session()
url = "https://flibusta.site/booksearch?ask="
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
def sequence(link_ls, name):
    link = 'Пусто'
    for i in link_ls:
        list = rq.get(url=url.replace("/booksearch?ask=", i), headers=user_agent).text
        soup_list = BeautifulSoup(list, 'lxml')
        appruved = str(soup_list.find('h1', {'class': 'title'})).split('">')[1].split('<')[0]
        print(appruved + f"{i}---{len(link_ls)}")
        if (name.lower() == appruved.lower()) or (i == link_ls[-1]):
            print("Except")
            link = "/b/" + str(soup_list.find('div', {"id": "main"})).split('<a href="/b/')[1].split('"')[0]
            print(link)
            break
    return link

def main(name):
    ask_search = rq.get(url=url + name, headers=user_agent).text
    soup = BeautifulSoup(ask_search, 'lxml')
    try:
        link_list = str(soup.find_all('div', {"id": "main"})).split('<li>')
        link_list.pop(0)
        print(link_list)
        for i in range(len(link_list)):
            link_list[i] = link_list[i].split('<a href="')[1].split('"')[0]
        for i in range(len(link_list)):
            if (link_list[0].find("/sequence/") != -1) and (link_list[i].find("/sequence/") == -1):
                length = len(link_list)
                for l in range(i, length):
                    link_list.pop(i)
                break
        print(link_list)
        if (link_list[0].find("/sequence/") == -1):
            Download(link_list[0], name)
            return "Файл скачен"
        else:
            print("1")
            link = sequence(link_ls=link_list, name=name)
            print("2")
            Download(link, name)
            return "Файл скачен"
    except Exception as err:
        print(err)
        return "Бот наебнулся(или сайт лёг, но скорее всего всё-таки бот)"

def Download(link, name):
    try:
        download = rq.get(url=url.replace("/booksearch?ask=", f"{link}/fb2"), headers=user_agent).content
        file = open(f"{name}.fb2", "wb")
        file.write(download)
        file.close()
    except:
        pass

if __name__ == "__main__":
    main("Неправильный самурай")