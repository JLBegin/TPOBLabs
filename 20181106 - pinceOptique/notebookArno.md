

| **Arnaud Mercier - 111 156 297** | Date: 6 novembre 2018 |
| -------------------------------- | --------------------: |
|                                  |                       |

# Pince Optique			

------

## Question préparatoires

### Pourquoi un objet ayant un indice de réfraction infériur au milieu ambiant ne pourra pas être capturé à l'aide d'un faisceau gaussien?

> La lumière ne sera pas déviée vers le centre de la particule et la force résultante ne poussera donc pas la particule vers le centre du faisceau. 

### Par quels atifices pourrait-on confiner cet objet?

> On pourrait modifier le milieu ambiant afin que son indice de réfraction soit inférieur à l'objet. Il serait aussi possible d'utiliser plusieurs laser de contraindre l'objet malgré la force résultante inverse. 

## Modification du montage fait par les autres équipes

Un laser He-Ne à été ajouté. Celui-ci est utilisé avec la *quadphotodiode* comme référentiel de position.  LA déviation du He-Ne va informer le *quad* sur la déviation de la bille.  Un Laser He-Ne est utilisé pour ne pas *bruler* le *quad*. Les deux faisceau (He-Ne et infrarouge YAG) doivent être doalligné en tout temps. Voir photo nouveau montage.

## Manipulations

### Réponse du détecteur:

*<u>Attention</u>* s'assurer que l'objecctif du bas est dans l'huile

Les 3 moteurs (X,Y,Z) sont ajusté pour voir bien une bille. On voit bien la frontière et aucune partie de l'image est saturé. Une fine ligne définie le contour de la cellule. Sa ne dérange pas trop car on veut que la particule soit au focus de la trappe et non de la lumière blanche.

- On allume le laser He-Ne et on le centre sur l'image de la caméra (X,Y). En bougeant en Z on peut alors voir 3 image de réflexions.

  1. réflexion entre huile et lamelle
  2. réflexion entre lamelle et échantillon
  3. réflexion entre échantillion et lame

- On veut se placer (en Z) entre la réflexion 2 et 3 , ce qui correspond au centre de l'échantillon (en Z)

- On éteint le laser He-Ne et on allume le YAG infrarouge.

- On place un échantillon et on essai de trouvé une bille pour la *trapp* 

  > - Il y a une densité de 10e-02 bille
  >
  > - il y a beaucoup de billes collé sur les paroie pas beaucoup en suspensions, dur d'en trouver une

- important de mettre la lame du bon coté (lamelle vers le bas) et de l'huile

  ### Calibration *quadCell*

- Une bille est centré et les parametres de *jog* sont ajusté dans la page **labView** *controle moteur* pour qu'on voit la cellule se déplacer sur tout l'écran durant une période d'envirion 6 à 7 secondes. 

- axe X

- > step-size = 0.05
  >
  > max velocity = 0.0058

- axe Y

- > step-size = 0.032
  >
  > max velocity = 0.0058

- Dans le logiciel **LabView** *PFL* les réglages suivants sont faits:

- > n. d'échantillons= 90000
  >
  > fréquence = 15000
  >
  > Ces réglages ont été calculé pour etre sur d'enregitré tout le déplacement de la bille

  nom de fichier :calibrationArnoLudoX.xslx et calibrationArnoLudoY.xslx sur l'ordinateur du labo. 

L'échantillonnage automatique n'as pas marché, il y a trop de bruit et un probleme d'enregistrement. EN ouvrant le logiciel du détecteur thorlabs on voit que si on bouge la bille au travers du faisceau nous obtenons la croube voulu. Nous allons donc faire ue calibration manuelle.

> step size 1 micron (limite des moteurs)(attention, backlash sur les moteurs)

On note les voltages initiaux sur  le capteur *quad* et à chaque step de 1 micron on note les voltage correspondant. Par la suit on approxime la région du centre comme une droite et on trouve les pentes.

Il a fallu faire ce processus pour les deux axes, les valeurs sont dans la table suivante:

> pente Y : 0.0087 [volt/micron]
>
> pente X : -0.0083 [volt/micron]

Les données son dans un fichier excel sur l'ordi de ludo :penteQuad.xlxs

### Caractérisation du puit de potentiel  (constante de trappe)

- Guillaume prépare un nouvel échantillon car les billes sont toutes collées sur la lame.
- On *trap* une nouvelle bille et on se déplace à à différentes vitesses. Il est important que la bille reste *trap* tout au long du déplacement
- On veut attendre d'être en vitesse constante avant de lire les voltages du *quad*.
- Pour chaque vitesse on note la différence de potentiel lu par le *quad* à la main.

