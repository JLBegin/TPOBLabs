| **Arnaud Mercier - 111 156 297** | Date: 4 décembre 2018 |
| -------------------------------- | --------------------: |
|                                  |                       |

# Oxymetrie								semaine 1

------



## Question préparatoires

### Quel est la plus grosse approximation dans ce lab:

> beer lambert -> les tissu sont isotrope et homogène



## En labo

### Générateurs de fonctions

On observe des ondes carrés  pour les deux channels sur l'oscilloScope

> il faut bien réglé les deux channels a couplage C-C pour avoir de belles ondes carré

Sur le logiciel oxymètre, on set les channel à 3 volts:

On mesure les valeurs suivantes sur l'oscilloscope

 channel 2 (pin 2 AO1) -> max: 3.2+/- 0.1, freq: 33 +/- 1 Hz

channel 1 (pin 4 AO 0) -> max: 3.2 +/- 0.1 , freq : 33 +/- 1 Hz

> il est impossible de voir l'infrarouge , il faudrait etre dans le noir total
>
> Nous pouvons cependant très bien voir la diode rouge

### Circuit d'amplification (détection)

Nous avons réalisé le montage de la figure 7

> nous obtenions que du bruit à la sortie de l'ampli
>
> Après chagement de puce OP27 nous obtenons un beau signal carré qui s'apparente au DAC avec le double de fréquence

Afin d'atténuer le bruit dans les hautes fréquances , la valeur d'un condensateur est ajusté afin d'avoir un effet passe bas

> valeur de 0.2$\mu$F

> la  fréquence de coupure est d'environ 800Hz

### Circuit de gain par transitor pour le courant de la DEL

[photo]

Mesures de $I_c$:

- Range ampèremètre 200mA

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



Mesures de $I_b$:

- Range ampèremètre 2000 $\mu$

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



- Valeur moyenne du gain $h_{FE}$:



## Deuxième séance

- Interchange Ox3 et Ox2 afin de tester la lumière infrarouge. 



Mesures de $I_c$:

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



Mesures de $I_b$:

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



### Montage d'oxymétrie complet

- 8.3 V au lieu de 9V sur chaque graphique



### Calibration et calcul du SpO2

Pouls déjà bien calibrer avec 60 sur l'oxymètre portable et le nôtre. 

SpO2 est initialement autour de 91% au lieu de 98%

Facteur de calibration à 1.1 pour SpO2

Prise de données sauvegardé.





### Branchement du circuit d'alimentation

Mesure des courants