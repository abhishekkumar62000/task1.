# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"Data.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.duplicated().sum())

# Check if there are any missing values in the DataFrame
print(df.isna().sum().any())

# Fill missing values using forward fill method
df = df.ffill()

# Check again if there are any missing values after filling
print(df.isna().sum().any())

# Print unique values in 'Country Name' column
print(df['Country Name'].unique())

# Print unique values in 'Country Code' column
print(df['Country Code'].unique())

# Print unique values in 'Indicator Name' column
print(df['Indicator Name'].unique())

# Print unique values in 'Indicator Code' column
print(df['Indicator Code'].unique())

# Drop unnecessary columns
df.drop(['Indicator Name', 'Indicator Code', 'Country Code'], axis=1, inplace=True)
print(df.columns)

# Plot histograms for each year
cols = ['2001', '2002', '2003', '2004', '2005', '2006', '2007',
        '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
        '2017', '2018', '2019', '2020', '2021', '2022']
for i in cols:
    fig = plt.figure(figsize=(5, 5))
    plt.hist(df[i], color='#1D194D', bins=10)
    plt.xlabel(i)
    plt.show()

# Calculate total values for each year
years = df.columns[1:]
total_values = df[years].sum()

# Plot bar chart for total values per year
plt.figure(figsize=(30, 30))
plt.barh(years, total_values, color='#214D18')
plt.xlabel('Total Values')
plt.ylabel('Year', size=20)
plt.title('Total Values per Year', size=20)
plt.show()

# Display top 10 countries in 2001
country_2001 = df.sort_values(by='2001').head(10)
print(country_2001)

# Transpose DataFrame for plotting
country_by_2001_t = country_2001.set_index('Country Name').T

# Plot bar chart for each country in 2001
for country_name, data_values in country_by_2001_t.iterrows():
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Countries')
    plt.ylabel('Data Values')
    plt.title(f"{country_name}")
    plt.xticks(rotation=90)
    plt.show()

# Display top 10 countries in 2022
country_2022 = df.sort_values(by='2022').head(10)
print(country_2022)

# Transpose DataFrame for plotting
country_by_2022_t = country_2022.set_index('Country Name').T

# Plot bar chart for each country in 2022
for country_name, data_values in country_by_2022_t.iterrows():
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Year')
    plt.ylabel('Data Value')
    plt.title(f"{country_name} - Data Values")
    plt.xticks(rotation=90)
    plt.show()
