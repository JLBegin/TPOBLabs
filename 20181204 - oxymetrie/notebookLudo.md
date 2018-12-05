

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









