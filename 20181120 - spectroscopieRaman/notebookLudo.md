

| **Ludovick Bégin - 111 159 148** | Date: 20 novembre 2018 |
| -------------------------------- | ---------------------: |
|                                  |                        |

# Spectroscopie Raman

### But

Analyser des spectres Raman et appliquer des techniques de moyennage pour diminuer le bruit et contourner les limites de saturation d'un capteur CCD. 


### Préparation

**_1. Identifier les lignes du Mercure dans l'annexe II que vous devriez voir dans le spectromètre lors de l'étalonnage au laboratoire._**

Les pics sont à 614.95, 690, 708 et 709 nm, et le premier est le plus intense. 

**_2. Profondeur des puits du capteur._**

[Data sheet de la caméra pixis 100b](https://www.princetoninstruments.com/userfiles/files/assetLibrary/Datasheets/Princeton_Instruments_PIXIS_100_rev_5_1_10_22_14.pdf)

Il existe 2 différents modes :

*High sensitivity* : 300 ke- (typical), 250 ke- (min)
*High capacity* : 1 Me- (typical), 750 ke- (min)

Le nombre de photons par incrément sur les pixels 16 bits dépend du mode d'opération. En considérant une efficacité quantique de 95% on obtient les valeurs suivantes. 

*High sensitivity* : $$\frac{(0.95)300\text{ke-}}{65535}\approx 4.35 $$ photons par incrément
*High capacity* : $$\frac{(0.95)1 \text{Me-}}{65535}\approx 14.5 $$ photons par incrément

***3. Graphique du bruit de photon en fonction du nombre de photons mesurés.***

Ayant des incréments de 1 bit, l'écart-type sur la mesure est de un demi bit. Cette erreur est constante. On peut alors grapher l'erreur relative (%) en fonction du nombre de photons mesurés. Puisque l'erreur en photons dépend du mode utilisé, on va plutôt exprimer le tout en fonction du nombre de bit compté. En s'attend alors à une erreur relative de 50% pour un compte de 1 bit et que cette valeur décroisse en fonction de $\sqrt{N}$. 

![Graphique du bruit de photon en fonction du nombre de photons mesurés](bruitPhotons.png)

***4. Conversion de la fréquence de vibration en nombre d'onde .***

$$w = \left(  \frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)$$

$$w_{632.8\rightarrow700 (nm)} = \left(  \frac{1}{632.8} - \frac{1}{700}\right)  =151.7 \text{cm}^{-1}$$

***5. Graphique lin-log du bruit en fonction du temps d'intégration.***





***6. Spectre d'émission et d'absorption de la chlorophyle***

![](absoptionChlorophyle.PNG)

![](émissionChlorophyle.PNG)

***7. Taux de gras saturé/insaturé dans l'huile d'olive***

Selon [wiki](https://en.wikipedia.org/wiki/Olive_oil), 

saturé $$ \rightarrow $$ 15% 

insaturé $$\rightarrow$$ 85% 



## Montage

![Montage de spectroscopie Raman](montageRaman.png)

Introduction sur le montage: illumination, fentes, filtre onde plane, réseau holographique.

Introduction sur le bruit de photons, loi de poisson et tout...



## Manipulations

- Logiciel d'acquisition : winspec32. Nous avons fixé le rate a 2MHz, le readout a low noise et le gain a 1 pour toute lexpérience

### Caractérisation de la CCD

#### Caractérisation du bruit de lecture

>  Le binning somme sur les pixels, le max sur le graphique peut alors se rendre à 100x 65 535

- Mesures enregistrées dans un fichier. Sans illumination, soit seulement bruit de lecture

| Temps d'intégration (ms) | Nom du fichier          |
| ------------------------ | ----------------------- |
| 100                      | bruit_lecture_100ms.txt |
| 50                       | bruit_lecture_50ms.txt  |
| 25                       | bruit_lecture_25ms.txt  |
| 10                       | bruit_lecture_10ms.txt  |
| 5                        | bruit_lecture_5ms.txt   |
| 1                        | bruit_lecture_1ms.txt   |
| 0.1                      | bruit_lecture_100um.txt |
| 0.01                     | bruit_lecture_10um.txt  |
| 0.001                    | bruit_lecture_1um.txt   |

**Bruit moyen: ** 61 570 / 100px

#### Caractérisation du bruit thermique

- 

| Temps d'intégration (s) | Nom du fichier           |
| ----------------------- | ------------------------ |
| 1                       | bruit_thermique_1s.txt   |
| 5                       | bruit_thermique_5s.txt   |
| 10                      | bruit_thermique_10s.txt  |
| 25                      | bruit_thermique_25s.txt  |
| 50                      | bruit_thermique_50s.txt  |
| 100                     | bruit_thermique_100s.txt |

**Graphique du signal en fonction du temps d'intégration**





#### Caractérisation du bruit de photon

- On installe un papier blanc à l'échantillon avec lumière de la salle ouverte de sorte à rediriger la lumière blanche vers le spectromètre. 

| Temps d'intégration (s) | Nom du fichier         |
| ----------------------- | ---------------------- |
| 0.001                   | bruit_photon_1ms.txt   |
| 0.1                     | bruit_photon_100ms.txt |
| 1                       | bruit_photon_1s.txt    |
| 5                       | bruit_photon_5s.txt    |
| 10                      | bruit_photon_10s.txt   |



#### Étalonnage de la caméra sur l'axe des longueurs d'onde

- Lampe au mercure avec feuille blanche à l'échantillon.
- On observe bel et bien le spectre de la lampe avec ses pics principaux. 
- Enregistrement du spectre pour un temps d'intégration de 10s sur le fichier *spectre_mercure.txt*. 
- 

#### Alignement du spectromètre par fluorescence

- On observe l'image du spectromètre avec de l'huile d'olive à l'échantillon. 
- On aligne le tout en redirigant le faisceau incident par le miroir. 

#### Prise de spectres Raman pour solutions organiques

- Pour chaque échantillon, on enregistre son spectre pour un temps d'intégration de 100s. 
- Software binning

| Solution      | Nom du fichier  |
| ------------- | --------------- |
| Sucrose       | sucrose.txt     |
| Glycérol      | glycerol.txt    |
| Isopropanol   | isopropanol.txt |
| Méthanol      | methanol.txt    |
| Éthanol       | ethanol.txt     |
| Canola        | canola.txt      |
| Arachide      | arachide.txt    |
| Tournesol     | tournesol.txt   |
| Maïs          | mais.txt        |
| Huile d'olive | olive.txt       |





**PHOTOS !!**



**Trouver un moyen de séparer le signal de la fluorescence du signal Raman.**

