# 🧠 Machine Learning II - Apprentissage par Renforcement

Ce repository contient des ressources et des travaux pratiques sur l'Apprentissage par Renforcement (**Reinforcement Learning - RL**). 🚀

---

## 📌 Devoir : Implémentation d'un Agent RL 🎮

🎯 **Objectif :**  
Créer un agent capable de trouver un **trésor** 🏆 dans une grille tout en évitant les **pièges** 💀.

🔍 **Règles du Jeu :**  
- L’agent commence en haut à gauche de la grille (📍 `(0,0)`).
- Il peut se déplacer en **HAUT ⬆️ | BAS ⬇️ | GAUCHE ⬅️ | DROITE ➡️**.
- Chaque déplacement coûte **-1 point** pour encourager les chemins courts.
- Piège **💀 = -10 points** | Trésor **🏆 = +10 points**.
- L’agent doit **apprendre par lui-même** en jouant plusieurs parties.

---

## 🧪 TP 1 : Introduction au Reinforcement Learning et OpenAI Gym

🔹 **Objectif :** Comprendre OpenAI Gym et l’interaction avec un environnement RL.

🛠 **Exercices :**
1. 🏗 **Exploration d'un Environnement Gym**
2. 🔍 **Manipulation des Observations et Récompenses**
3. 🎮 **Contrôle Manuel de l’Agent**
4. 📊 **Évaluation des Performances d’une Politique Aléatoire**

📜 _(Voir `TP01.pdf` pour les détails)_

---

## 🏎️ TP 2 : Implémentation de l’Algorithme Q-Learning

🎯 **Objectif :** Appliquer l’algorithme **Q-Learning** pour une prise de décision optimale.

🔹 **Tâches :**
- 🧊 **Explorer** l’environnement **FrozenLake-v1** 🏞.
- 📝 **Créer et initialiser une Q-Table**.
- 🔄 **Implémenter l’algorithme Q-Learning**.
- 📊 **Évaluer les performances de l’agent**.

📜 _(Voir `TP02.pdf` pour plus de détails)_

---

## 🚦 TP 3 : Optimisation des Feux de Circulation 🚦

🎯 **Objectif :** Utiliser **Q-Learning** et **SARSA** pour optimiser le trafic.

🔹 **Tâches :**
- 🏙 **Simuler un environnement de gestion du trafic**.
- 📊 **Comparer les résultats de Q-Learning et SARSA**.
- 🚥 **Évaluer la fluidité du trafic après optimisation**.

📜 _(Voir `TP03.pdf` pour plus de détails)_

---

## 🚖 TP 4 : Apprentissage Profond pour les Jeux 🎮

🎯 **Objectif :** Implémenter **Proximal Policy Optimization (PPO)** pour entraîner un agent **Taxi-v3**.

🔹 **Tâches :**
- 🗺 **Créer une table de politiques**.
- 🔄 **Mettre à jour les valeurs des états**.
- 🎯 **Entraîner l’agent pour résoudre Taxi-v3**.

📜 _(Voir `TP04.pdf` pour plus de détails)_

---

## 🛠 Technologies Utilisées

🔹 **Langage Principal :** ![Python](https://img.shields.io/badge/Python-🐍-blue)

🔹 **Frameworks et Librairies :**  
![OpenAI Gym](https://img.shields.io/badge/OpenAI_Gym-🕹️-red)  
![NumPy](https://img.shields.io/badge/NumPy-🔢-blue)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-📊-green)

---

🚀 **Bon apprentissage et exploration du Reinforcement Learning !** 💡
