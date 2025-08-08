import os
import shutil
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def deplacer_fichiers_personnalise():
    dossier_source = champ_dossier.get()
    nom_sous_dossier = champ_nom_dossier.get().strip()
    pourcentage_str = champ_pourcentage.get().strip()

    # Validation des champs
    if not dossier_source or not os.path.isdir(dossier_source):
        messagebox.showerror("Erreur", "Veuillez sélectionner un dossier source valide.")
        return

    if not nom_sous_dossier:
        messagebox.showerror("Erreur", "Veuillez entrer un nom pour le nouveau sous-dossier.")
        return

    try:
        pourcentage = float(pourcentage_str)
        if not (0 < pourcentage <= 100):
            raise ValueError
    except ValueError:
        messagebox.showerror("Erreur", "Le pourcentage doit être un nombre entre 0 et 100.")
        return

    fichiers = [f for f in os.listdir(dossier_source)
                if os.path.isfile(os.path.join(dossier_source, f))]

    if not fichiers:
        messagebox.showinfo("Aucun fichier", "Le dossier ne contient aucun fichier à déplacer.")
        return

    nb_a_deplacer = int(len(fichiers) * (pourcentage / 100))
    if nb_a_deplacer == 0:
        messagebox.showinfo("Info", "Le pourcentage est trop bas pour déplacer au moins un fichier.")
        return

    random.shuffle(fichiers)
    fichiers_a_deplacer = fichiers[:nb_a_deplacer]

    # Créer le nouveau sous-dossier
    chemin_nouveau = os.path.join(dossier_source, nom_sous_dossier)
    os.makedirs(chemin_nouveau, exist_ok=True)

    # Déplacer les fichiers
    for fichier in fichiers_a_deplacer:
        src = os.path.join(dossier_source, fichier)
        dst = os.path.join(chemin_nouveau, fichier)

        # Renommer en cas de doublon
        if os.path.exists(dst):
            base, ext = os.path.splitext(fichier)
            compteur = 1
            nouveau_nom = f"{base}_{compteur}{ext}"
            dst = os.path.join(chemin_nouveau, nouveau_nom)
            while os.path.exists(dst):
                compteur += 1
                nouveau_nom = f"{base}_{compteur}{ext}"
                dst = os.path.join(chemin_nouveau, nouveau_nom)

        shutil.move(src, dst)

    messagebox.showinfo("Succès", f"{nb_a_deplacer} fichier(s) déplacé(s) vers :\n{chemin_nouveau}")

def choisir_dossier():
    dossier = filedialog.askdirectory()
    if dossier:
        champ_dossier.delete(0, tk.END)
        champ_dossier.insert(0, dossier)

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Déplacement personnalisé de fichiers")
fenetre.geometry("500x300")
fenetre.resizable(False, False)

# Widgets
tk.Label(fenetre, text="Dossier source :").pack(pady=5)
cadre_dossier = tk.Frame(fenetre)
champ_dossier = tk.Entry(cadre_dossier, width=50)
champ_dossier.pack(side=tk.LEFT, padx=5)
tk.Button(cadre_dossier, text="Parcourir", command=choisir_dossier).pack(side=tk.LEFT)
cadre_dossier.pack()

tk.Label(fenetre, text="Nom du nouveau sous-dossier :").pack(pady=5)
champ_nom_dossier = tk.Entry(fenetre, width=50)
champ_nom_dossier.insert(0, "Sélection aléatoire")
champ_nom_dossier.pack()

tk.Label(fenetre, text="Pourcentage de fichiers à déplacer (ex : 50) :").pack(pady=5)
champ_pourcentage = tk.Entry(fenetre, width=10)
champ_pourcentage.insert(0, "50")
champ_pourcentage.pack()

tk.Button(fenetre, text="Déplacer les fichiers", command=deplacer_fichiers_personnalise,
          bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)

fenetre.mainloop()
