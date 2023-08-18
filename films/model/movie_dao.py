from .db_connection import Connection
from tkinter import messagebox


def create_table():
    connection = Connection()

    sql = """
    CREATE TABLE movies(
        id_movie INTEGER,
        name VARCHAR(100),
        duration VARCHAR(10),
        genre VARCHAR(100),
        PRIMARY KEY(id_movie AUTOINCREMENT)
    )"""
    try:
        connection.cursor.execute(sql)
        connection.close()
        title = "Create record"
        message = "Table created in database"
        messagebox.showinfo(title, message)
    except:
        title = "Create record"
        message = "The table has already been created"
        messagebox.showwarning(title, message)


def drop_table():
    connection = Connection()

    sql = "DROP TABLE movies"

    try:
        connection.cursor.execute(sql)
        connection.close()
        title = "Delete record"
        message = "The database table was successfully deleted."
        messagebox.showinfo(title, message)
    except:
        title = "Delete record"
        message = "Error deleting table"
        messagebox.showerror(title, message)


class Movie:
    def __init__(self, name, duration, genre):
        self.id_movie = None
        self.name = name
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"Movie[{self.name}, {self.duration}, {self.genre}]"


# insert movie
def save_movie(movie):
    connection = Connection()

    sql = f"""INSERT INTO movies (name, duration, genre)
    VALUES('{movie.name}', '{movie.duration}', '{movie.genre}')"""

    try:
        connection.cursor.execute(sql)
        connection.close()
    except:
        title = "Save data"
        message = "Failed to save data"
        messagebox.showerror(title, message)


# get movies


def list_movie():
    connection = Connection()

    movies_list = []
    sql = "SELECT * FROM movies"

    try:
        connection.cursor.execute(sql)
        movies_list = connection.cursor.fetchall()
        connection.close()

    except:
        title = "Log connection"
        message = "Failed to load data"
        messagebox.showerror(title, message)

    return movies_list


def update_movie(movie, id_movie):
    connection = Connection()

    sql = f"""UPDATE movies SET name = '{movie.name}', duration = '{movie.duration}', genre = '{movie.genre}' WHERE id_movie = {id_movie} """

    try:
        connection.cursor.execute(sql)
        connection.close()

    except:
        title = "Data edition"
        message = "Fail to edit"
        messagebox.showerror(title, message)

def delete_movie(id_movie):
    connection = Connection()
     
    sql = f'DELETE FROM movies WHERE id_movie = {id_movie}'

    try:
        connection.cursor.execute(sql)
        connection.close()

    except:
        title = "Delete data"
        message = "Could not delete record"
        messagebox.showerror(title, message)
