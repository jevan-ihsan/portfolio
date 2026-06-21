import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set style to match the other charts
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (8, 5)

# Load the dataset
csv_path = "/Users/jevanhava/Documents/CFI /BIDA/12. Python Data Analysis/Learner Files/C3 - Visualizing Data/3 - Chapter Exercise/chapter-exercise-data.csv"
df = pd.read_csv(csv_path)

# Fill na values with zeros
df = df.fillna(0)

# Calculate Amount column just like in the completed notebook
df['Amount'] = df['PricePerItem'] * df['Quantity']

# Ensure directories exist
preview_dir = "/Users/jevanhava/Documents/Project/Portofolio/Preview/assets/charts"
root_dir = "/Users/jevanhava/Documents/Project/Portofolio/assets/charts"
os.makedirs(preview_dir, exist_ok=True)
os.makedirs(root_dir, exist_ok=True)

# 1. Discrete Frequency Histogram of Order Quantities
plt.figure()
sns.histplot(df['Quantity'], kde=False, color='#193f6e')
plt.title('Order Quantities Distribution')
plt.xlabel('Quantity')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(preview_dir, "chart_ex_histogram.png"), dpi=150)
plt.savefig(os.path.join(root_dir, "chart_ex_histogram.png"), dpi=150)
plt.close()

# 2. Grouped Order Counts per Customer
plt.figure()
cust_orders = pd.DataFrame(df.groupby('CustomerID')['OrderID'].count())
orders_by_customers = pd.DataFrame(cust_orders.groupby('OrderID')['OrderID'].count())
sns.barplot(x=orders_by_customers.index, y='OrderID', data=orders_by_customers, color='#b8832e')
plt.title('Grouped Order Counts per Customer')
plt.xlabel('Num of Orders')
plt.ylabel('Num of Customers')
plt.tight_layout()
plt.savefig(os.path.join(preview_dir, "chart_ex_barplot.png"), dpi=150)
plt.savefig(os.path.join(root_dir, "chart_ex_barplot.png"), dpi=150)
plt.close()

# 3. Bivariate Scatter Plot: Quantity vs. Amount
plt.figure()
sns.scatterplot(x='Quantity', y='Amount', data=df, alpha=0.7, color='#193f6e')
plt.title('Bivariate Scatter Plot: Quantity vs. Amount')
plt.xlabel('Quantity')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig(os.path.join(preview_dir, "chart_ex_scatterplot.png"), dpi=150)
plt.savefig(os.path.join(root_dir, "chart_ex_scatterplot.png"), dpi=150)
plt.close()

print("Successfully generated and saved all three authentic exercise charts!")
