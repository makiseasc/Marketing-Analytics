# Business Data Analysis Portfolio
# Marketing campaign analysis

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Generate sample marketing campaign data
np.random.seed(42)  # For reproducibility

# Generate dates for a 3-month campaign
dates = [datetime.now() - timedelta(days=x) for x in range(100)]

# Create campaign data
data = {
    'Date': dates,
    'Channel': np.random.choice(['Email', 'Social', 'PPC', 'Content'], 100),
    'Spend': np.random.normal(1000, 200, 100),  # Marketing spend
    'Impressions': np.random.normal(5000, 1000, 100),
    'Clicks': np.random.normal(500, 100, 100),
    'Conversions': np.random.normal(50, 10, 100)
}

df = pd.DataFrame(data)

# Calculate key metrics
df['Conversion_Rate'] = (df['Conversions'] / df['Clicks']) * 100
df['Cost_Per_Click'] = df['Spend'] / df['Clicks']
df['Cost_Per_Conversion'] = df['Spend'] / df['Conversions']

# Group by channel to analyze performance
channel_performance = df.groupby('Channel').agg({
    'Conversion_Rate': 'mean',
    'Cost_Per_Click': 'mean',
    'Cost_Per_Conversion': 'mean',
    'Spend': 'sum',
    'Conversions': 'sum'
}).round(2)

print("\nChannel Performance Analysis:")
print(channel_performance)

# Create visualization
plt.figure(figsize=(12, 6))
plt.bar(channel_performance.index, channel_performance['Conversion_Rate'])
plt.title('Conversion Rate by Marketing Channel')
plt.xlabel('Channel')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

# Let's dive deeper into Social's performance
social_analysis = df[df['Channel'] == 'Social'].describe()
print("\nDetailed Social channel Metrics:")
print(social_analysis)

# Let's add ROI analysis
df['ROI'] = ((df['Conversions'] * 100) - df['Spend']) / df['Spend'] * 100 # Assuming $100 per conversion

# Compare ROI across channels
roi_by_channel = df.groupby('Channel')['ROI'].mean().round(2)
print("\nROI by Channel:")
print(roi_by_channel)

# Visualize ROI comparison
plt.figure(figsize=(12, 6))
plt.bar(roi_by_channel.index, roi_by_channel)
plt.title('ROI by Marketing Channel')
plt.xlabel('Channel')
plt.ylabel('RI (%)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

# Create a markdown cell or comment secion with our analysis:

