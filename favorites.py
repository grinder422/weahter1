from tkinter import messagebox, END

FAVORITE_CITIES = []

def add_to_favorites(city, favorites_list):
    if city and city not in FAVORITE_CITIES:
        FAVORITE_CITIES.append(city)
        update_favorites_list(favorites_list)
        messagebox.showinfo("Успіх", f"{city} додано до улюблених!")
    elif city in FAVORITE_CITIES:
        messagebox.showwarning("Увага", "Місто вже у списку улюблених!")

def remove_from_favorites(favorites_list):
    try:
        selected_city = favorites_list.get(favorites_list.curselection())
        FAVORITE_CITIES.remove(selected_city)
        update_favorites_list(favorites_list)
        messagebox.showinfo("Успіх", f"{selected_city} видалено з улюблених!")
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть місто для видалення.")

def update_favorites_list(favorites_list):
    favorites_list.delete(0, END)
    for city in FAVORITE_CITIES:
        favorites_list.insert(END, city)
