import tkinter as tk
from tkinter import ttk
import math

# Constantes
AIR_DENSITY = 1.225  # Densité de l'air en kg/m^3

# Fonction pour calculer la portance
def calculate_lift():
    diameter = diameter_scale.get() / 100  # Convertir en mètres
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    cl = cl_scale.get()
    rpm = rpm_scale.get()
    velocity = (rpm * diameter * math.pi) / 60  # Vitesse en m/s

    lift = 0.5 * AIR_DENSITY * area * cl * (velocity ** 2)
    lift_label.config(text=f"Portance: {lift:.2f} N")
    weight_label.config(text=f"Poids supportable: {lift / 9.81:.2f} kg")

# Fonction pour mettre à jour les valeurs des curseurs
def update_values(event=None):
    diameter_value_label.config(text=f"Diamètre: {diameter_scale.get():.2f} cm")
    cl_value_label.config(text=f"Coefficient de portance (Cl): {cl_scale.get():.2f}")
    rpm_value_label.config(text=f"RPM: {rpm_scale.get():.0f}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calcul de Portance d'Hélice")

# Curseur pour le diamètre de l'hélice (en cm)
diameter_label = ttk.Label(root, text="Diamètre de l'hélice (cm):")
diameter_label.pack()
diameter_scale = ttk.Scale(root, from_=10, to=100, orient="horizontal")
diameter_scale.set(50)  # Valeur par défaut
diameter_scale.pack()
diameter_value_label = ttk.Label(root, text="Diamètre: 50.00 cm")
diameter_value_label.pack()

# Curseur pour le coefficient de portance (Cl)
cl_label = ttk.Label(root, text="Coefficient de portance (Cl):")
cl_label.pack()
cl_scale = ttk.Scale(root, from_=0.1, to=2.0, orient="horizontal")
cl_scale.set(1.0)  # Valeur par défaut
cl_scale.pack()
cl_value_label = ttk.Label(root, text="Coefficient de portance (Cl): 1.00")
cl_value_label.pack()

# Curseur pour le RPM
rpm_label = ttk.Label(root, text="RPM:")
rpm_label.pack()
rpm_scale = ttk.Scale(root, from_=1000, to=10000, orient="horizontal")
rpm_scale.set(5000)  # Valeur par défaut
rpm_scale.pack()
rpm_value_label = ttk.Label(root, text="RPM: 5000")
rpm_value_label.pack()

# Bouton pour calculer la portance
calculate_button = ttk.Button(root, text="Calculer la Portance", command=calculate_lift)
calculate_button.pack()

# Labels pour afficher les résultats
lift_label = ttk.Label(root, text="Portance: ")
lift_label.pack()
weight_label = ttk.Label(root, text="Poids supportable: ")
weight_label.pack()

# Lier les curseurs à la fonction de mise à jour
diameter_scale.bind("<Motion>", update_values)
cl_scale.bind("<Motion>", update_values)
rpm_scale.bind("<Motion>", update_values)

# Lancer l'interface
root.mainloop()