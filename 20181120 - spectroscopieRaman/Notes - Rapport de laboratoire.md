

## Notes - Rapport de laboratoire

**Titre**: Détermination du taux de saturation par spectroscopie Raman de solutions organiques fluorescentes.

Mesures ratiométriques pour déterminer taux de saturation par spectroscopie Raman en présence de fluorescence importante. 

**Résumé**:

**Introduction**:

**Cadre théorique**:

- > Solutions saturées (les différents liens moléculaires)

- Spectroscopie Raman (excitation à une longueur d'onde, capte le spectre, analyse le shift en wavenumber) explication du shift en wavenumber (modes vibrationnels des liens moléculaires ? et/ou géométrie moléculaire) **BREF... vribrations, section efficace**

- > Fluorescence des huiles (spectre d'absorption de la fluorescence) / intensité de la fluorescence dépendant de la solution.

- Bruits (émission/absorption d'un photon = variable aléatoire = modèle poisson = loi normale lorsque n-> infty => réduction écart-type par sqrt(N) ). Nombre de photons par bit et résolution?

- **Équation du signal pour un pixel (intensité et bruit)** 

- *Bruit thermique ?* Caméra refroidie (donc négligeable) avec spectre de référence

- Section efficace * concetration chlorophll

- Isoler le spectre Raman (fluo, thermique, read noise). Méthode de soustraction de la fluorescence

**Méthode**:

- Setup Raman (étalonné) (fentes croisées (compromis alignement/qté de lumière), taille de la fente qui va jouer sur la résolution(compromis qté de lumière), filtre 632.8nm funky pour bloquer l'excitation dans un ***4f (collimé) ?,*** réseau de diffraction holographique vers la caméra avec lentille (traduction angle-position), caméra CCD et binning avec temps d'intégration qui ne sature pas, ***LabView ? / numérisation ?*** )
- Recalibration avec solutions organiques transparente (éthanol) pour re étalonner 

- Calculer le facteur d'écart-type nécessaire pour avoir le temps d'intégration minimal pour différencier les pics. # ref équation cadre théorique


**Résultats**:

- Tableau des taux de saturation des différentes huiles. 
- Graph olive ou mais (avec spectre complet et spectre raman seul). Ou comparaison de deux huiles de taux différents sur même graph (où la fluorescence est enlevée). Graph multiple (ex: 8 lignes raman sur un graph)
- Graph olive: réduction du bruit pour N=x et N=10x ?

**Discussion**:

- Réduction du bruit ? Spectre du bruit ? (pour une courte et longue acquisition)
- Comparaison théorique des taux de saturation
- *Y a t'il un sujet intéressant à creuser ?*
- *Comment gérer la fluorescence ? Théo ? Discussion ?* (changer l'illumination, soustraction python, photobleaching fluorescence (section efficace), changer d'huile moins verte)
- *Proposition d'améliorations ?* ( Changer l'illumination)

**Annexe**: 

- Étalonnage ?

- Exemple soustraction de la fluorescence python

