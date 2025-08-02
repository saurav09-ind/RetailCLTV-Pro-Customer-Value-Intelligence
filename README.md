# RetailCLTV-Pro-Customer-Value-Intelligence


A complete end-to-end data analytics project that delivers intelligent insights into **Customer Lifetime Value (CLTV)** using real retail data. This project leverages **SQL, Python, and Power BI** to analyze customer behavior, predict future value, and visualize actionable segments for strategic marketing and retention.

---

## 📌 Objective

To build a full-cycle analytics and ML-powered CLTV system that:
- Understands customer purchasing patterns
- Segments customers based on value and behavior
- Predicts CLTV using ML models
- Visualizes results through a clean, professional Power BI dashboard

---

## 🧾 Dataset Used

- **Source**: [UCI / Kaggle Online Retail Dataset]
- ~540,000 transactions from a UK-based online retailer
- Features: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`


---

## 🚀 Project Architecture

### 📁 Folder Structure

CLTV-360-Project/
│
├── 📁 data/
│   ├── raw/
│   │   └── online_retail_dataset.csv
│   ├── interim/
│   │   └── transactions_cleaned.csv
│   └── processed/
│       ├── customer_features.csv
│       ├── rfm_segments.csv
│       └── cltv_predictions.csv
│
├── 📁 notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda_visuals.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_cltv_prediction.ipynb
│   └── 05_final_analysis.ipynb
│
├── 📁 scripts/
│   ├── load_to_pgadmin.py
│
├── 📁 sql/
│   ├── create_tables.sql
│   ├── insert_cleaned_data.sql
│   ├── rfm_segmentation_query.sql
│   └── cltv_output_query.sql
│
├── 📁 models/
│   └── xgb_cltv_model.pkl
│
├── 📁 dashboard/
│   ├── powerbi/
│     └── CLTV_Dashboard.pbix
├── README.md
├── .gitignore
└── project_summary.txt


---

## 📊 Phase-wise Breakdown

### 🔹 Phase 1: EDA & Cleaning (SQL + Python)
- Removed nulls, duplicates, negative quantities
- Created `TotalPrice = Quantity * UnitPrice`
- Loaded cleaned data into PostgreSQL for queries

### 🔹 Phase 2: Feature Engineering
Created 9+ CLTV-related features including:
- `Recency`, `Frequency`, `Monetary`
- `AOV`, `ChurnProbability`, `Expected_Lifespan`
- `PurchaseFrequency`, `Profit`, and calculated `CLTV`

### 🔹 Phase 3: Customer Segmentation
- Used **Rule-based segmentation** on CLTV quartiles
- Mapped segment labels:
  - `0 → Churn Risk`
  - `1 → Potential`
  - `2 → Promising`
  - `3 → Champions`

### 🔹 Phase 4: CLTV Prediction (ML Model)
- Used **Random Forest, XGBoost, Linear Regression**
- Trained models on engineered features to predict `CLTV`
- Evaluated using `R²`, `RMSE`, `MAE`

---

## 📈 Power BI Dashboard

### 💡 One-page Interactive Dashboard Includes:
- KPIs: **Total Revenue, Total Customers, Avg CLTV**
- Segment-wise bar & pie charts
- CLTV comparison across customer tiers and countries
- Filters: Country, Segment, CLTV Range

### 🖼️ Preview:

![Dashboard Screenshot](images/sample_dashboard.png)
<img width="1326" height="741" alt="Screenshot 2025-08-02 150847" src="https://github.com/user-attachments/assets/219b638e-8aba-4f86-8d2c-2c0ca67379a2" />


---

## 🛠️ Tech Stack

| Tool        | Use Case                       |
|-------------|--------------------------------|
| **Python**  | Data Cleaning, EDA, Modeling   |
| **SQL**     | Querying & data manipulation   |
| **Power BI**| Visualization & storytelling   |
| **Pandas, Seaborn, XGBoost, Sklearn** | Core libraries for ML & analysis |

---

## 📚 Key Learnings

- CLTV prediction using real business metrics
- Rule-based + predictive segmentation
- Integrating SQL + Python + BI tools in a real project
- Presenting data to non-technical stakeholders with dashboards
📌 Top 5 Key Insights from Customer Data
1.Top 5% Customers Contribute ~40% Revenue
  High-value customers are driving a disproportionate share of total revenue, reinforcing the importance of personalized retention efforts.

2.Churn Risk Segment Accounts for 50% of Customers
  A significant portion of customers fall into the lowest-value segment (Segment 0), indicating an urgent need for re-engagement strategies.

3.Average CLTV per Customer: £220.47
  The average predicted Customer Lifetime Value is £220.47, serving as a benchmark for targeting and ROI calculation.

4.Customer Lifespan Estimates Range: 2 to 9 Months
  Most loyal customers are expected to continue buying for up to 9 months, based on Recency and Purchase Frequency.

5.UK Generates ~85% of Total Revenue
  While international orders exist, the UK market remains the dominant revenue driver — ideal for regional campaign focus.
---

## 🧠 Future Enhancements

- Add retention score & campaign targeting recommendation
- Use BG/NBD & Gamma-Gamma probabilistic models
- Automate ETL using Airflow / Prefect

---

## 🙌 Author

**Saurav Said**  
Final Year B.Tech AI & Data Science  
Aspiring Data Analyst | SQL | Python | Power BI




