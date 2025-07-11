
# 📈 ML Linear Regression — 2025 Sales Forecast

Forecast monthly sales for the year **2025** using **Linear Regression**, based on historical sales data from **2015–2024**.

---

## 📊 Case Study Overview

This project leverages 10 years of monthly sales data (2015 to 2024) from a feed manufacturing business to train a simple yet effective **Linear Regression** model. The objective is to predict the monthly sales for the year **2025**.

This is a beginner-friendly project designed to demonstrate how linear regression can be used for time-based forecasting.

---

## 🗂 Project Structure

```
ML_Linear_Regression/
│
├── app.py                     # Command-line version for quick predictions
├── app.ipynb                  # Jupyter Notebook with step-by-step workflow and visualizations
├── data/dataset.csv   # Historical monthly sales dataset
└── README.md                  # Project documentation
```

---

## 🛠 Getting Started

Follow the steps below to run this project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jameelcloudnative/ML_Linear_Regression.git
cd ML_Linear_Regression
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

**On macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

**On Windows:**

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install pandas scikit-learn matplotlib
```

---

## 🚀 Running the Project

### ✅ Option 1: Terminal-Based Prediction

Run the command-line script to view predictions directly in your terminal:

```bash
python app.py
```

This will display the predicted monthly sales for 2025.

---

### 📓 Option 2: Jupyter Notebook (Recommended for Visualization)

If you prefer a visual and interactive experience:

```bash
jupyter notebook
```

Then open `app.ipynb` to:

- Load and preprocess data
- Fit a linear regression model
- Visualize historical trends
- Forecast and plot monthly sales for 2025

---

## 📁 Dataset

**File:** `sales_data_2015_2024.csv`

- Format: Monthly sales per row, with each row representing a year
- Columns: Jan, Feb, Mar, ..., Dec
- Data source: Internal records from a company

> Make sure the CSV file is located in the root directory of the project.

---

## 📦 Dependencies

The following Python libraries are required:

- `pandas`
- `scikit-learn`
- `matplotlib`

You can install them using:

```bash
pip install -r requirements.txt
```

> You may manually create the `requirements.txt` by running:  
> `pip freeze > requirements.txt`

---

## 🧑‍💻 Author

**Jameel Ahmed**  
Learning AI/ML  
[LinkedIn Profile](https://www.linkedin.com/in/jameel-ahmed) <!-- Replace with actual profile if available -->

---

## 📬 Feedback & Contributions

Feel free to open an issue or submit a pull request if you have:

- Suggestions to improve the code  
- Ideas for better forecasting methods  
- Corrections or feature additions  

---

## ⭐️ Give a Star

If you found this project helpful, please consider giving it a ⭐️ on GitHub to support the project and help others discover it!


