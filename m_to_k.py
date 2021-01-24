# Miles to kilometer converter
from tkinter import *

TITLE_FONT = ("Lobster", 12)
INPUT_FONT = ("Sen", 8)
LABEL_FONT = ("Sen", 11)


def convert():
    miles = float(mile_input.get())
    km = round(miles * 1.069)
    kilo_input.config(text=f"{km}")
    print(km)


window = Tk()
window.minsize(width=100, height=100)
window.title("Gui App")
window.resizable(width=False, height=False)
window.config(bg="grey15", padx=5, pady=5)

title_text = Label(text="Miles to Kilometer Converter",
                   font=TITLE_FONT, bg="grey15", foreground="grey50")
title_text.grid(row=0, column=3)

mile_input = Entry(width=15)
mile_input.config(font=INPUT_FONT, bg="grey20",
                  foreground="orange", justify="center", border=0, highlightthickness=1, highlightbackground="black", highlightcolor="orange", insertbackground="orange")
mile_input.grid(row=1, column=3)

mile_text = Label(text="Miles")
mile_text.config(font=LABEL_FONT, bg="grey15", fg="grey")
mile_text.grid(row=1, column=4)

text = Label(text="is equal to")
text.config(font=("Lobster", 11), bg="grey15", fg="grey")
text.grid(row=2, column=2)

# kilo_input = Label(width=15)
# kilo_input.config(font=("Sen", 8), bg="grey20",
#                   foreground="orange", justify="center", border=0, highlightthickness=1, highlightbackground="black", highlightcolor="orange", insertbackground="orange")
# kilo_input.grid(row=2, column=3)

kilo_input = Label(text="0", width=10)
kilo_input.config(font=("Sen", 8), bg="grey20",
                  foreground="orange", justify="center", border=1, highlightthickness=1, highlightbackground="black", highlightcolor="orange")
kilo_input.grid(row=2, column=3)

kilo_text = Label(text="Km")
kilo_text.config(font=LABEL_FONT, bg="grey15", fg="grey")
kilo_text.grid(row=2, column=4)


button = Button(text="Convert", command=convert)
button.config(font=INPUT_FONT, background="grey15", foreground="orange",
              activebackground="orange", activeforeground="grey15", border=0)
button.grid(row=3, column=3)

window.mainloop()
