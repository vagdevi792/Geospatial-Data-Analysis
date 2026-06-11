import pandas as pd
import matplotlib.pyplot as plt

# Sample location-based sales data
data = {
    'Region': ['North', 'South', 'East', 'West', 'Central'],
    'Sales': [12000, 18000, 25000, 15000, 22000],
    'Latitude': [28.61, 13.08, 22.57, 19.07, 23.25],
    'Longitude': [77.20, 80.27, 88.36, 72.87, 77.41]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Sales Data:")
print(df)

# Find region with highest sales
best_region = df.loc[df['Sales'].idxmax()]

print("\nBest Region for Expansion:")
print(best_region)

# Sales Visualization
plt.figure(figsize=(8, 5))
plt.bar(df['Region'], df['Sales'])
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()
