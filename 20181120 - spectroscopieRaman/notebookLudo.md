

| **Ludovick Bégin - 111 159 148** | Date: 20 novembre 2018 |
| -------------------------------- | ---------------------: |
|                                  |                        |

## Spectroscopie Raman - Partie 1

### But

Obtenir et analyser les spectres Raman de différentes solutions organiques afin de déterminer le taux en gras saturés d'huiles et appliquer des techniques de moyennage statistique pour diminuer le bruit et contourner les limites de la saturation d'un capteur CCD. 



### Préparation

**_1. Identifier les lignes du Mercure dans l'annexe II que vous devriez voir dans le spectromètre lors de l'étalonnage au laboratoire._**

Les pics importants du mercure après 632.8nm sont à 671, 690, 708 et 709 nm


**_2. Profondeur des puits du capteur._**

[Data sheet de la caméra pixis 100b](https://www.princetoninstruments.com/userfiles/files/assetLibrary/Datasheets/Princeton_Instruments_PIXIS_100_rev_5_1_10_22_14.pdf)

Il existe 2 différents modes :

*High sensitivity* : 300 ke- (typical), 250 ke- (min)
*High capacity* : 1 Me- (typical), 750 ke- (min)

Le nombre de photons par incrément sur les pixels 16 bits dépend du mode d'opération. En considérant une efficacité quantique de 95% on obtient les valeurs suivantes. 

*High sensitivity* : $$\frac{(0.95)300\text{ke-}}{65535}\approx 4.35 $$ photons par incrément
*High capacity* : $$\frac{(0.95)1 \text{Me-}}{65535}\approx 14.5 $$ photons par incrément

***3. Graphique de l'erreur de lecture en fonction du nombre de photons mesurés.***

Ayant des incréments de 1 bit, l'écart-type sur la mesure est de un demi bit. Cette erreur est constante. On peut alors grapher l'erreur relative (%) en fonction du nombre de photons mesurés. Puisque l'erreur en photons dépend du mode utilisé, on va plutôt exprimer le tout en fonction du nombre de bit compté. En s'attend alors à une erreur relative de 50% pour un compte de 1 bit et que cette valeur décroisse en fonction de $\sqrt{N}$. 

![Graphique du bruit de photon en fonction du nombre de photons mesurés](bruitPhotons.png)


***4. Conversion de la fréquence de vibration en nombre d'onde .***

$$w = \left(  \frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)$$

$$w_{632.8\rightarrow700 (nm)} = \left(  \frac{1}{632.8} - \frac{1}{700}\right)  =151.7 \text{cm}^{-1}$$

***5. Le bruit de photon en fonction du temps d'intégration.***

Le bruit de photon est une variable aléatoire modélisé par le processus de poisson et qui peut alors être exprimé par la loi normale (gaussienne) lorsque l'échantillonage est grand (théorème central limite). En augmentant le temps d'intégration (somme de variables aléatoires), la moyenne du nombre de photons augmente linéairement ($n\mu$), alors que l'écart-type augmente plus lentement par la racine ($\sqrt{n}\sigma$). On peut alors réduire le bruit (l'écart-type sur la moyenne) en intégrant plus longtemps. 


***6. Spectre d'émission et d'absorption de la chlorophyle***

![](absoptionChlorophyle.PNG)

![](émissionChlorophyle.PNG)


***7. Taux de gras saturé/insaturé dans l'huile d'olive***

Selon [wiki](https://en.wikipedia.org/wiki/Olive_oil), 

saturé $$ \rightarrow $$ 15% 

insaturé $$\rightarrow$$ 85% 



### Montage

![Montage de spectroscopie Raman](montageRaman.jpg)

- Le laser illumine l'échantillon sur une ligne horizontale.
- L'illumination sur l'échantillon est imagé, à l'aide d'un relais, sur une fente.

- La fente (de 100$\mu$m) est orienté verticalement afin de faciliter l'alignement (obtention de lumière). Cela bloque toutefois grandement la lumière provenant de l'échantillon (compromis).
- L'image de cette fente est alors agrandi par un autre relais. 
- La lumière passe alors sur un réseau de diffraction holographique. 
- Chaque longueur d'onde est alors diffracté à un angle spécifique. 
- Une lentille est placée devant la caméra afin de traduire chaque angle en une position sur la CCD.
- Cela indique alors que la résolution en longueur d'onde sur la caméra est principalement limité par la largeur de la fente verticale (compromis). 


### Manipulations

- Logiciel d'acquisition : winspec32. 

  > Nous avons fixé la fréquence d'acquisition à 2MHz, le readout à *low noise* et le gain à 1 pour toute l'expérience.


#### Caractérisation de la CCD

##### Caractérisation du bruit de lecture

>  Le binning somme les pixels verticaux, le max sur le graphique peut alors se rendre à 100 x 65 535 pour une acquisition simple (non répétée). Lorsqu'une acquisition répétée est programmée, le logiciel ne moyenne pas les valeurs, il continu à les additionner. La valeur maximale du graphique dépend alors du nombre d'acquisition. 

- Aucune illumination en bloquant l'entrée de la lumière et en fermant les lumières de la salle (=> seulement le bruit de lecture).
- Mesures enregistrées dans les fichiers suivants: 

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

![](readNoisePlot.png)

**Bruit moyen pour 100 pixels: ** 61600 bits $\times$ 4.35  photons / bit = 268.1 kilo-photons

##### Caractérisation du bruit thermique

- Aucune illumination (seulement le bruit de lecture et le bruit thermique).
- Temps d'intégration plus long afin d'observer l'effet du bruit thermique.
- Mesures enregistrées dans les fichiers suivants: 

| Temps d'intégration (s) | Nom du fichier           |
| ----------------------- | ------------------------ |
| 1                       | bruit_thermique_1s.txt   |
| 5                       | bruit_thermique_5s.txt   |
| 10                      | bruit_thermique_10s.txt  |
| 25                      | bruit_thermique_25s.txt  |
| 50                      | bruit_thermique_50s.txt  |
| 100                     | bruit_thermique_100s.txt |

![](thermalNoisePlot.png)

Pour chaque temps d'intégration R (écrit dans la table), on calcule la valeur moyenne du signal et on calcule la pente moyenne (curve-fit de degré 1):

**Bruit thermique moyen par seconde**: **8.97 bits/s = 39 photons/s**

##### Caractérisation du bruit de photon

- On installe un papier blanc à l'échantillon avec lumière de la salle ouverte de sorte à rediriger la lumière blanche vers le spectromètre. 
- Mesures enregistrées dans les fichiers suivants: 

| Temps d'intégration (s) | Nom du fichier         |
| ----------------------- | ---------------------- |
| 0.001                   | bruit_photon_1ms.txt   |
| 0.1                     | bruit_photon_100ms.txt |
| 1                       | bruit_photon_1s.txt    |
| 5                       | bruit_photon_5s.txt    |
| 10                      | bruit_photon_10s.txt   |

![](photonNoise.png)



#### Étalonnage de la caméra sur l'axe des longueurs d'onde

- Lampe au mercure allumée avec une feuille blanche à l'échantillon de sorte à réfléchir (diffus) vers le spectromètre.
- On observe bel et bien le spectre de la lampe avec ses pics principaux. 
- Enregistrement du spectre pour un temps d'intégration de 10s sur le fichier `spectre_mercure.txt`. 
- Pour l'instant nous n'avons pas effectué la conversion de nm à pixel (selon l'alignement de la lampe au mercure)

**ATTN: Il est important d'enregistrer le spectre de la lampe au mercure à chaque début de lab**.

 

#### Alignement du spectromètre par fluorescence

- On observe le spectre sur la CCD avec de l'huile d'olive à l'échantillon. 
- On aligne le tout en redirigant le faisceau incident par le miroir afin de centrer le spectre en hauteur sur la CCD. 

#### Prise des spectres Raman pour les solutions organiques

- Pour chaque échantillon, on enregistre son spectre pour un temps d'intégration de 100s (soit 100 acquisitions programées de 1s chaque afin de ne pas saturer la caméra). 
- Software binning activé (somme des pixels verticaux, soit ceux de même longueur d'onde).

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

 

#### Comment séparer le signal de la fluorescence du signal Raman

- Longueur d'excitation différente ---> pas possible dans le cadre du labo.
- Trouver une différence dans la réponse de ces deux phénomènes par rapport à un certain paramètre (comme faire varier l'intensité de la source laser ?) ---> rien trouvé de concluant.
- Intégrer assez longtemps afin d'obtenir une courbe avec assez peu de bruit pour qu'il soit possible de distinguer les pics de Raman de la courbe de fluorescence (pics 5x plus grand que l'écart-type du bruit ?).



## Spectroscopie Raman - Partie 2

### But

Réduire le bruit sur le signal afin d'obtenir le spectre Raman de l'huile d'olive. 



### Manipulations

- Réalignement du faisceau d'entrée afin de remplir la caméra en son centre. 

- Recalibration à l'aide de la lampe au mercure. Spectre à nouveau sauvegardé sous le fichier `mercury_27nov.txt`. 

- Prise de mesure du spectre de l'huile d'olive sur 10 min (300 acquisitions de 2 secondes)

- Calcul du ratio nécessaire afin de différencier les pics Raman du bruit. 

  > On observe un petit pic raman avec une hauteur environ égale à 2.5 fois celle du bruit. 
  >
  > Il faudrait obtenir un ratio deux fois plus grand. Cela mène alors à 4x plus de données selon la théorie énoncée en préparation. 

- Prise d'une nouvelle mesure du spectre de l'huile d'olive en prenant compte de la diminution sur le bruit avec $\sqrt{N}$ de sorte à obtenir le ratio calculé. 

  > Acquisition sur 40 min (1200 x 2s)

- Spectre enregistré sous le fichier `olive40m.txt`.

  > Chaque acquisition de 2s prend plutôt près de 3 secondes au logiciel. L'acquisition de 40m prend alors plutôt 1h20 à faire, bien qu'il y est seulement l'information de 40m. 

- Il peut être possible de soustraire la fluorescence du signal à l'aide de techniques de curve-fitting ou autres. 