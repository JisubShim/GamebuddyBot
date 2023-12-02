import requests
from bs4 import BeautifulSoup
import time

def get_steam_games(url, count):
    """
    주어진 URL에서 Steam 게임 정보를 가져오는 함수.
    """
    res = requests.get(url, cookies={'Steam_Language': 'koreana'})
    json_data = res.json()
    soup = BeautifulSoup(json_data['results_html'], 'html.parser')

    games_info = {}
    games = soup.select('.search_result_row')
    for game in games[:count]:
        game_title = game.select_one('.title').text
        game_url = game['href']
        games_info[game_title] = game_url

    return games_info