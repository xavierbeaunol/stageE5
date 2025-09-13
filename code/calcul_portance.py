import tkinter as tk
from tkinter import ttk

# Constantes
rho = 1.225  # Densité de l'air en kg/m^3 (au niveau de la mer)
Cl = 0.8  # Coefficient de portance typique

# Fonction pour mettre à jour les labels des curseurs
def update_label_envergure(value):
    label_valeur_envergure.config(text=f"{float(value):.2f} m")

def update_label_corde(value):
    label_valeur_corde.config(text=f"{float(value):.2f} m")

def update_label_vitesse(value):
    label_valeur_vitesse.config(text=f"{float(value):.0f} km/h")

# Fonction pour calculer la portance
def calculer_portance():
    try:
        # Récupérer les valeurs des curseurs
        envergure = float(curseur_envergure.get())
        corde = float(curseur_corde.get())
        vitesse = float(curseur_vitesse.get()) * 1000 / 3600  # Conversion de km/h en m/s

        # Calcul de la surface de l'aile
        surface = envergure * corde

        # Calcul de la portance (formule complète)
        portance = 0.5 * rho * surface * (vitesse ** 2) * Cl

        # Affichage des résultats
        label_surface.config(text=f"Surface de l'aile: {surface:.2f} m²")
        label_portance.config(text=f"Portance: {portance:.2f} N")
        label_poids.config(text=f"Poids supporté: {portance / 9.81:.2f} kg")

    except ValueError:
        label_surface.config(text="Erreur: Entrez des valeurs valides")
        label_portance.config(text="")
        label_poids.config(text="")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calcul de Portance d'une Aile de Drone")

# Cadre pour les entrées
frame_entrees = ttk.Frame(root, padding="10")
frame_entrees.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Curseur pour l'envergure
label_envergure = ttk.Label(frame_entrees, text="Envergure (m):")
label_envergure.grid(row=0, column=0, sticky=tk.W)
curseur_envergure = ttk.Scale(frame_entrees, from_=0.1, to=4.0, orient=tk.HORIZONTAL, length=200, command=update_label_envergure)
curseur_envergure.set(1.0)
curseur_envergure.grid(row=0, column=1, sticky=tk.W)
label_valeur_envergure = ttk.Label(frame_entrees, text="1.00 m")
label_valeur_envergure.grid(row=0, column=2, sticky=tk.W)

# Curseur pour la corde
label_corde = ttk.Label(frame_entrees, text="Corde (m):")
label_corde.grid(row=1, column=0, sticky=tk.W)
curseur_corde = ttk.Scale(frame_entrees, from_=0.05, to=1.5, orient=tk.HORIZONTAL, length=200, command=update_label_corde)
curseur_corde.set(0.2)
curseur_corde.grid(row=1, column=1, sticky=tk.W)
label_valeur_corde = ttk.Label(frame_entrees, text="0.20 m")
label_valeur_corde.grid(row=1, column=2, sticky=tk.W)

# Curseur pour la vitesse de croisière
label_vitesse = ttk.Label(frame_entrees, text="Vitesse de croisière (km/h):")
label_vitesse.grid(row=2, column=0, sticky=tk.W)
curseur_vitesse = ttk.Scale(frame_entrees, from_=10, to=100, orient=tk.HORIZONTAL, length=200, command=update_label_vitesse)
curseur_vitesse.set(50)
curseur_vitesse.grid(row=2, column=1, sticky=tk.W)
label_valeur_vitesse = ttk.Label(frame_entrees, text="50 km/h")
label_valeur_vitesse.grid(row=2, column=2, sticky=tk.W)

# Bouton pour calculer la portance
bouton_calculer = ttk.Button(frame_entrees, text="Calculer la Portance", command=calculer_portance)
bouton_calculer.grid(row=3, column=0, columnspan=3, pady=10)

# Cadre pour les résultats
frame_resultats = ttk.Frame(root, padding="10")
frame_resultats.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels pour afficher les résultats
label_surface = ttk.Label(frame_resultats, text="Surface de l'aile: ")
label_surface.grid(row=0, column=0, sticky=tk.W)
label_portance = ttk.Label(frame_resultats, text="Portance: ")
label_portance.grid(row=1, column=0, sticky=tk.W)
label_poids = ttk.Label(frame_resultats, text="Poids supporté: ")
label_poids.grid(row=2, column=0, sticky=tk.W)

# Lancer l'application
root.mainloop()