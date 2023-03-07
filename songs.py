from bs4 import BeautifulSoup
import requests
SONG_URL = "https://www.billboard.com/charts/hot-100/"


class Songs:
    def __init__(self):
        pass

    def scrap_songs(self):
        user_ip = input(f"Which year do you want to travel to?Type the date in this format YYYY-MM-DD: ")
        response = requests.get(f"{SONG_URL}{user_ip}")
        year = user_ip.strip("-")[0]
        title_text_list = []
        soup = BeautifulSoup(response.text, 'html.parser')

        title_songs = soup.select(selector="li ul li h3")
        for t in title_songs:
            title_text_list.append(t.get_text().strip())
        return {'title_text_list':title_text_list, 'year':year}
