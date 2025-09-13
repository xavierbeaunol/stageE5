import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

def charger_profil_aile(fichier):
    """Charge un fichier .dat et extrait les coordonnées du profil d'aile."""
    x_coords = []
    y_coords = []
    
    with open(fichier, "r", encoding="utf-8", errors="ignore") as file:
        lignes = file.readlines()
        for line in lignes[1:]:  # Ignorer la première ligne qui contient le nom du profil
            try:
                x, y = map(float, line.split())
                x_coords.append(x)
                y_coords.append(y)
            except ValueError:
                continue  # Ignorer les lignes mal formatées
    
    return np.array(x_coords), np.array(y_coords)

def tracer_profil_aile(x_coords, y_coords, nom_profil="Profil d'Aile"):
    """Trace le profil d'aile avec matplotlib."""
    plt.figure(figsize=(10, 4))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', markersize=3, label=nom_profil)
    plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # Ligne centrale
    plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # Bord d'attaque
    plt.axvline(1, color='black', linewidth=0.5, linestyle="--")  # Bord de fuite
    plt.xlabel("Position relative (X)")
    plt.ylabel("Épaisseur relative (Y)")
    plt.title(f"Visualisation du {nom_profil}")
    plt.legend()
    plt.grid()
    plt.show()

def ouvrir_fichier():
    """Ouvre une boîte de dialogue pour sélectionner un fichier .dat et affiche le profil."""
    fichier = filedialog.askopenfilename(title="Sélectionner un fichier .dat", filetypes=[("Fichiers .dat", "*.dat")])
    if fichier:
        x, y = charger_profil_aile(fichier)
        tracer_profil_aile(x, y, nom_profil=fichier.split("/")[-1])

def interface_graphique():
    """Créer une interface graphique avec un bouton pour charger un fichier."""
    root = tk.Tk()
    root.title("Visualisation du Profil d'Aile")
    root.geometry("300x100")
    
    bouton_ouvrir = tk.Button(root, text="Charger un fichier .dat", command=ouvrir_fichier)
    bouton_ouvrir.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    interface_graphique()
