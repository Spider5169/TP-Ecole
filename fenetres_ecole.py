from tkinter import *
import fonctions_ecole

#ouverture fenetre principale
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
text = Text(frameb, bd=5, wrap=WORD, width= 30, highlightthickness=5)
text.grid(row=0, rowspan=4, column=2)

#grille de 4 boutons
width = 200
height = 180
image1 = PhotoImage(file="note.png").zoom(15).subsample(25)
image2 = PhotoImage(file="commentaire.png").zoom(15).subsample(25)
image3 = PhotoImage(file="nouveau.png").zoom(15).subsample(22)
image4 = PhotoImage(file="supprimer.png").zoom(15).subsample(25)

bouton1= Button(frameb, image= image1,bg='#C0ECF2', width= width, height= height, command= fonctions_ecole.aff_moy)
bouton1.grid(row=0, column=0, sticky=W)
label_bt1= Label(frameb,text="Note", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt1.grid(row=1, column=0)
bouton2= Button(frameb, image= image2,bg='#C0ECF2', width= width, height= height, command= 'fonctions_ecole.aff_com')
bouton2.grid(row=0, column=1, sticky=W)
label_bt2= Label(frameb,text="Appréciations", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt2.grid(row=1, column=1)
bouton3= Button(frameb, image= image3,bg='#C0ECF2', width= width, height= height, command= 'fonctions_ecole.add_eleve')
bouton3.grid(row=2, column=0, sticky=W)
label_bt3= Label(frameb,text="Ajouter", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt3.grid(row=3, column=0)
bouton4= Button(frameb, image= image4,bg='#C0ECF2', width= width, height= height, command= 'fonctions_ecole.remove_eleve')
bouton4.grid(row=2, column=1, sticky=W)
label_bt4= Label(frameb,text="Supprimer", font=('Courier',15),bg='#C0ECF2',fg='black')
label_bt4.grid(row=3, column=1)

'''
#barre menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Note d'un élève", command= fonctions_ecole.aff_moy)
file_menu.add_command(label="Appréciations de la classe", command= fonctions_ecole.aff_com)
file_menu.add_command(label="Ajouter nouvel élève", command= fonctions_ecole.add_eleve)
file_menu.add_command(label="Supprimer un élève", command= fonctions_ecole.remove_eleve)
file_menu.add_command(label="Quitter", command= window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)
'''
window.mainloop()

#ouverture d'une fenetre temporaire

class Widget :

    largeur = 480
    hauteur = 360
    hauteur_liste = 1.0

    def __init__(self,name1):
        self.nom = name1

    def get_nom(self):
        return self.nom
'''
    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur

    def get_hauteur_liste(self):
        return self.hauteur_liste
'''
    def set_hauteur(self, change_hauteur):
        self.hauteur_liste += change_hauteur

    win_widget = Tk()
    win_widget.title(str(get_nom))
    win_widget.geometry("480x360")
    win_widget.iconbitmap("choix.ico")
    win_widget.config(background='#C0ECF2')

    frame0 = Frame(win_widget, bg ='#C0ECF2', bd = 5, relief=RAISED)
    frame0.pack(expand=YES)
    label0 = Label(frame0, text="liste des élèves de la classe :", font=('Courier',15),bg='#C0ECF2',fg='black')
    label0.pack()
    liste_eleve = Text(frame0, font=("Helvetica", 20),wrap=WORD, bg='#55b4dd', fg='white', width=20, height= hauteur_liste)
    liste_eleve.pack()

    frame1= Frame(win_widget, bg ='#C0ECF2', bd = 5, relief=SUNKEN)
    frame1.pack(expand=YES)
    label1 = Label(frame1, text="Saisissez le prénom d'un élève : ", font=('Courier',15),bg='#C0ECF2',fg='black')
    label1.grid(row=0, column=0, columnspan=2)
    entree = Entry(frame1, font=("Helvetica", 20), bg='#55b4dd', fg='white')
    entree.grid(row=1, column=0,)

    bt1 = Button(frame1, text=("OK"), bg='#C0ECF2', width= 6, height= 2, command= fonctions_ecole.envoie)
    bt1.grid(row=1, column=1)

    win_widget.mainloop()
