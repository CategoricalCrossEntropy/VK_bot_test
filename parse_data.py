import requests
from bs4 import BeautifulSoup


def get_weather(city_name, day="today"):
    headers = {'user-agent': 'Mozilla/5.0'}
    try:
        response = requests.get("https://sinoptik.ua/погода-{}".format(city_name.lower()),
                                headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        if day == "today":
            temp = soup.find("p", class_="today-temp").get_text(strip=True)
            desc = soup.find('div', class_="description").get_text(strip=True)
        else:
            temp = soup.find("div", class_="temperature").get_text(strip=True)
            desc = None
        return temp, desc
    except AttributeError:
        return None, None


def get_courses():
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get("https://ru.myfin.by/currency/sankt-peterburg",
                            headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "table-best yellow_bg"})
    rows = table.findAll("tr")[1:]
    courses = {}
    names = ["Евро", "Юань", "Фунт", "Йена", "Франк"]
    for i in range(5):
        row = rows[i]
        courses[names[i]] = row.findAll('td')[2].text
    return courses