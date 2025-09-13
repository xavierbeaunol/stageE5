import tkinter as tk
from tkinter import filedialog, messagebox

def convert_dat_to_obj(input_path, output_path):
    try:
        with open(input_path, 'r') as dat_file, open(output_path, 'w') as obj_file:
            obj_file.write("# NACA Airfoil\n")
            obj_file.write("o Airfoil\n")
            
            vertices = []
            for line in dat_file:
                x, y = map(float, line.split())
                vertices.append((x, y, 0))  # Ajouter z = 0 pour une forme 2D
            
            # Écrire les sommets
            for v in vertices:
                obj_file.write(f"v {v[0]} {v[1]} {v[2]}\n")
            
            # Écrire les faces (en supposant que les points sont ordonnés)
            obj_file.write("l ")
            for i in range(1, len(vertices) + 1):
                obj_file.write(f"{i} ")
            obj_file.write("1\n")  # Fermer la boucle
        
        messagebox.showinfo("Succès", f"Le fichier a été converti avec succès et enregistré sous :\n{output_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite :\n{str(e)}")

def select_input_file():
    input_path = filedialog.askopenfilename(
        title="Sélectionnez le fichier .dat",
        filetypes=[("Fichiers DAT", "*.dat"), ("Tous les fichiers", "*.*")]
    )
    if input_path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, input_path)

def select_output_file():
    output_path = filedialog.asksaveasfilename(
        title="Enregistrer le fichier .obj",
        defaultextension=".obj",
        filetypes=[("Fichiers OBJ", "*.obj"), ("Tous les fichiers", "*.*")]
    )
    if output_path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_path)

def start_conversion():
    input_path = input_file_entry.get()
    output_path = output_file_entry.get()
    
    if not input_path or not output_path:
        messagebox.showwarning("Attention", "Veuillez sélectionner un fichier d'entrée et un fichier de sortie.")
        return
    
    convert_dat_to_obj(input_path, output_path)

# Interface graphique
root = tk.Tk()
root.title("Convertisseur DAT vers OBJ")

# Champ pour le fichier d'entrée
tk.Label(root, text="Fichier .dat d'entrée :").grid(row=0, column=0, padx=5, pady=5)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Parcourir...", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Champ pour le fichier de sortie
tk.Label(root, text="Fichier .obj de sortie :").grid(row=1, column=0, padx=5, pady=5)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Parcourir...", command=select_output_file).grid(row=1, column=2, padx=5, pady=5)

# Bouton pour lancer la conversion
tk.Button(root, text="Convertir", command=start_conversion).grid(row=2, column=1, pady=10)

# Lancer l'interface
root.mainloop()