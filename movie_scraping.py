import urllib.request as req
from bs4 import BeautifulSoup

gatunek_list = {"Komedia": 13, "Horror": 12, "Thriller": 24, "Animacja": 2, "Wojenny": 26,
                "Sci-Fi": 33, "Akcja": 28, "Kryminał": 15, "Fantasy": 9}


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


class SampleMovie:
    def __init__(self, movie_content, gatunek):
        self.movie = movie_content
        self.gatunek = gatunek

    def get_data(self):
        self._miejsce = self.movie.find('div', class_='ranking__position').text
        self._tytul = self.movie.find('h3', class_='film__title').text
        self._ocena = self.movie.find('span', class_='rate__value').text

    def pack_data(self):
        return zip(self._miejsce, self._tytul, self._ocena, self.gatunek)
