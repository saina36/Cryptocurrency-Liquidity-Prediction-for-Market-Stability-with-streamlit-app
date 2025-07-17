# Cryptocurrency-Liquidity-Prediction-for-Market-Stability-with-streamlit-app


---

## **1. Project Overview**

The project aims to **predict the liquidity ratio of cryptocurrencies** and classify them as **Low, Medium, or High liquidity**, assisting traders and market analysts in understanding **market stability**.

✅ **Key Objectives:**

* Predict **liquidity ratio** using market indicators.
* Classify market stability (**Low/Medium/High liquidity**).
* Provide an **interactive real-time prediction app** using **Streamlit**.

---

## **2. Dataset Overview**

| Feature              | Description                                                   |
| -------------------- | ------------------------------------------------------------- |
| **price**            | Current market price of the cryptocurrency (USD).             |
| **1h, 24h, 7d**      | Percentage change in price over 1 hour, 24 hours, and 7 days. |
| **24h\_volume**      | Total traded volume in 24 hours (USD).                        |
| **mkt\_cap**         | Market capitalization (USD).                                  |
| **liquidity\_ratio** | Target variable, representing market liquidity.               |
| **date**             | Transaction date (removed after analysis).                    |

✅ **Final Feature Set for Prediction**:
`volume_to_market_cap, 1h, 24h, 7d`

---

## **3. Exploratory Data Analysis (EDA)**

### **3.1 Data Cleaning**

* **Null values**: Only 7–8 rows had nulls → dropped.
* **Date features** (`year, month, day, weekday`): Dropped (constant values → no predictive power).

### **3.2 Outlier Handling**

* Applied **3×IQR** → reduced extreme fluctuations while preserving important market volatility.

### **3.3 Distribution Analysis**

| Feature                     | Observation                                       |
| --------------------------- | ------------------------------------------------- |
| **1h, 24h, 7d**             | Mostly normal; slight left skew in `1h`.          |
| **volume\_to\_market\_cap** | Highly right-skewed → log-transformation applied. |

### **3.4 Correlation Insights**

* `volume_to_market_cap` shows **highest correlation with liquidity (0.71)**.
* `price_to_liquidity` had low predictive power → removed.

### **3.5 VIF (Multicollinearity)**

* Dropped `24h_volume_log` & `mkt_cap_log` due to **high VIF (>70)**.

---

## **4. High-Level Design (HLD)**

### **4.1 End-to-End Flow**

```
Raw Data → Preprocessing → EDA → Feature Engineering → 
Feature Selection → Model Training & Evaluation → 
Model Saving → Deployment
```

### **4.2 Modules**

1. **Data Preprocessing Module** – Cleans nulls, handles outliers, log-transforms skewed features.
2. **Feature Engineering Module** – Derives `volume_to_market_cap`, `price_to_liquidity`.
3. **Modeling Module** – Trains multiple regressors, evaluates with R², MAE, RMSE.
4. **Deployment Module** – Real-time prediction with Streamlit.

---

## **5. Low-Level Design (LLD)**

### **5.1 Important Functions**

| Function                  | Purpose                                               |
| ------------------------- | ----------------------------------------------------- |
| **drop\_outliers\_iqr()** | Removes rows outside 3×IQR.                           |
| **classify\_liquidity()** | Maps predicted ratio → Low/Medium/High.               |
| **train\_models()**       | Trains multiple models & compares metrics.            |
| **save\_model()**         | Saves model, scaler, and feature list using `joblib`. |

### **5.2 Feature Engineering Formulae**

```
volume_to_market_cap = 24h_volume / mkt_cap
price_to_liquidity = price / liquidity_ratio  (removed later due to low correlation)
```

---

## **6. Model Evaluation**

### **6.1 Performance Metrics**

| Model                   | R² Score  | MAE       | RMSE      |
| ----------------------- | --------- | --------- | --------- |
| Linear Regression       | 0.509     | 0.029     | 0.040     |
| Ridge Regression        | 0.509     | 0.029     | 0.040     |
| Lasso Regression        | 0.468     | 0.030     | 0.042     |
| ElasticNet              | 0.496     | 0.029     | 0.041     |
| **KNN Regressor**       | **0.824** | **0.014** | **0.024** |
| ✅ **Gradient Boosting** | **0.959** | **0.007** | **0.011** |

### **6.2 Overfitting Check**

* **Train R²**: 0.9878
* **Test R²**: 0.9591 → **no significant overfitting**.

### **6.3 Evaluation Plot**

* **Scatter Plot (Predicted vs Actual)** shows points closely aligned to the diagonal → strong prediction reliability.

---

## **7. Deployment Pipeline**

### **7.1 Streamlit App Workflow**

1. **User Input** → `1h, 24h, 7d, volume, market_cap`
2. **Feature Engineering** → Calculate `volume_to_market_cap`
3. **Scaling** → Apply pre-fitted `StandardScaler`
4. **Prediction** → Gradient Boosting predicts liquidity ratio
5. **Classification** → Display **Low/Medium/High Liquidity**

### **7.2 App Snapshot (Logic)**

```
Low (<0.05) → Low Liquidity (unstable)
Medium (0.05–0.15) → Moderate stability
High (>0.15) → Highly liquid, stable
```

---

## **8. Key Highlights**

✅ **Accurate & Robust Model (R² \~96%)**
✅ **Real-time Interactive Prediction App**
✅ **Clean, modular pipeline for future updates**
✅ **Explainable feature engineering & proper validation**

---

## **9. Future Enhancements**

* Include **time-series features (lag/rolling)** for trend-based predictions.
* Build **API-based real-time data ingestion** from crypto exchanges.
* Add **Shapley Values (SHAP)** for explainable AI.

---

# ✅ **How to Run**

1. Install dependencies → `pip install -r requirements.txt`
2. Run the app → `streamlit run app.py`
3. Input market details & get instant predictions!

---

