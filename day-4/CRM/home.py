from customtkinter import *

app = CTk()
app.geometry("700x500")

# Name Label
nameLabel = CTkLabel(master=app, text="Name")
nameLabel.grid(row=0, column=0,padx=20, pady=20, sticky="ew")
 
# Name Entry Field
nameEntry = CTkEntry(master=app, placeholder_text="Teja")
nameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

app.mainloop()