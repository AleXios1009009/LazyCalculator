

import requests
import socket
import tkinter as tk
from tkinter import messagebox

#internet check
try:
    socket.setdefaulttimeout(2)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
except: #No internet access
    print("ERROR: ")
    print("Without internet i can't get the joke from the internet so please get an internet connection and restart the program, thanks")
    messagebox.showerror("Error","An internet connection is needed to run the program")
    exit()
#internet check passed

root = tk.Tk()
root.title("LazyCalculator by Alessio")
root.geometry("400x350")
tk.Label(root, text="Enter first number").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()
tk.Label(root, text="Enter second number").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()
label_risultato = tk.Label(root, text="", font=("Arial", 10, "italic"), wraplength=350)
label_risultato.pack(pady=20)
def calcola():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        label_risultato.config(text="Loading...")
        root.update()
        risposta = requests.get("https://naas.isalman.dev/no") #Api by hotheadhacker "no-as-a-service"
        pun = risposta.json()["reason"]
        somma = a + b
        result = f"Error: \n{pun}"
        root.title("Look at terminal for actual answer")
        root.after(2000, clear_title)
        print(f"it's {somma}")
        label_risultato.config(text=result)
    except ValueError:
        messagebox.showwarning("Error", "I asked for numbers, not text")
    except:
        label_risultato.config(text="Congratulation you broke my program, create a ticket on my github please!")
btn_calcola = tk.Button(root, text="Solve", command=calcola, bg="yellow", fg="black")
btn_calcola.pack(pady=10)
def clear_title():
    root.title("LazyCalculator by Alessio")
root.mainloop()

