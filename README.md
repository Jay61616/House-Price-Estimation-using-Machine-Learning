# 🏡 House Price Prediction with Random Forest

![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data--Handling-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow?logo=matplotlib)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-lightgrey?logo=jupyter)


This project predicts house prices using a Random Forest regression model and visualizes key insights using Python libraries.

---

## 🎯 Objectives
- Estimate house prices based on building features
- Visualize relationships between features and price
- Evaluate the model using R² and Mean Squared Error

---

## 📊 Dataset
- Source: Kaggle
- Attributes: Elevator, Address, Warehouse, Parking, Rooms, Area, and Price (USD)

---

## 🔍 Analysis & Visuals

### 📊 1. Distribution of Prices (Bar Chart)
- **Why created**: To understand the overall distribution and range of house prices in the dataset.
- **What it shows**: Most house listings fall within a specific price range, with a few high-priced outliers.
- **Insight**: The market appears to be right-skewed, meaning most homes are affordably priced, but there are a few high-end listings pulling the average upward.

![7](https://github.com/user-attachments/assets/7064c5c2-ff47-4d0e-8ebb-4d14e513d0cf)

---

### 📈 2. Actual vs. Predicted Prices (Scatter Plot)
- **Why created**: To evaluate how well the Random Forest model performs on unseen data.
- **What it shows**: Each dot represents a prediction. Dots closer to the diagonal (perfect fit) line indicate better predictions.
- **Insight**: The model has strong predictive power — as shown by most points clustering around the line — indicating low error and high R² (≈ 0.96).
  
![8](https://github.com/user-attachments/assets/6cf9dab2-b3d6-44b8-a00c-cc0f3d42f711)

---

### 🏢 3. Price by Elevator Availability (Box Plot)
- **Why created**: To analyze whether having an elevator significantly impacts house pricing.
- **What it shows**: Two box plots (with/without elevator) comparing their price distributions.
- **Insight**: Houses with elevators tend to have higher median prices and more pricing variability — suggesting elevators are a premium feature.
  
![9](https://github.com/user-attachments/assets/5caf81a8-885e-4d2f-86a5-efa04413f52e)


---

## 🧠 Results

- **R-squared (R²): 0.9596**
  - 📈 This means that **95.96% of the variability in house prices** can be explained by the features in the dataset (area, rooms, elevator, etc.).
  - ✅ A very high R² value like this indicates the model fits the data well and captures most of the pricing patterns.

- **Mean Squared Error (MSE): 2,945,622,608.81**
  - ⚙️ This is the average of the squared differences between the actual and predicted prices.
  - 📏 While it looks large, this number is expected when working with currency values in the **millions** — especially when some houses are priced over 1,000,000.
  - 🧠 Lower MSE = better predictions, and this result shows the model performs reliably with limited error.

---

## 📌 Key Insight

> Properties with elevators and larger area are strongly correlated with higher prices, as revealed by box plots and scatter visualizations.

---

## 🛠 Tools & Libraries
- Jupyter Notebook
- Python (pandas, seaborn, matplotlib, sklearn)
- ipywidgets (interactive UI)
- RandomForestRegressor

---

## 📁 Folder Structure
```
house-price-prediction-rf/
├── data/
│   └── housePrice.csv
├── notebook/
│   └── Project_PriceEstimation.py
├── report/
│   └── Finalreport.md  
├── README.md
```

---

## 📈 Future Work
- Expand dataset with additional features
- Improve R² with feature engineering
- Deploy UI as a web app

---

## 👨‍💻 Author
**Jaya Chandra Kadiveti**  
📧 [Kadivetijayachandra@gmail.com)](mailto:Kadivetijayachandra@gmail.com)

---

> Educational project submitted for MSCS3050 - Spring 2023
