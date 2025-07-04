import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_6300677.csv", skiprows=4)

# Check data structure
print(df.head())

# Select top 10 countries by population (for 2022)
top_countries = df[['Country Name', '2022']].sort_values(by='2022', ascending=False).head(10)

# Plotting
plt.figure(figsize=(12,6))
plt.bar(top_countries['Country Name'], top_countries['2022'])
plt.title('Top 10 Countries by Population (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
