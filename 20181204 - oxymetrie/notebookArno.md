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