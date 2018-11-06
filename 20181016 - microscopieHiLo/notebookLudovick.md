

| Ludovick Bégin - 111 159 148 | Date: 16 octobre 2018 |
| ---------------------------- | --------------------: |
|                              |                       |



# Microscopie et résolution  -  16 octobre 2018

------



## Préparation

![Photo du montage à microscopie](microscopie.jpg)

Les calculs de limite de résolution n'ont pas été fait en préparation. Un plan sur le système HiLo a plutôt été écrit en pensant commencer directement par cette partie. Les calculs de préparation ne sont toutefois pas nécessaire pour l'expérience effectuée cette semaine.

 

## Alignement et mise au point

- L'illumination est mise à intensité moyenne

- On installe un échantillon de bactéries colorés déjà préparé sous lamelle et facile à voir (**Trouver référence**). 

- Le bon objectif d'alignement est choisi, soit l'objectif 10x qui possède ici la plus grande ouverture numérique, soit la plus grande profondeur de champ, ce qui permet d'arriver au focus plus facilement. 

- Le condenseur est avancé à quelques millimètres de l'échantillon en mode champ clair ("O") et le diaphragme d'ouverture est ouvert afin de laisser passer le plus de lumière. 

- La mise au point sur l'échantillon est effectuée.

  > Il est noté que la mise au point se fait généralement très proche de l'objectif et qu'il est du coup plus efficace de commencer le balayage en se rapprochant le plus près possible de l'objectif et descendre lentement jusqu'à la mise au point. 



## Installation de la caméra

- La camera DMK 21AF04 est vissé sur l'oculaire, comme on peut le voir sur la photo du montage plus haut.  
- Le logiciel IC Capture est ouvert. Il reconnait la caméra et on peut y voir l'image en temps réel.
- On garde le même échantillon que plus tôt pour recalibrer le système avec la caméra. 
- On remet l'image au focus pour la caméra (ce qui n'est pas au même endroit que pour la mise au point avec l'oculaire). 



## Observation des échantillons vivants

- Préparation d'un échantillon de levures et de bactéries. À l'aide d'une micropipette, 15 $\mu$L d'une solution à bactéries est installé sur une lamelle de microscope et 100 $\mu$L d'une solution à levures est installé de la même manière sur une lamelle. 
- L'échantillon de levure est placé sous le microscope avec l'objectif 40x non Ph (sans constraste de phase).
- L'image est mise au focus et enregistrée sur le logiciel -> `levure_40x.jpg`.

![Levures à 40x](levures_40x.jpg)

- L'échantillon est remplacée par celle des bactéries.

  > On observe aucunes bactéries avec les objectifs sans contraste de phase.

- On règle alors l'illumination en contraste de phase Ph3 avec objectif 40x Ph3. 

- L'oculaire sans caméra est remplacé par la lentille de Bertrand et on observe l'anneau du condenseur.

- Cet anneau est aligné au centre à l'aide des vis de déplacement du condenseur. 

- L'image est mise au focus sur la caméra et enregistrée sur le logiciel -> `bacteries_40x.jpg`.

  > Il y a dans l'image beaucoup de saletés provenant des lentilles. 

![Bactéries à 40x](bacteries_40x.jpg)

- On place une goutte d'huile à objectif type A sur l'échantillon afin d'utiliser l'objectif 100x Ph4.

- On image l'échantillon de bactéries avec et sans contraste de phase sous les noms `bacteries_100x_2_Ph4.jpg` et `bacteries_100x_2_O.jpg` respectivement .

  > Bien qu'on observe assez bien les bactéries avec contraste de phase, elles sont pratiquement invisble sans.

  > La distance de travail de l'objectif 100x est **très courte**. 


Par contrainte de temps, et sachant que la deuxième partie de l'expérience ne sera pas faite (afin de travailler sur le montage HiLo), la calibration des dimensions observées est laissée de côté. Le but et les manipulations de cette étape sont toutefois bien comprises. 





# Microscopie HiLo -  23 octobre 2018

------



## Préparation

**But**

Transformer un système de microscopie standard en système HiLo. Cette expérience se concentrera à amener un faisceau laser diffusé et grossi jusqu'à l'entrée de l'objectif de sorte à le remplir et ainsi créer une illumination sur l'échantillon. 



**Schéma du montage à réaliser**

![Schéma du montage à réaliser](dessinMontage.png)



**FAUX** le faisceau sera diffusé à la fin avant d'entrer dans l'objectif. La source est alors considéré collimé avant d'entrer dans le premier relais, et de petit diamètre. Le faisceau en resort grossi d'un facteur d'environ 8x pour finir avec un diamètre d'environ 3 cm. La distance entre le relais et l'objectif n'a pas d'importance, car le faisceau y est collimé. 



**Étapes à réaliser**

- Trouver l'objectif désiré.
- Trouver un diffuseur (feuille de papier) et le fixer sur la plaque vertical à la focal de la premier lentille du 4f. --> **Correction**: Le diffuseur sera placé à la fin du premier relais juste avant d'entrer dans le bloc séparateur afin de perdre moins de lumière. 
- Placer un pin hole  à la sortie du diffuseur pour 'cleaner' le faisceau (colimé) et avoir le bon diamètre (pour remplir le back aperture de l'objectif) --> **Correction**: finalement inutile, particulièrement avec la correction précédente.
- Trouver une combinaison de lentille permettant de focaliser le faisceau un peu avant l'objectif de sorte qu'il diverge à nouveau et remplisse l'objectif
- Monter l'objectif et le cube et vérifier que le faisceau remplit l'objectif
- L'objectif doit être placé à une BFL après le relais 4f --> **Faux !** finalement, le faisceau est initialement collimé et le relais fait alors simplement grossir ce faisceau qui reste collimé. On veut alors juste avoir un beau faisceau qui rempli l'objectif. 
- Placer l'échantillon au point focale de l'objectif ou working distance
- Placez la caméra sur la plaque verticale en haut du cube séparateur
- Placez une lentile convergent entre le cube et la caméra. Ajuster la position de la caméra pour que l'image remplisse le capteur.
- S'assurer que le l'illumination uniforme est **uniforme** . Si ce n'est pas le cas, trouver une façon de l'uniformiser.
- Prendre des images Hi et Lo puis les combiner dans FiJI
- Comparer les images Hi Lo avec un confocale et prouver son bon fonctionnement malgré son faible cout.



## Manipulation

- On réutilise le microscope standard qui possède un objectif 10x et une lentille qui forme un système 4f. On enlève les oculaires du microscope standard et on cherchera alors à diriger notre faisceau à cet endroit. 

- On utilise pour l'instant comme diffuseur un papier pour nettoyer les lentilles entre 2 lames de verre. 

- **Correction**: Finalement, le diffuseur sera placé après le premier relais juste avant le bloc séparateur afin de moins perdre de lumière dans le circuit optique. On a alors un faisceau collimé en entrée qui sera alors grossi par le premier relais en restant collimé. La distance _bfl_ sur le schéma est alors faux. Le microscope possède l'objectif 10x avec une autre lentille qui forme un système 4f. Il s'agit alors d'amener notre tache de sorte à remplir la première lentille de ce 4f.

  > **Attention**: quelques miroirs présente de l'astigmatisme, ou sont simplement courbe. Ils ne peuvent donc pas être utilisés pour rediriger le faisceau. 

- Le premier relais est alors composé d'une lentille de focale 2.54 cm et d'une autre avec 20 cm de focale. Cela permet alors de grossir le faisceau d'un facteur d'environ 8. On obtient un faisceau collimé d'environ 3 cm de diamètre à la sortie de ce relais. 

- On baisse le système 4f en redirigant la sortie du laser plus bas tout en essayant de respecter les limites d'angles sur les miroirs afin de ne pas avoir d'aberration. 
- Un mirroir fait sortir le faisceau vers le microscope. On a ici un beau faisceau rond qui rempli l'objectif du microscope. (**Photo**)
- Un grand pôle sert à amener la plaque de verre au dessus du microscope et un diffuseur est placé juste avant. 
- On obtient de la lumière à l'échantillon dans le microscope.
- Plaque de verre trop près du plan image du microscope, on voit alors quelques poussières et traces dans l'image. 
- Avec diffuseur il est difficile de voir une image au focus. 
- Manque de degré de liberté sur la plaque de verre
- Il faudrait remplacer la plaque de verre idéalement par un cube et le rapprocher du microscope. 

Possibilité de passer une plaque à Daniel en lui indiquant de demander au COPL d'ajouter un coating 50%. Ou trouver un dichroïque. 

Installer la caméra

Ajouter un relais afin d'obtenir une image qui entre mieux dans la caméra. Le faisceau initial est d'environ 3 cm vers la caméra DMK 21AF04 qui semble accepter un diamètre d'environ 0.5 cm.

Petit diffuseur pour créer une illumination speckle et une méthode pour obtenir un illumination uniforme (généralement obtenue en brassant le diffuseur). 



![Nouveau schéma corrigé](schemaHiloCorrigé.png)



## Montage réalisé



![Montage du système HiLo réalisé](montageHilo.png)

