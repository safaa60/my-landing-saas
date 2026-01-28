# K-Store KR — Justifications techniques (Séance 3)

## 1) Décisions Mobile First

### Priorité au-dessus de la ligne de flottaison
- Titre principal (H1) avec promesse claire.
- Description courte du service.
- CTA principal : « Explorer la boutique → ».
- Preuves rapides (chips : catégories, panier simple, sélection qualitative).

### Éléments masqués / différés sur mobile
- Navigation du header (menu masqué).
- Sections longues affichées plus bas dans la page.
- Aucune image lourde dans le hero.

### Pourquoi
Sur mobile, l’utilisateur scanne très rapidement la page.  
L’objectif est de comprendre en moins de 5 secondes :
- ce que propose K-Store KR,
- pourquoi c’est intéressant,
- et quoi faire ensuite (cliquer sur le CTA).

Masquer la navigation évite la distraction et concentre l’attention sur l’action principale.

---

## 2) Responsive desktop (progressive enhancement)

### Breakpoint choisi
- `@media (min-width: 900px)`

### Enrichissements desktop
- Affichage de la navigation complète.
- Hero en deux colonnes (texte + carte visuelle).
- Sections organisées en grilles (2 ou 3 colonnes).
- CTA toujours visible mais sans casser la hiérarchie mobile.

### Pourquoi
900px correspond au passage tablette → desktop.  
Cela permet :
- d’exploiter l’espace horizontal,
- d’améliorer le confort de lecture,
- sans modifier la structure mobile de base.

Le mobile reste prioritaire et ne régresse pas.

---

## 3) Performance

### LCP identifié
- Élément : `<h1>`
- Section HTML : `.hero`
- Valeur mesurée : **0,17 seconde**

Le contenu principal est textuel, ce qui permet un affichage quasi immédiat.

### Deux actions décidées (maximum)

1. Ne pas utiliser d’images lourdes dans le hero  
   → améliore fortement le LCP et la performance perçue.

2. Utiliser un seul fichier CSS léger, sans framework  
   → réduit les ressources bloquantes au chargement.

### Pourquoi
Ces choix garantissent :
- un temps de chargement très court sur mobile,
- une interface lisible immédiatement,
- une bonne expérience même avec une connexion moyenne.

---

## Conclusion

Les choix Mobile First, le breakpoint unique et la sobriété du CSS permettent :

- une page claire et rapide sur mobile,
- une expérience enrichie sur desktop,
- d’excellents scores Lighthouse,
- et une landing page efficace pour promouvoir le site e-commerce K-Store KR.
