# K-Store KR — Landing page promotionnelle (Mobile First)

Projet réalisé dans le cadre de la **Séance 3 – Projet de synthèse (HTML/CSS, Mobile First, performance, CI/CD, Streamlit)**.

Cette landing page a pour objectif de promouvoir un site e-commerce coréen (snacks, ramen, boissons, K-beauty, lifestyle) et d’inciter les visiteurs à découvrir la boutique en ligne.

---

## 🎯 Objectifs du projet

- Concevoir une landing page **Mobile First** claire et efficace
- Mettre en place un responsive robuste (progressive enhancement)
- Optimiser la performance perçue et mesurée (audit Lighthouse)
- Justifier les choix techniques (UX, responsive, performance)
- Livrer un projet propre via GitHub avec CI/CD et publication Streamlit

---

## 🧱 Technologies utilisées

- HTML5 (structure sémantique)
- CSS3 (sans framework)
- Git & GitHub
- GitHub Actions (CI)
- Streamlit (hébergement de la landing)

---

## 📁 Structure du projet

.
├── index.html
├── style.css
├── justifications.md
├── README.md
├── mini_rapport_audit_lighthouse_scolaire.docx
├── app.py
├── requirements.txt
└── .github/
└── workflows/
└── ci.yml



---

## ▶️ Lancer le projet en local

### 1) Landing page seule

Ouvre simplement le fichier :

index.html

dans le navigateur.
---

### 2) Via Streamlit

Créer un environnement virtuel (optionnel mais recommandé) :


python -m venv .venv
Activer :

Windows :
.venv\Scripts\activate

Mac / Linux :
source .venv/bin/activate

Installer les dépendances :
pip install streamlit

Lancer l’application :
 python -m streamlit run app.py

 lien du déploiement :
 https://kstore-landing.streamlit.app
 

📝 Justifications
Les décisions Mobile First, responsive et performance sont détaillées dans :
justifications.md

👤 Auteur
Projet réalisé par :
[safaa zemmar]