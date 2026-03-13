# 🏭 Manufacturing Yield & Root Cause Analysis Command Center

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-0071C5?style=for-the-badge)

## 📌 Project Overview
In high-volume manufacturing (e.g., semiconductors, PCBs), a 1% drop in yield can cost millions of dollars. This project is an end-to-end Business Intelligence solution designed to track manufacturing yield, identify the root causes of production defects, and simulate the financial impact of process improvements.

Unlike standard visualization projects, this dashboard is built on a custom **simulated dataset (10,000+ rows)** generated via Python, injected with real-world manufacturing anomalies (e.g., thermal correlations, machine-specific shift degradation, and null values) to test robust ETL and DAX methodologies.

---

## 🛠️ Tech Stack & Methodology
* **Data Generation (Python):** Wrote a script using `pandas` and `numpy` to generate 10,000 logs containing timestamps, machine IDs, voltage, temperature, and defect rates based on hidden statistical correlations.
* **Data Modeling (Power Query):** Transformed flat flat files into a relational **Star Schema** with isolated Dimension (`Dim_Machine`) and Fact (`Fact_Manufacturing`) tables, plus a dynamic DAX `Calendar` table.
* **Calculations (DAX):** Engineered explicit measures using `VAR`, `DIVIDE` (for zero-error handling), Time Intelligence (`DATEADD`), and dynamic parameter filtering.

---

## 📊 Dashboard Architecture & Key Insights

### Phase 1: Executive Command Center (Home)
Designed for high-level plant managers to monitor KPIs at a glance.
* **Feature:** Built custom navigation sidebars for an "App-like" UX.
* **Insight:** Applied conditional formatting to instantly flag the "Night Shift" as the primary driver of the 96.78% yield drop.


### Phase 2: Root Cause Deep Dive (Machines)
Designed for Analytics Engineers to trace the exact source of failure.
* **Feature:** Integrated an **AI Decomposition Tree** and a Statistical Scatter Plot.
* **Insight:** Proved a negative correlation between high machine temperatures and yield percentage. Traced 139,313 total defects directly to the Night Shift operating on Machine M-104 and M-102.


### Phase 3: The Simulation Lab
Designed for Financial / Operational decision-making.
* **Feature:** Built a **"What-If" DAX Parameter**.
* **Value Add:** Allows executives to slide a dynamic scale (0-10%) to instantly calculate the projected monetary savings of resolving the thermal defects (calculating at $50/defect).


---

## 💡 Why This Matters
This project demonstrates the ability to move beyond basic reporting and deliver **actionable engineering intelligence**. By combining data generation, relational modeling, AI visuals, and dynamic financial simulations, it proves a readiness to tackle messy, real-world enterprise data.
