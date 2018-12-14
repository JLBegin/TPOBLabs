

| **Ludovick Bégin - 111 159 148** | Date: 4 décembre 2018 |
| -------------------------------- | --------------------: |
|                                  |                       |

## Oxymétrie - Partie 1

### But

Mettre en application les notions d'oxymétrie et d'électronique afin de bâtir un sphygmo-oxymètre.


### Préparation

***1. Quelle est la plus grosse approximation dans ce laboratoire ?***

La loi de Beer-Lambert qui décrit l'atténuation d'un signal lumineux dans un matériau fonctionne si ce matériau est isotrope et homogène. On approxime alors les tissus humains comme un matériau isotrope et homogène. 


### Manipulations

#### Générateur de fonctions

Le tout est effectué à l'aide du programme LabView `oxymètre.lvm`. 

- Labview affiche une moyenne de 0V sur le channel rouge et 2.5V sur le channel infrarouge.

- Connection des sorties de la carte d'acquisition sur l'oscilloscope.

  - AO0 (Branche 4) vers Channel 1

  - AO1 (Branche 2) vers Channel 2

  > Il faut régler les deux channels de l'oscilloscope en mode couplage C-C pour voir l'onde carré.

- On règle les deux channels sur LabView à 3V et on observe leur signal sur l'oscilloscope: 
  - Channel 1 et channel 2: 
    - Tension crète à crète : 3.20 V
    - Fréquence : 33.33 Hz

    > On observe des ondes carrés qui sont déphasées afin d'allumer les deux LED en alternance (pour le tier du temps chacun). 

- On connecte les sorties de la carte d'acquisition (AO0 et AO1) à l'oxymètre afin d'alimenter ce dernier avec le générateur de fonctions.
- On voit la lumière rouge en marche, la lumière infrarouge reste toutefois invisible même sur la carte infrarouge. 


#### Circuit de détection

![Circuit de détection](circuit_detection.PNG)

- Ce circuit est monté en respectant les indications sur la figure.

  > Nous obtenions que du bruit à la sortie de l'amplificateur et le changement de la transimpédance n'aide pas la cause.

  > Après changement de la puce OP27 nous obtenons un beau signal carré qui s'apparente au DAC avec le double de la fréquence (66.66 Hz). L'ancienne puce (non-fonctionnelle) est jetée au poubelle. On garde maintenant la résistance de 1M$\Omega$. 

- Le condensateur (à droite sur la figure du circuit) est fixé à 0.2 $\mu F$ avec la boîte Cap-Range afin d'obtenir un filtre passe-bas décent sur le signal. 

- La fréquence de coupure est calculée à environ 800 Hz.

![Signal observé en détection](signal_detection.jpg)

- Signal observé en détection (haut) et signal d'entré pour l'une des DEL (bas). 


#### Circuit de gain par transitor pour le courant de la DEL

![Circuit d'amplification pour une DEL](circuit_ampli.PNG)

Ce circuit est monté en respectant les indications sur la figure.


##### Mesures de $I_c$:

- Range ampèremètre reglé à 200mA

| AO0 (V)    | $I_c $ (mA) |
| ---------- | ----------- |
| $\pm$ 0.01 | $\pm$ 0.2   |
| 0.80       | 14.9        |
| 0.90       | 23.5        |
| 1.00       | 27.2        |
| 1.10       | 28.7        |
| 1.20       | 35.6        |
| 1.30       | 38.7        |
| 1.40       | 39.6        |



##### Mesures de $I_b$:

- Range ampèremètre reglé à 2000 $\mu$A

| AO0 (V)    | $I_b $ ($\mu$A) |
| ---------- | --------------- |
| $\pm$ 0.01 | $\pm$ 2         |
| 0.80       | 61              |
| 0.90       | 115             |
| 1.00       | 172             |
| 1.10       | 230             |
| 1.20       | 290             |
| 1.30       | 350             |
| 1.40       | 416             |



- Valeur moyenne du gain $h_{FE} = I_c / I_b = 40x/0.59x = 68$



## Deuxième séance

- On interchange Ox3 et Ox2 afin de tester la lumière infrarouge. 



##### Mesures de $I_c$:

- Range ampèremètre 200mA

| AO0 (V)    | $I_c $ (mA) |
| ---------- | ----------- |
| $\pm$ 0.01 | $\pm$ 0.2   |
| 0.80       | 14.9        |
| 0.90       | 18.9        |
| 1.00       | 30.0        |
| 1.10       | 33.3        |
| 1.20       | 38.4        |
| 1.30       | 41.8        |
| 1.40       | 44.9        |



##### Mesures de $I_b$:

- Range ampèremètre 2000 $\mu$A

| AO0 (V)    | $I_b $ ($\mu$A) |
| ---------- | --------------- |
| $\pm$ 0.01 | $\pm$ 2         |
| 0.80       | 97              |
| 0.90       | 180             |
| 1.00       | 270             |
| 1.10       | 320             |
| 1.20       | 346             |
| 1.30       | 422             |
| 1.40       | 500             |



- Valeur moyenne du gain $h_{FE} = I_c / I_b = 51x/0.63x = 81$



#### Montage complet du sphygmo-oxymètre

![](circuit_final.PNG)

- Ce circuit est monté en respectant les indications sur la figure.
- La lecture en tension sur LabView est de 8.3 V au lieu de 9V sur chaque graphique



#### Calibration et calcul du SpO2

- Pouls déjà bien calibrer avec 60 sur l'oxymètre portable et le nôtre. 

- SpO2 est initialement autour de 91% au lieu de 98%.

- Facteur de calibration à 1.1 pour SpO2.

- Prise de données sauvegardé sur clé usb.



