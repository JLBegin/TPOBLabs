

| **Ludovick Bégin - 111 159 148** | Date: 4 décembre2018 |
| -------------------------------- | -------------------: |
|                                  |                      |

## Oxymétrie - Partie 1

### But



### Préparation



### Montage



### Manipulations

##### Générateur de fonctions

- Labview affiche moyenne de 0V sur le channel rouge et 2.5V sur le channel infrarouge.

- Connection des sorties de la carte d'acquisition sur l'oscilloscope.

AO0 : Branche 4 : Channel 1

AO1 : Branche 2 : Channel 2

- On règle les deux channels sur Labview à 3V et on observe leur signal sur l'oscilloscope: 
  - Channel 1
    - C-C (max-min) : 3.20 V
    - Freq: 33.33 Hz +/- 1
  - Channel 2
    - C-C: 3.20 V
    - Freq: 33.33 Hz

- On connecte les sorties de la carte directement à l'oxymètre.
- On voit la lumière rouge en marche, la lumière infrarouge reste toutefois invisible même sur la carte infrarouge. 

##### Circuit de détection

- Boite cap-range**

- Ampli non fonctionnel -> changé -> ca marche !
- Condensateur 0.2 uF

- Fréquence de coupure : 800 Hz
- 

##### Circuit amplifiant le courant pour la DEL

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



##### Montage d'oxymétrie complet

- 8.3 V au lieu de 9V sur chaque graphique



##### Calibration et calcul du SpO2

Pouls déjà bien calibrer avec 60 sur l'oxymètre portable et le nôtre. 

SpO2 est initialement autour de 91% au lieu de 98%

Facteur de calibration à 1.1 pour SpO2

Prise de données sauvegardé.



