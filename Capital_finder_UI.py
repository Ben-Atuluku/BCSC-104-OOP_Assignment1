#Tiny program which makes use of a simple UI to search a dictionary
import tkinter as tk

window1 = tk.Tk()
window1.geometry('500x300')
title = tk.Label(window1, text="Enter the country below:")
title.pack()
entry1 = tk.Entry(window1)
entry1.pack()
capitals = {
    "USA" : "Washington",
    "UK" : "London",
    "Nigeria" : "Abuja",
    "Germany" : "Berlin",
    "Russia" : "Moscow",
    "Canada" : "Ontario",
    "France" : "Paris",
    "India" : "New Delhi",
    "Italy" : "Rome",
    "China": "Beijing",

}
result1 = tk.Label(window1, text=" ")
result1.pack()
def search(country):
    capital = capitals[country]
    print(capital)
    result1.config(text=capital)

srch_btn = tk.Button(window1, text="Search", command= lambda: search(entry1.get()))
srch_btn.pack()

window1.title("Dictionary")
window1.mainloop()


