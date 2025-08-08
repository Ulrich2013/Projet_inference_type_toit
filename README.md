# Projet de classification des types de toits et inférence avec le modéle ResNet-50 a partir des images géospatiales 🏠

Ce projet présente un notebook Google Colab utilisant des données géospatiales (shapefiles, images raster et photos) pour inférer automatiquement le type de toit des bâtiments.

# Information sur le modéle ResNet-50
Qu'est-ce que ResNet-50 ? 
ResNet-50 est un modèle de vision par ordinateur basé sur un type de réseau neuronal appelé réseau neuronal convolutif (CNN). Les CNN sont conçus pour aider les ordinateurs à comprendre les informations visuelles en apprenant des modèles dans les images, tels que les bords, les couleurs ou les formes, et en utilisant ces modèles pour reconnaître et classer les objets. 

Introduit en 2015 par des chercheurs de Microsoft Research, ResNet-50 est rapidement devenu l'un des modèles les plus impactants dans le domaine en raison de sa précision et de son efficacité dans les tâches de reconnaissance d'images à grande échelle.

L'une des principales caractéristiques de ResNet-50 est son utilisation des connexions résiduelles, également connues sous le nom de connexions raccourcies. Il s'agit de voies simples qui permettent au modèle de sauter certaines étapes du processus d'apprentissage. En d'autres termes, au lieu d'obliger le modèle à faire passer l'information par chaque couche, ces raccourcis lui permettent de transmettre les détails importants plus directement. L'apprentissage est ainsi plus rapide et plus fiable.

<img width="1364" height="560" alt="image" src="https://github.com/user-attachments/assets/91892673-e862-473f-aed4-7bf82ad0238d" />

Cette conception permet de résoudre un problème courant dans le domaine de l'apprentissage profond, appelé "problème du gradient de fuite". Dans les modèles très profonds, des informations importantes peuvent se perdre au fur et à mesure qu'elles traversent de nombreuses couches, ce qui complique l'apprentissage du modèle. 

# Aperçu du fonctionnement de ResNet-50

ResNet-50 a une structure bien organisée qui permet au modèle d'aller en profondeur sans perdre d'informations importantes. Il suit un modèle simple et reproductible qui lui permet d'être efficace tout en offrant de bonnes performances. 

Voici un aperçu du fonctionnement de l'architecture ResNet-50 :

Base extraction de caractéristiques: Le modèle commence par appliquer une opération mathématique appelée convolution. Cette opération consiste à faire glisser de petits filtres (appelés noyaux) sur l'image pour produire des cartes de caractéristiques - de nouvelles versions de l'image qui mettent en évidence des motifs de base tels que les bords ou les textures. C'est ainsi que le modèle commence à repérer des informations visuelles utiles.
‍
Apprentissage de caractéristiques complexes : Au fur et à mesure que les données se déplacent dans le réseau, la taille des cartes de caractéristiques diminue. Cela est possible grâce à des techniques telles que la mise en commun ou l'utilisation de filtres avec des pas plus grands (appelés strides). Dans le même temps, le réseau crée davantage de cartes de caractéristiques, ce qui lui permet de capturer des motifs de plus en plus complexes, tels que des formes, des parties d'objets ou des textures.
‍
Compression et expansion des données : Chaque étape comprime les données, les traite, puis les développe à nouveau. Cela permet au modèle d'apprendre tout en économisant de la mémoire.
‍
Raccourcis : Il s'agit de chemins simples qui permettent à l'information d'aller plus loin au lieu de passer par toutes les couches. Elles rendent l'apprentissage plus stable et plus efficace.
‍
Faire une prédiction: À la fin du réseau, toutes les informations apprises sont combinées et passent par une fonction softmax. Celle-ci produit une distribution de probabilités sur les classes possibles, indiquant la confiance du modèle dans chaque prédiction - par exemple, 90 % de chats, 9 % de chiens, 1 % de voitures.

Fig. 2. L'architecture ResNet-50.

Les connexions résiduelles permettent d'éviter cela en assurant une circulation claire de l'information du début à la fin. C'est pourquoi le modèle est appelé ResNet-50 : ResNet signifie Residual Network (réseau résiduel), et le chiffre "50" fait référence au nombre de couches utilisées pour traiter une image. 

## 📂 Structure du dépôt

- `notebooks/` : notebook principal du projet
- `data_shapefiles/` : shapefiles utilisés (fichiers .shp, .shx, .dbf, etc.)
- `data_rasters/` : images raster (GeoTIFF, TIFF)
- `data_images/` : images `.zep`, `.png`, `.jpg` utilisées dans les inférences

## 🚀 Lancement rapide

1. Ouvrir le notebook via [Google Colab](https://colab.research.google.com/)
2. Importer les données dans les dossiers respectifs
3. Lancer les cellules pour obtenir les prédictions

## 👤 Auteur

**ULRICH TAKAM**, 2025 – Projet open source éducatif
