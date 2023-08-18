import tkinter as tk
from tkinter import ttk
from model.movie_dao import create_table, drop_table
from model.movie_dao import Movie, save_movie, list_movie, update_movie, delete_movie
from tkinter import messagebox


def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar, width=300, height=300)

    start_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Start", menu=start_menu)

    start_menu.add_command(label="Create record", command=create_table)
    start_menu.add_command(label="Delete record", command=drop_table)
    start_menu.add_command(label="Quit", command=root.destroy)

    menu_bar.add_cascade(label="Settings")
    menu_bar.add_cascade(label="Help")


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config(bg='blue')
        self.id_movie = None

        self.movie_fields()
        self.disable_fields()
        self.movie_table()

    def movie_fields(self):
        # label fields
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.config(font=("Arial", 12, "bold"))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.duration_label = tk.Label(self, text="Duration:")
        self.duration_label.config(font=("Arial", 12, "bold"))
        self.duration_label.grid(row=1, column=0, padx=10, pady=10)

        self.genre_label = tk.Label(self, text="Genre:")
        self.genre_label.config(font=("Arial", 12, "bold"))
        self.genre_label.grid(row=2, column=0, padx=10, pady=10)

        # input fields
        self.name = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name)
        self.name_entry.config(width=50, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.duration = tk.StringVar()
        self.duration_entry = tk.Entry(self, textvariable=self.duration)
        self.duration_entry.config(width=50, font=("Arial", 12))
        self.duration_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.genre = tk.StringVar()
        self.genre_entry = tk.Entry(self, textvariable=self.genre)
        self.genre_entry.config(width=50, font=("Arial", 12))
        self.genre_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # buttons
        self.new_button = tk.Button(self, text="New", command=self.enable_fields)
        self.new_button.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F",
        )
        self.new_button.grid(row=3, column=0, padx=10, pady=10)

        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF",
        )
        self.save_button.grid(row=3, column=1, padx=10, pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.disable_fields)
        self.cancel_button.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370",
        )
        self.cancel_button.grid(row=3, column=2, padx=10, pady=10)

    # enable fields
    def enable_fields(self):
        self.name.set("")
        self.duration.set("")
        self.genre.set("")

        self.name_entry.config(state="normal")
        self.duration_entry.config(state="normal")
        self.genre_entry.config(state="normal")

        self.save_button.config(state="normal")
        self.cancel_button.config(state="normal")

    # disable fields
    def disable_fields(self):
        self.id_movie = None
        
        self.name.set("")
        self.duration.set("")
        self.genre.set("")

        self.name_entry.config(state="disabled")
        self.duration_entry.config(state="disabled")
        self.genre_entry.config(state="disabled")

        self.save_button.config(state="disabled")
        self.cancel_button.config(state="disabled")

    def save_data(self):
        movie = Movie(
            self.name.get(),
            self.duration.get(),
            self.genre.get(),
        )

        if self.id_movie == None:
            save_movie(movie)
        else:
            update_movie(movie, self.id_movie)
        self.movie_table()

        self.disable_fields()

    def movie_table(self):
        # retrieve record
        self.movies_list = list_movie()
        self.movies_list.reverse()

        self.board = ttk.Treeview(self, columns=("Name", "Duration", "Genre"))
        self.board.grid(row=4, column=0, columnspan=4, sticky="nse")

        # scrollbar for table if it exceeds ten records
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.board.yview
        )
        self.scrollbar.grid(row=4, column=4, sticky="nse")
        self.board.configure(yscrollcommand=self.scrollbar.set)

        self.board.heading("#0", text="ID")
        self.board.heading("#1", text="NAME")
        self.board.heading("#2", text="DURATION")
        self.board.heading("#3", text="GENRE")

        # iterate list
        for m in self.movies_list:
            self.board.insert("", 0, text=m[0], values=(m[1], m[2], m[3]))

        # edit button

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_movie)
        self.edit_button.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F",
        )
        self.edit_button.grid(row=5, column=0, padx=10, pady=10)

        # delete button

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        self.delete_button.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370",
        )
        self.delete_button.grid(row=5, column=1, padx=10, pady=10)

    def edit_movie(self):
        try:
            self.id_movie = self.board.item(self.board.selection())["text"]
            self.movie_name = self.board.item(self.board.selection())["values"][0]
            self.movie_duration = self.board.item(self.board.selection())["values"][1]
            self.movie_genre = self.board.item(self.board.selection())["values"][2]

            self.enable_fields()

            self.name_entry.insert(0, self.movie_name)
            self.duration_entry.insert(0, self.movie_duration)
            self.genre_entry.insert(0, self.movie_genre)

        except:
            title = "Data editing"
            message = "You have not selected any records"
            messagebox.showwarning(title, message)

    def delete_data(self):
        try:
            self.id_movie = self.board.item(self.board.selection())["text"]
            delete_movie(self.id_movie)

            self.movie_table()
            self.id_movie = None

        except:
            title = "Delete record"
            message = "You have not selected any records"
            messagebox.showwarning(title, message)
