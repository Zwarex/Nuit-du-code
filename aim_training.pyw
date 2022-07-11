"""
NOUS AVONS CONCEPTUALISÉ UN "AIM TRAINER".
IL S'AGIT D'UN JEU OU L'ON DOIT CLIQUER SUR LES MONSTRES QUI APPARAISSENT A L'ÉCRAN.
LORSQUE L'ON CLIQUE DESSUS LE MONSTRE DISPARAIT.
PLUS LE JEU AVANCE PLUS LE NOMBRE D'ENNEMI AUGMENTE.
SI UN MONSTRE ARRIVE EN BAS DE L'ÉCRAN ON PERD UNE VIE PUIS AU BOUT DE TROIS VIE PERDU LA PARTIE EST TÉRMINÉE.
POUR CLIQUER SUR LES MONSTRES IL SUFFIT DE DIRIGER LE CURSEUR AVEC LA SOURIS.
"""

from random import randint 
import pyxel as px

px.init(128, 128, title="Train Aim", fps=30)
px.mouse(True)
px.load("2.pyxres")
px.cls(1)
px.playm(0, True)

###############################
# FONCTIONS GÉRANT LE CURSEUR #
###############################

def bouge_curseur():
    """déplacement avec les touches de directions"""
    global curseur_x, curseur_y
    curseur_x = px.mouse_x
    curseur_y = px.mouse_y

def affiche_vie():
    """gère l'affichage des vies"""
    global vie 
    #affiche vie
    if vie == 3:
        px.blt(111, 5, 0, 32, 64, 8, 8, 0)
        px.blt(120, 5, 0, 32, 64, 8, 8, 0)
        px.blt(102, 5, 0, 32, 64, 8, 8, 0)
    elif vie == 2:
        px.blt(102, 5, 0, 32, 72, 8, 8, 0)
        px.blt(111, 5, 0, 32, 64, 8, 8, 0)
        px.blt(120, 5, 0, 32, 64, 8, 8, 0)
    elif vie == 1:
        px.blt(102, 5, 0, 32, 72, 8, 8, 0)
        px.blt(111, 5, 0, 32, 72, 8, 8, 0)
        px.blt(120, 5, 0, 32, 64, 8, 8, 0)
    else :
       game_over()

def spawn_mob():
    """gère le random de l'apparition des mobs"""
    chance = 0 
    if timer <= 10 :
       chance = randint(0,70)
    elif timer <= 40 :
        chance = randint(0,50)
    elif timer <= 60 :
        chance = randint(0,20)
    else :
        chance = randint(0,2)
    if chance == 0 :
       creation_mob()

def game_over():
    """Affiche game over quand les vies sont à 0"""
    px.rect(0, 0, 128, 128, 1)
    px.text(45, 50, "GAME OVER", 7)
    px.text(45, 60, "SCORE "+str(score), 7)

def modif_timer():
    """gère les secondes dans le prgramme"""
    global timer, seconde
    seconde = px.frame_count % 30 
    if seconde == 0 : 
       timer += 1

def affiche_timer():
    """affiche le timer dans le programme"""
    px.text(0,1,"Time:"+str(timer),7)

def click() :
    """gere le click de la souris"""
    global score
    compteur = 0 
    for x,y in zip(mob_x,mob_y) :
        if (curseur_y <= y+8 and curseur_y <= y+8) and ( curseur_x >= x and curseur_x <= x + 8):
           score += 1
           mob_y.pop(compteur)
           mob_x.pop(compteur)
           compteur += 1

def colision() :
    """gere la colision sur l'axe des y"""
    global vie
    compteur = 0
    for y in mob_y :
        if mob_y[compteur] == 128 :
           vie -= 1 
           mob_y.pop(compteur)
           mob_x.pop(compteur) 
        compteur += 1
    return

def affichage_score() :
    """afficeh le score"""
    px.text(97,0,"Score:"+str(score),7)
    
def creation_mob() :
    """créé un mob""" 
    global mob_x,mob_y
    mob_x.append(randint(0,120))
    mob_y.append(15)

def deplacement_mob() :
    """gere le déplacement des mobs"""
    compteur = 0
    for x in mob_y :
        mob_y[compteur]+=1
        compteur += 1

def affichage_mob():
    """affiche les mobs"""
    global vaisseau_y
    for x,y in zip(mob_x,mob_y) :
        px.blt(x, y, 0, 24, 8, 8, 8, 0)
        vaisseau_x.append(x)

def affichage_vaisseau():
    for x in vaisseau_x : 
        px.blt(x,10,0,72,40,16,8,0)
        vaisseau_x.pop(0)
        
##################
# GESTION DU JEU #
##################

def update():
    bouge_curseur()  
    modif_timer()
    if px.btnr(px.MOUSE_BUTTON_LEFT):
        click()

def draw():
    px.cls(1)
    affiche_timer()
    affiche_vie()
    affichage_score()
    if vie >= 0 :
        spawn_mob()
        deplacement_mob()
        affichage_mob()
        affichage_vaisseau()
    colision()

########################
#  PROGRAMME PRINCIPAL #
########################

# position initiale du curseur
# (origine des positions : coin haut gauche)
curseur_x = 2
curseur_y = 2
px.rect(curseur_x,curseur_y,1,1,1)
px.blt(64,10,0,72,40,16,8,0)
vaisseau_x = []
#affichage
score = 0
vie = 3 
mob_x = []
mob_y = []
#gestion globale du jeu
timer,seconde,temp_timer = 0,0,""
chance = 0
#Jeu
px.run(update,draw)
