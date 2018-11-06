

| **Ludovick Bégin - 111 159 148** | Date: 6 novembre 2018 |
| -------------------------------- | --------------------: |
|                                  |                       |

# Pince Optique - Partie 1



### Préparation

**_Pourquoi un objet ayant un indice de réfraction inférieur au milieu ambiant ne pourra pas être capturé à l'aide d'un faisceau gaussien?_**

La lumière ne sera pas déviée vers le centre de la particule et la force résultante ne poussera donc pas la particule vers le centre du faisceau. 

**_Par quels atifices pourrait-on confiner cet objet?_**

On pourrait modifier le milieu ambiant afin que son indice de réfraction soit inférieur à l'objet. Il serait aussi possible d'utiliser plusieurs laser de contraindre l'objet malgré la force résultante inverse. 



**[Photo du montage]**



Le montage original a précédement été modifié. Un laser He-Ne a été rajouté afin de ne pas endommager le _QuadCell_ et permettre un alignement plus facile et sécuritaire. Les deux lasers se rendent alors à l'échantillon et la déviation du laser He-Ne informe le _QuadCell_ de la position de la bille à l'échantillon.

Une lame contenant un échantillon de microbilles de 6 um de diamètre à concentration 10^-6 a déjà été préparé et placé sur l'objectif. 

> Lorsque le laser He-Ne est allumé, l'image n'est pas clair. 

### Alignement et mise au point

- Une bille est centré à l'image à l'aide des contrôles en X et Y du stage. On place alors l'image au focus avec le contrôle en Z afin d'obtenir une image clair où la circonférence de la bille est bien définie. 
- On observe l'image du laser He-Ne aux trois interfaces où il y a réflexion, soit à l'interface entre l'huile de l'objectif et la lame de verre et un interface au début et à la fin de l'échantillon (lame-eau). 
- Le sytème est aligné en corrigeant la position du miroir du He-Ne afin de centrer l'image du laser dans le détecteur à la position (0, 0). 
- Les billes observables sont tous collés à l'interface de la lame de verre et de l'échantillon. Guillaume part alors préparer un nouvel échantillon dans lequel on peut observer les billes libres. 
- On met les lunettes de protection et allume le laser infrarouge YAG. Il est maintenant possible de contrôler la position des billes. 

- On éteint le laser infrarouge.



### Calibration du QuadCell

- On trouve une bille collée à la surface de sorte qu'elle ne bouge pas pendant l'acquisition. On centre la bille sur un axe et la place sur le côté pour l'autre axe. 
- On programme alors sur le logiciel LabView `Controle Moteur.vi` un déplacement de 0.05 à une vitesse de 0.0058. 
- On part une acquisition sur le QuadCell à l'aide du logiciel LabView `PFM.vi` avec une fréquence de 10 kHz pour 60 000 échantillons. 
- On allume le laser He-Ne et part l'acquisition avec le déplacement programmé. 

- Résultats pour l'axe X : 

  > Relation non linéaire. 

- Résultats pour l'axe Y:



- L'acquisition par la carte est très bruité et ne donne pas la relation attendue lorsqu'on balais la bille. 
- On passe alors en acquisition manuelle afin de prendre les mesures sans passer par la carte d'acquisition. On fait des step de 1 um et traverse la bille dans l'axe Y en notant la tension du QuadCell sur X diff. 



| Distance ($\mu$m) | Tension (V) |
| ----------------- | ----------- |
| +/-               | +/-  0.005  |
| 0                 | 0.034       |
| 1                 | 0.034       |
| 2                 | 0.034       |
| 3                 | 0.032       |
| 4                 | 0.019       |
| 5                 | -0.032      |
| 6                 | -0.002      |
| 7                 | 0.004       |
| 8                 | 0.012       |
| 9                 | 0.025       |
| 10                | 0.031       |
| 11                | 0.060       |
| 12                | 0.070       |
| 13                | 0.058       |
| 14                | 0.037       |
| 15                | 0.038       |
| 16                | 0.037       |
| 17                | 0.037       |

- Cela donne une pente linéaire au centre de la courbe de **8700 V/m**.



#### Pente axe X

- On fait de même pour l'axe X, en prenant les mesures du Y Diff sur le QuadCell. 



| Distance ($\mu$m) | Tension (V) |
| ----------------- | ----------- |
| +/-               | +/- 0.005   |
| 0                 | -0.0062     |
| 1                 | -0.0063     |
| 2                 | -0.0070     |
| 3                 | -0.0070     |
| 4                 | -0.0065     |
| 5                 | -0.004      |
| 6                 | -0.002      |
| 7                 | 0.025       |
| 8                 | 0.045       |
| 9                 | 0.030       |
| 10                | 0.035       |
| 11                | 0.016       |
| 12                | 0.0063      |
| 13                | 0.00        |
| 14                | -0.009      |
| 15                | -0.012      |
| 16                | -0.023      |
| 17                | -0.035      |
| 18                | -0.035      |
| 19                | -0.049      |
| 20                | -0.03       |
| 21                | -0.006      |
| 23                | -0.006      |
| 24                | -0.005      |
| 25                | -0.005      |

- Cela donne une pente linéaire au centre de la courbe de **-8300 V/m**.





### Caractérisation du puit de potentiel

- On change à nouveau l'échantillon puisqu'on n'y trouve plus de billes libres.
- On capte une bille avec la pince optique et on réaligne le laser infrarouge afin de positionner la bille au centre du QuadCell et lire une tension d'environ 0 Volt dans les 2 axes. 
- Pour chaque valeur de tension on soustrait la tension de base avant le mouvement. 
- L'acquisition est faite pour l'axe Y.

| Vitesse (mm/s) | Différence de tension (V) |
| -------------- | ------------------------- |
| ----           | +/- 0.003                 |
| 0.02           | 0                         |
| 0.03           | 0.005                     |
| 0.05           | 0.010                     |
| 0.08           | 0.015                     |

