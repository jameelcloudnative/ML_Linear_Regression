# 📈 ML_Linear_Regression

Predict the sales for the year **2025** using **Linear Regression**.

---

## 🧪 Case Study

This project is based on sales data from a **feed mill company** collected from **2014 to 2024**. Using this historical monthly sales data, we apply **Linear Regression** to forecast the expected sales for each month in **2025**.

---

## 🗂️ Project Structure

ML_Linear_Regression/
│
├── app.py # Command-line version of the prediction script
├── app.ipynb # Jupyter Notebook version with visualization
├── sales_data_2015_2024.csv # Historical sales dataset
└── README.md # Project instructions


---

## 🛠️ How to Run

Follow the steps below to set up and run the project locally on your terminal:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ML_Linear_Regression.git
cd ML_Linear_Regression

#### 2.Create a Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate     # On Linux/macOS
env\Scripts\activate        # On Windows

#### 3. Install Dependencies
pip install pandas scikit-learn matplotlib

Option 1: Run app.py for Terminal Output

python app.py
This will output the predicted sales for each month of 2025 directly in the terminal.

option 2: Use app.ipynb in Jupyter Notebook
jupyter notebook