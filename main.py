import tkinter as tk
from tkinter import messagebox
import wifi
import webbrowser

def scan_wifi():
    networks = wifi.Cell.all('wlan0')
    network_list.delete(0, tk.END)  # Efface la liste actuelle

    for network in networks:
        network_list.insert(tk.END, network.ssid)

def connect_wifi():
    selected_network = network_list.get(tk.ACTIVE)
    password = password_entry.get()

    # Connecter au réseau sélectionné
    try:
        selected = [cell for cell in wifi.Cell.all('wlan0') if cell.ssid == selected_network][0]
        selected.connect(password=password)
        messagebox.showinfo("Succès", f"Connecté au réseau {selected_network}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de se connecter : {str(e)}")

def open_web():
    url = entry.get()
    webbrowser.open(url)

root = tk.Tk()
root.title("Application Wi-Fi et Navigateur Simple")
root.configure(bg='white')  # Fond blanc pour l'interface

# Partie Gestion Wi-Fi
wifi_frame = tk.Frame(root, bg='white')
wifi_frame.pack()

wifi_label = tk.Label(wifi_frame, text="Réseaux disponibles :", bg='white', fg='blue')
wifi_label.pack()

network_list = tk.Listbox(wifi_frame, bg='white', fg='blue')
network_list.pack()

scan_button = tk.Button(wifi_frame, text="Scanner", command=scan_wifi, bg='blue', fg='white')
scan_button.pack()

password_label = tk.Label(wifi_frame, text="Mot de passe :", bg='white', fg='blue')
password_label.pack()

password_entry = tk.Entry(wifi_frame, show="*")
password_entry.pack()

connect_button = tk.Button(wifi_frame, text="Se Connecter", command=connect_wifi, bg='blue', fg='white')
connect_button.pack()

# Partie Navigateur Simple
browser_frame = tk.Frame(root, bg='white')
browser_frame.pack()

browser_label = tk.Label(browser_frame, text="Entrez l'URL :", bg='white', fg='blue')
browser_label.pack()

entry = tk.Entry(browser_frame)
entry.pack()

button = tk.Button(browser_frame, text="Ouvrir", command=open_web)
button.pack()

root.mainloop()
