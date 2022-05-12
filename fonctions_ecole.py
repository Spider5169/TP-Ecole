import os
import json
import fenetres_ecole

#on vérifie qu'il existe un fichier classe.json sinon on le créé
def loader():
    eleves ={}
    if os.path.exists("classe.json") :
        with open("classe.json", "r+") as file :
            eleves = json.load(file)
    else :
        with open("classe.json", "w+") as file :
            json.dump(eleves,file)


#consulter la moyenne d'un élève
def aff_moy():
    with open("classe.json", "r+") as file:
        eleves = json.load(file)

    widget_affiche = fenetres_ecole.Widget(name1="Moyenne d'un élève")

    for liste in eleves :
        fenetres_ecole.Widget.liste_eleve.insert("1.0", liste+"\t")
        fenetres_ecole.Widget.set_hauteur(1)

    widget_affiche.mainloop()

def envoie():
    eleve = fenetres_ecole.Widget.entree.get()
    if eleve in eleves.keys() :
        fenetres_ecole.text.delete("1.0", END)
        fenetres_ecole.text.insert("1.0", f'La Moyenne de {eleve} est de\n {eleves[eleve]["moyenne"]}/20.')
        fenetres_ecole.Widget.destroy()
    else :
        fenetres_ecole.text.delete("1.0", END)
        fenetres_ecole.text.insert("1.0", "L'élève recherché ne fait pas parti de cette classe.")
