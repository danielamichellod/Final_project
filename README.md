# ✈️ Flight Delays Analysis – EDA & Dashboard Project

## 1. Project Description

This project analyzes U.S. flight delay patterns using a Kaggle dataset (https://www.kaggle.com/datasets/usdot/flight-delays).
The goal is to assess **operational performance** across three dimensions:
- **Punctuality:** Completed flights and on-time performance.
- **Reliability:** Flight cancellations and diversions.
- **Disruption Impact:** Severity of diversions and delays.

The project includes **data cleaning, transformation, exploratory data analysis (EDA), metric creation, and a dashboard-ready dataset** for further visualization.

---

## 2. Objectives 🎯

- Search, download, and combine multiple flight datasets into a single unified dataset.
- Clean and transform raw data, handle missing values, and remove irrelevant columns.
- Create reusable Python functions for EDA, metrics, and visualization.
- Analyze operational KPIs: cancellations, diversions, delay distributions, and hub-specific delays.
- Provide insights into **internal vs external drivers of delays.**
- Structure the project for reproducibility and future dashboard integration.

---

# 3. Repository Structure 📂

```
Final_project/
│
├── data/ # Processed datasets for analysis
│   ├── joint_dataset_airport_avg_delay_dashboard.csv
│   ├── joint_dataset_airport_severe_delay_dashboard.csv
│   ├── joint_dataset_cleaning.csv
│   ├── joint_dataset_delay_causes_dashboard.csv
│   ├── joint_dataset_delay_distribution_dashboard.csv
│   ├── joint_dataset_operationalperformancemetrics.csv
│   └── joint_dataset.csv
│
├── data_raw/ # Raw unprocessed datasets
│   ├── airlines.csv
│   ├── airports.csv
│   └── flights.csv
│
├── jupyters_notebook/ # Analysis and cleaning notebooks
│   ├── dataset_categoricalcolumns.ipynb
│   ├── dataset_cleaning.ipynb
│   ├── dataset_numericalcolumns.ipynb
│   ├── dataset_operationalperformancemetrics.ipynb
│   ├── dataset_pivottablesdashboard.ipynb
│   ├── flight_analysis_report.ipynb
│   └── preliminary_EDA.ipynb
│
├── SRC/ # Reusable Python scripts
│   ├── sp_cleaning_aviation.py
│   ├── sp_eda.py
│   ├── sp_metrics.py
│   └── sp_visualization.py
│
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── Dashboardscreenshot # screenshot to visualize the dashboard
├── venv/ # Virtual environment
```

GoogleDrive link for the dashboard (https://docs.google.com/spreadsheets/d/1LKkHX3nMVUqv_pZ_OZ6A1HN873N-_t5Ys39yMSoJOu8/edit?gid=0#gid=0)

---

## 4. Execution Steps 🏃‍♂️

1. **Clone the repository**:
```bash
git clone <https://github.com/danielamichellod/Final_project>
cd Final_project

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  

3. Install dependencies:

pip install -r requirements.txt

4. Run Jupyter notebooks in order:

- dataset_cleaning.ipynb → Data cleaning pipeline.
- dataset_categoricalcolumns.ipynb & dataset_numericalcolumns.ipynb → EDA of categorical & numerical variables.
- dataset_operationalperformancemetrics.ipynb → Operational metrics calculations.
- dataset_pivottablesdashboard.ipynb → Pivot tables for dashboard.
- flight_analysis_report.ipynb → Full insights and analysis report.
```
---

## 4. Key Metrics & Results 📊

**Flight Completion & Disruptions:**

| **Metric**                    | **Value**    |
|------------------------------------|---------------------|
| Cancellation Rate                | 1.54% (~1 in 65 flights)         |
| Diversion Rate             |  0.26% (~1 in 385 flights)        |
| Total Disruption Rate    |  1.81% (~1 in 55 flights)       |

**On-Time Performance (Completed Flights Only):**

| **Metric**                    | **Value**    |
|------------------------------------|---------------------|
| On-Time Performance (≤15 min)                | 82.09%        |
| Average Arrival Delay             |  4.41 min       |
| Median Arrival Delay   |  -5 min      |
| Delay Rate (>15 min)   | 17.91%      |
| Severe Delay Rate (>60 min)   |  5.58%      |
| 90th Percentile Delay   |  34 min     |
| 95th Percentile Delay  | 66 m      |

**Insights:**

- Most flights arrive early or slightly late (right-skewed distribution).
- Nearly 1 in 18 flights experiences severe delays (>60 min).
- Median departure delays for diverted flights are small (2 min), suggesting diversions are mostly not caused by late departures.

**Top Delay-Contributing Factors:**

| **Cause**                    | **Proportion**    |
|------------------------------------|---------------------|
| Late Aircraft Delay                | 39.84%       |
| Airline Delay            |  32.2%       |
| Air System Delay   |  22.88%      |
| Weather Delay   | 4.95%      |
| Security Delay   |  0.13%      |

- **72% of delays** come from airline operations and network effects.
- Weather and security delays have minor impact on total delay minutes.

**Hub Analysis Highlights:**

- **High-delay hubs:** Wilmington, Gustavus → smaller airports with operational fragility.
- **Medium-delay hubs:** St. Cloud, Aspen-Pitkin → moderate delays (10-12% severe).
- **Lower-delay hubs:** Trenton Mercer, Eagle County → more stable operations.

---

# 6. Project Development 🛠️

**1. Data acquisition:** Downloaded from Kaggle.
**2. Folder & environment setup:** Virtual environment, clean folder structure.
**3. Data cleaning & transformation:**
- Joined flights, airports, and airlines datasets.
- Checked missing values, removed irrelevant columns, filled gaps.
- Created copies for safe manipulation.
**4. Function creation:** Python scripts in SRC/ for reusable cleaning, EDA, metrics, and visualization.
**5. Metric & KPI computation:** Cancellation rate, diversion rate, on-time performance, delay distributions, hub-level analysis.
**6. Dashboard preparation:** Pivot tables and processed datasets ready for visualization.

---

# 7. Dashboard



---

# 8. Conclusions 🧩

- The **U.S. flight network is highly stable**, with over 82% of flights on time.
- Moderate delays (15-60 min) are common and operationally manageable (~12% of flights).
- Severe delays (>60 min) are rare (~5.6%) but have a disproportionate operational and financial impact.
- Most delays are internally driven by **airline operations and late aircraft rotations**, not external factors like weather.
- Smaller or regional airports are **more sensitive to disruptions**, highlighting operational fragility.

**Overall Insight**: The aviation system is reliable for the majority of passengers but vulnerable to **high-impact tail events**, which require targeted operational management.

---

# 9. Recommendations ✅

- Focus operational improvement efforts on **late aircraft and airline delay mitigation.**
- Monitor and support **smaller/regional airports** to reduce severe delays.
- Use historical delay patterns to optimize **crew scheduling and aircraft rotations.**
- Build dashboard KPIs for **real-time monitoring** of punctuality, reliability, and disruption impact.

---

# 10. Requirements 🐍

- **Python 3.9+**
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, jupyter, etc

---

# 11. Contributions ✨

Contributions are welcome, including:
- Improving code efficiency and reusability.
- Enhancing visualizations or dashboards.
- Suggesting additional metrics or analyses.

---

# 12. Author ✉️

Daniela - [GitHub Profile](https://github.com/danielamichellod)