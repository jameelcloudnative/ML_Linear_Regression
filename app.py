import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("data/dataset.csv")

# Transpose data to get years as rows and months as columns
df_t = df.set_index("Month").T
df_t.index.name = "Year"
df_t.reset_index(inplace=True)
df_t["Year"] = df_t["Year"].astype(int)

# Prepare input (X) and predictions dictionary
X = df_t["Year"].values.reshape(-1, 1)
month_columns = df_t.columns[1:]  # All months

# Store predictions for each month
predictions_2025 = {}

# Train and predict using linear regression for each month
for month in month_columns:
    y = df_t[month].values
    model = LinearRegression()
    model.fit(X, y)
    y_pred_2025 = model.predict([[2025]])
    predictions_2025[month] = int(y_pred_2025[0])

# Convert predictions to DataFrame
predicted_df = pd.DataFrame(list(predictions_2025.items()), columns=["Month", "Predicted Sales 2025"])

# Define the correct month order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Apply categorical ordering and sort
predicted_df["Month"] = pd.Categorical(predicted_df["Month"], categories=month_order, ordered=True)
predicted_df = predicted_df.sort_values("Month")

# Display predicted values
print(predicted_df)


