

| **Arnaud Mercier - 111 156 297** | Date: 20 novembre 2018 |
| -------------------------------- | ---------------------: |
|                                  |                        |

# Spectroscopie Raman					semaine 1

------

## Question préparatoires

### Lignes de Mercure qui devront être observées dans le spectromètre durant l'étalonnage 

> Selon l'annexe 2,  le pic avec le plus d'intensité est celui à 614.95 nm . Il serait donc bien de commencer à le repéré et de le placer au début du captur. Par la suite ds pics à 690, 708 et 709 possèdent une intnsité de 250, 250 et 200. 

### Profondeur des puits du capteur CCD

> Lien  vers la ficher technique de la caméra pixis 100b : [dataSheet](https://www.princetoninstruments.com/userfiles/files/assetLibrary/Datasheets/Princeton_Instruments_PIXIS_100_rev_5_1_10_22_14.pdf)
>
> Il existe 2 différents modes :
>
> *High sensitivity* : 300 ke- (typical), 250 ke- (min)
> *High capacity* : 1 Me- (typical), 750 ke- (min)
>
> Le nombre de requis pour agmenter la valeur de un pixel de '1' ( valeur des pixels de 0 à 65535 (16bits)) dépend du mode d'opération. Considérons une efficacité quantique de 95%.
>
> High sensitivity* : $$\frac{(0.95)300\text{ke-}}{65535}\approx 4.35 $$ photon par incrément
> *High capacity* : $$\frac{(0.95)1 \text{Me-}}{65535}\approx 14.5 $$ photon par incrément

### Graphique du bruit de photon en fonction du nombre photons mesuré

> on saucera pas... $$\frac{N}{\sqrt{N}}$$
> Il est aussi importnt de voir qu dans la dataSheet, le fabricant spécifie des valeurs pour le bruit de lecture
>
> @ 100 kHz  $$\rightarrow$$  3 e- rms (typical), 5 e- rms (max)
> @2MHz $$\rightarrow$$ 11 e- rms (typical), 16 e- rms (max)

### Conversion longueur d'onde $\rightarrow$  nombre d'onde

> $$w = \left(  \frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)$$
>
> $$w_{632.8\rightarrow700 (nm)} = \left(  \frac{1}{632.8} - \frac{1}{700}\right)  =151.7 \text{cm}^{-1}$$
>
> [source](https://en.wikipedia.org/wiki/Raman_spectroscopy)

### Graphique du bruit en fonction du temps d'intégration



###Spectre d"émission et d'absoption de la chlorophyle

> tout est bine détaillé sur ce [site](https://omlc.org/spectra/PhotochemCAD/html/123.html).
>
> ![](absoptionChlorophyle.PNG)

> ![](émissionChlorophyle.PNG)