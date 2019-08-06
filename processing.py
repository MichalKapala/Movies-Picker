
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