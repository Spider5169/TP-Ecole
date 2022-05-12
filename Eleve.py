'''
import fenetres_ecole
import fonctions_ecole

if __name__ == '__main__':
    fonctions_ecole.loader()
    fenetres_ecole.window.mainloop()
'''

from tkinter import *
import os
import json

eleves = {}
def loader():
    global eleves
    if os.path.exists("classe.json") :
        with open("classe.json", "r+") as file :
            eleves = json.load(file)
    else :
        with open("classe.json", "w+") as file :
            json.dump(eleves,file)


loader()
#consulter la moyenne d'un élève
def aff_moy():
    with open("classe.json", "r+") as file:
        eleves = json.load(file)
# fenetre d'entree de nom
    widget = Tk()
    widget.title("Entrer le nom d'un élève")
    widget.geometry("480x250")
    widget.iconbitmap("choix.ico")
    widget.config(background='#C0ECF2')
# affichage de la liste des eleves
    leh = 1
    frame0 = Frame(widget, bg ='#C0ECF2', bd = 5, relief=RAISED)
    frame0.pack(expand=YES)
    label0 = Label(frame0, text="liste des élèves de la classe :", font=('Courier',15),bg='#C0ECF2',fg='black')
    label0.pack()
    liste_eleve = Text(frame0, font=("Helvetica", 20),wrap=WORD, bg='#55b4dd', fg='white', width=20, height= leh)
    liste_eleve.pack()
    for liste in eleves :
        liste_eleve.insert("1.0", liste+"\t")
        leh += 0.5
        liste_eleve.config(height=leh)

#saisie du nom de l'élève
    frame1= Frame(widget, bg ='#C0ECF2', bd = 5, relief=SUNKEN)
    frame1.pack(expand=YES)
    label1 = Label(frame1, text="Saisissez le prénom d'un élève : ", font=('Courier',15),bg='#C0ECF2',fg='black')
    label1.grid(row=0, column=0, columnspan=2)
    entree = Entry(frame1, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree.grid(row=1, column=0,)
    def envoie():
        eleve = entree.get()
        if eleve in eleves.keys() :
            text.delete("1.0", END)
            text.insert("1.0", f'La Moyenne de {eleve} est de\n {eleves[eleve]["moyenne"]}/20.')
            widget.destroy()
        else :
            text.delete("1.0", END)
            text.insert("1.0", "L'élève recherché ne fait pas parti de cette classe.")

    bt1 = Button(frame1, text=("OK"), bg='#C0ECF2', width= 6, height= 2, command= envoie)
    bt1.grid(row=1, column=1)
    widget.mainloop()


#affichage de toutes les appréciations de la classe
def aff_com():
    global eleves
    with open("classe.json", "r+") as file:
        eleves = json.load(file)
        text.delete("1.0", END)
    for com in eleves.values() :
        text.insert("1.0", com['appreciation']+"\n")


#ajout d'un élève à la classe
def add_eleve():
# fenetre d'ajout
    widget2 = Tk()
    widget2.title("Ajouter un nouvel élève")
    widget2.geometry("480x360")
    widget2.iconbitmap("choix.ico")
    widget2.config(background='#C0ECF2')
#champs à remplir
    frame2= Frame(widget2, bg ='#C0ECF2', bd = 5, relief=SUNKEN)
    frame2.pack(expand=YES)
    label2 = Label(frame2, text="Saisissez le prénom d'un élève : ", font=('Courier',15),bg='#C0ECF2',fg='black')
    label2.grid(row=0, column=0, columnspan=2)
    entree2 = Entry(frame2, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree2.grid(row=1, column=0,)
    label3 = Label(frame2, text="Saisissez la moyenne de l'élève : ", font=('Courier',15),bg='#C0ECF2',fg='black')
    label3.grid(row=2, column=0, columnspan=2)
    entree3 = Entry(frame2, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree3.grid(row=3, column=0,)
    label4 = Label(frame2, text="Saisissez l'appréciation de l'élève : ", font=('Courier',15),bg='#C0ECF2',fg='black')
    label4.grid(row=4, column=0, columnspan=2)
    entree4 = Entry(frame2, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree4.grid(row=5, column=0,)
#attribution des entrées à des variables
    def envoie2():
        nom = entree2.get()
        note = entree3.get()
        comment = entree4.get()
        if nom == "" or note == "" or comment == "" :
            widget2.destroy()
            add_eleve()
        else :
#ajout au dictionnaire
            with open("classe.json", "r+") as file:
                eleves = json.load(file)
            eleves [nom]={
                "moyenne": note,
                "appreciation" : comment
            }
#confirmation à l'utilisateur
            text.delete("1.0", END)
            text.insert(
                "1.0",
                f"l'élève {nom} à bien été ajouté à la classe, avec {note}/20 de moyenne\net cette appréciation : {comment}"
            )
#ajout/création au fichier de la classe
            with open ("classe.json", "w+") as file2 :
                json.dump(eleves, file2)
            widget2.destroy()


    bt2 = Button(frame2, text=("Annuler"), bg='#C0ECF2', width= 6, height= 2, command= widget2.destroy)
    bt2.grid(row=6, column=0, sticky=E)
    bt3 = Button(frame2, text=("OK"), bg='#C0ECF2', width= 6, height= 2, command= envoie2)
    bt3.grid(row=6, column=1)
    widget2.mainloop()


#suppression d'un élève
def remove_eleve():
    with open("classe.json", "r+") as file:
        eleves = json.load(file)
# fenetre d'entree de nom
    widget3 = Tk()
    widget3.title("Supprimer un élève")
    widget3.geometry("480x250")
    widget3.iconbitmap("choix.ico")
    widget3.config(background='#C0ECF2')
# affichage de la liste des eleves
    leh2 = 1
    frame4 = Frame(widget3, bg='#C0ECF2', bd=5, relief=RAISED)
    frame4.pack(expand=YES)
    label4 = Label(frame4, text="liste des élèves de la classe :", font=('Courier', 15), bg='#C0ECF2', fg='black')
    label4.pack()
    liste_eleve2 = Text(frame4, font=("Helvetica", 20), wrap=WORD, bg='#55b4dd', fg='white', width=20, height=leh2)
    liste_eleve2.pack()
    for liste2 in eleves:
        liste_eleve2.insert("1.0", liste2 + "\t")
        leh2 += 0.5
        liste_eleve2.config(height=leh2)
# saisie du nom de l'élève
    frame5 = Frame(widget3, bg='#C0ECF2', bd=5, relief=SUNKEN)
    frame5.pack(expand=YES)
    label5 = Label(frame5, text="Saisissez le prénom d'un élève : ", font=('Courier', 15), bg='#C0ECF2', fg='black')
    label5.grid(row=0, column=0, columnspan=2)
    entree_sup = Entry(frame5, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree_sup.grid(row=1, column=0, )

    def envoie3():
        eleve = entree_sup.get()
        if eleve in eleves.keys():
            del eleves[eleve]
            with open("classe.json", "w+") as file4:
                json.dump(eleves, file4)
            text.delete("1.0", END)
            text.insert("1.0", f"L'élève {eleve} vient d'être supprimé")
            widget3.destroy()
            remove_eleve()
        else:
            text.delete("1.0", END)
            text.insert("1.0", "L'élève recherché ne fait pas parti de cette classe.")

    bt1 = Button(frame5, text=("OK"), bg='#C0ECF2', width=6, height=2, command=envoie3)
    bt1.grid(row=1, column=1)
    widget3.mainloop()


#Fenetre Principale du Programme
window = Tk()
window.title("CHOIX")
window.geometry("720x640")
window.minsize(480,360)
window.iconbitmap("choix.ico")
window.config(background='#C0ECF2')
#titre
framea= Frame(window, bg ='#C0ECF2', bd = 1, relief=SUNKEN)
framea.pack(expand=YES)
label_titre= Label(framea, text="Que voulez-vous faire ?", font=('Courier',35),bg='#C0ECF2',fg='black')
label_titre.pack(side=TOP)
bouton_titre = Button (window, text="Quit", command= window.quit)
bouton_titre.pack(side=BOTTOM)
#frame des boutons de choix
frameb= Frame(window, bg ='#C0ECF2', bd = 1, relief=SUNKEN)
frameb.pack(expand=YES)

# zone affichage à droite
text = Text(frameb, bd=5, wrap=WORD, width= 30, highlightthickness=5,)
text.grid(row=0, rowspan=4, column=2)

#grille de 4 boutons
width = 200
height = 180
image1 = PhotoImage(file="note.png").zoom(15).subsample(25)
image2 = PhotoImage(file="commentaire.png").zoom(15).subsample(25)
image3 = PhotoImage(file="nouveau.png").zoom(15).subsample(22)
image4 = PhotoImage(file="supprimer.png").zoom(15).subsample(25)

bouton1= Button(frameb, image= image1,bg='#C0ECF2', width= width, height= height, command=aff_moy)
bouton1.grid(row=0, column=0, sticky=W)
label_bt1= Label(frameb,text="Note", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt1.grid(row=1, column=0)
bouton2= Button(frameb, image= image2,bg='#C0ECF2', width= width, height= height, command= aff_com)
bouton2.grid(row=0, column=1, sticky=W)
label_bt2= Label(frameb,text="Appréciations", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt2.grid(row=1, column=1)
bouton3= Button(frameb, image= image3,bg='#C0ECF2', width= width, height= height, command= add_eleve)
bouton3.grid(row=2, column=0, sticky=W)
label_bt3= Label(frameb,text="Ajouter", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt3.grid(row=3, column=0)
bouton4= Button(frameb, image= image4,bg='#C0ECF2', width= width, height= height, command= remove_eleve)
bouton4.grid(row=2, column=1, sticky=W)
label_bt4= Label(frameb,text="Supprimer", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt4.grid(row=3, column=1)

#barre menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Note d'un élève", command=aff_moy)
file_menu.add_command(label="Appréciations de la classe", command=aff_com)
file_menu.add_command(label="Ajouter nouvel élève", command=add_eleve)
file_menu.add_command(label="Supprimer un élève", command=remove_eleve)
file_menu.add_command(label="Quitter", command= window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)


window.mainloop()

