from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox
from weather_api import get_weather
from favorites import add_to_favorites, remove_from_favorites, update_favorites_list, FAVORITE_CITIES

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        weather_label.config(text=weather)
    else:
        messagebox.showerror("Помилка", "Введіть назву міста!")

def show_favorite_weather(event):
    try:
        selected_city = favorites_list.get(favorites_list.curselection())
        weather = get_weather(selected_city)
        weather_label.config(text=weather)
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть місто зі списку.")

root = Tk()
root.title("Прогноз погоди")

Label(root, text="Введіть місто:").pack()
city_entry = Entry(root)
city_entry.pack()

Button(root, text="Отримати погоду", command=show_weather).pack()
Button(root, text="Додати до улюблених", command=lambda: add_to_favorites(city_entry.get(), favorites_list)).pack()
Button(root, text="Видалити з улюблених", command=lambda: remove_from_favorites(favorites_list)).pack()

Label(root, text="Улюблені локації:").pack()
favorites_list = Listbox(root)
favorites_list.pack()
favorites_list.bind("<<ListboxSelect>>", show_favorite_weather)

weather_label = Label(root, text="", justify="left")
weather_label.pack()

update_favorites_list(favorites_list)
root.mainloop()




