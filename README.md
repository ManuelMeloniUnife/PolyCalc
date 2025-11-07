# PolyCalc 🧮

Un'applicazione desktop per il calcolo e l'analisi di polinomi. Questo progetto è sviluppato come parte del corso di Ingegneria del Software Avanzata (A.A. 2023/2024) dell'Università di Ferrara.

L'obiettivo primario del progetto non è la complessità algoritmica, ma l'applicazione rigorosa delle moderne pratiche di ingegneria del software, tra cui:

* Architettura software disaccoppiata (Logica vs. Interfaccia)
* Test-Driven Development (TDD)
* Misurazione della copertura dei test
* Integrazione e Deployment Continui (CI/CD)
* Containerizzazione

---

## 🎯 Funzionalità Principali

Il "motore" logico di PolyCalc (`polycalc/`) è una libreria Python pura progettata per gestire:

* **Algebra Polinomiale:** Esecuzione delle operazioni algebriche fondamentali tra diverse espressioni polinomiali.
* **Analisi Matematica:** Applicazione dei concetti di analisi di base (calcolo differenziale e integrale) ai polinomi.
* **Utility di Conversione:** Parsing di espressioni da stringhe e formattazione per una visualizzazione leggibile.

---

## 🛠️ Stack Tecnologico

Questo progetto utilizza un set di strumenti moderno per lo sviluppo e il deployment:

* **Linguaggio:** Python (3.10+)
* **Gestione Ambiente:** Conda
* **Framework di Testing:** `pytest` (per i test di Unità e Integrazione)
* **Misurazione Copertura:** `pytest-cov`
* **Automazione CI/CD:** GitHub Actions
* **Containerizzazione:** Docker

---

## 🗺️ Roadmap e Sviluppi Futuri

Questo progetto segue un'architettura che separa nettamente la logica di calcolo (il "Motore") dall'interfaccia utente (la "GUI").

* **Fase 1 (In Corso):** Sviluppo e test rigorosi (TDD) del "Motore" logico.
* **Fase 2:** Implementazione di un'interfaccia grafica (GUI) desktop (utilizzando `tkinter`) che consumerà la libreria del "Motore".
* **Fase 3:** Integrazione del deployment della GUI containerizzata all'interno della pipeline CI/CD.

---