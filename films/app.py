import tkinter as tk
from client.gui import Frame, menu_bar


def main():
    root = tk.Tk()
    root.title("Films App")
    root.iconbitmap("img/film.ico")
    root.resizable(0, 0)

    menu_bar(root)

    app = Frame(root=root)
    app.mainloop()


if __name__ == "__main__":
    main()
