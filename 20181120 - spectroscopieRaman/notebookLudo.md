

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



### Manipulations





#### Montage

![Montage de spectroscopie Raman](montageRaman.png)



