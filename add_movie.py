from app.models import Movies_Database
from movie_scraping import Movies
from processing import SampleMovie
from app import db

gatunek_list = {"Komedia": 13, "Horror": 12, "Thriller": 24, "Animacja": 2, "Wojenny": 26,
                "Sci-Fi": 33, "Akcja": 28, "Fantasy": 9}


def main():
    for gatunek in gatunek_list:
        movies_list = Movies(gatunek).find_movies()
        for j in movies_list:
            movie_data = SampleMovie(j, gatunek)
            movie_data.get_data()
            ocena = movie_data._ocena.replace(',', '.')
            movie = Movies_Database(name=movie_data._tytul, type=movie_data.gatunek, score=float(ocena))
            try:
                db.session.merge(movie)
                db.session.commit()
            except Exception as error:
                print(error)

if __name__ == "__main__":
    main()