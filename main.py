import movie_scraping
import database_save

gatunek_list = {"Komedia": 13, "Horror": 12, "Thriller": 24, "Animacja": 2, "Wojenny": 26,
                "Sci-Fi": 33, "Akcja": 28, "Fantasy": 9}


def main():
    id = 0
    for gatunek in gatunek_list:
        movies_list = movie_scraping.Movies(gatunek).find_movies()
        for j in movies_list:
            movie_data = movie_scraping.SampleMovie(j, gatunek)
            movie_data.get_data()
            db = database_save.Database('movies.db')
            db.create_connection()
            db.create_table()
            db.insert(id ,movie_data._tytul, movie_data._ocena, movie_data.gatunek)
            id += 1


if __name__ == '__main__':
    main()