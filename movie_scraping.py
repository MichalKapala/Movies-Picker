import urllib.request as req
from bs4 import BeautifulSoup

gatunek_list = {"Komedia": 13, "Horror": 12, "Thriller": 24, "Animacja": 2, "Wojenny": 26,
                "Sci-Fi": 33, "Akcja": 28, "Fantasy": 9}


class Movies:
    def __init__(self, gatunek, rok=None, kraj=None):
        self.gatunek = gatunek
        self.rok = rok
        self.kraj = kraj

    def find_movies(self):
        main_list = []
        for i in range(1, 5):
            url = '{}{}{}{}'.format('https://www.filmweb.pl/ajax/ranking/film/', self.gatunek + '/',
                                    str(gatunek_list[self.gatunek]) + '/', str(i))
            page = req.urlopen(url).read()
            bs = BeautifulSoup(page, 'html.parser')
            bs = bs.find('div', class_='ranking__list')
            film_list = bs.find_all('div', class_='item place')
            main_list.extend(film_list)
        return main_list






