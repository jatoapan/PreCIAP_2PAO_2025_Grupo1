# 🚗 Used Car Price Prediction

<p align="center">
  https://img.shields.io/badge/Python-3.10-blue.svg
  https://img.shields.io/badge/Notebook-Google_Colab-orange.svg
  https://img.shields.io/badge/Status-In_Progress-yellow.svg
</p>

---

## 🎯 Project Overview

This academic project aims to predict the price of used cars based on various features such as brand, model, year, mileage, fuel type, seller type, and transmission.

The workflow includes:
1. Exploratory Data Analysis (EDA)
2. Data Cleaning and Preprocessing
3. Feature Encoding
4. Regression Model Training
5. Model Evaluation and Visualization

---

## 🛠️ Core Technologies

* **Python 3.10**: Main programming language
* **Google Colab**: Cloud-based development environment
* **Libraries**:
  * `pandas` & `numpy`: Data manipulation
  * `matplotlib` & `seaborn`: Data visualization
  * `scikit-learn`: Regression modeling and metrics
  * `statsmodels`: Statistical analysis and ANOVA
  * `VIF`: Multicollinearity detection

---

## 📊 Dataset

The dataset is located in the `data/` folder and contains:
* `car_prediction_data.csv`: Includes features like:
  * `Car_Name`
  * `Year`
  * `Selling_Price`
  * `Present_Price`
  * `Kms_Driven`
  * `Fuel_Type`
  * `Seller_Type`
  * `Transmission`
  * `Owner`

---

## 🚀 How to Run

1. Open `notebook.ipynb` in Google Colab.
2. Upload the dataset to the `data/` folder.
3. Run all cells in order to:
   * Load and clean the data
   * Encode categorical variables
   * Train a regression model
   * Evaluate performance using R²
   * Visualize predictions vs actual prices

---

## 📈 Results

* Regression model trained using `LinearRegression` from `scikit-learn`
* Evaluation metrics include:
  * R² score on training and test sets
  * ANOVA summary from `statsmodels`
  * VIF analysis for feature selection
* Visualizations:
  * Boxplots for outlier detection
  * Scatter plots for prediction comparison
  * Correlation heatmap

---

## 📂 Project Structure

├── data/
│   └── car_prediction_data.csv       # Dataset
├── notebook.ipynb                    # Main analysis and modeling notebook
├── README.md                         # Project documentation


---

## 📚 Skills Developed

* Data preprocessing and cleaning
* Regression modeling
* Model evaluation (R², ANOVA, VIF)
* Data visualization and interpretation

---

## 📌 Status

This project is part of an academic assignment and is currently in progress.

