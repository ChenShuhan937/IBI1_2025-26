# Practical 10: Working with Global Health Data
# Import required libraries 
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# Section 3: Importing a dataset
# --------------------------
# Change working directory 
os.chdir("C:\\Users\\11\\Downloads")
# Check current directory 
print("Current working directory:", os.getcwd())
# List files in directory
print("Files in directory:", os.listdir())

# Read CSV file into dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# --------------------------
# Section 4: Working with dataframes
# --------------------------
# View first 5 rows
print("\nFirst 5 rows of dataframe:")
print(dalys_data.head(5))

# View dataframe information
print("\nDataframe information:")
dalys_data.info()

# View descriptive statistics
print("\nDescriptive statistics:")
print(dalys_data.describe())

# --------------------------
# Show 3rd & 4th columns (Year, DALYs) for first 10 rows
# --------------------------
first_10 = dalys_data.iloc[0:10, [2, 3]]
print("\nFirst 10 rows: Year and DALYs:")
print(first_10)
# Max DALYs in first 10 years of Afghanistan is 1990
# (from first 10 rows of Afghanistan data)
test = dalys_data.iloc[0:10:2,0:5]
print("\nWhat does this show:")
print(test)
#Results: It shows the even number rows below 10.

# --------------------------
# Boolean index for columns
# --------------------------
my_columns = [True, True, False, True]
bool_index = dalys_data.iloc[0:3, my_columns]
print("\nBoolean index example (first 3 rows):")
print(bool_index)
#Test what happens if my_columns is shorter or longer of the data frame (make adjustment to the code above)
#Python returns errors because the boolean index has wrong length.


# --------------------------
# All data for Zimbabwe using Boolean loc
# --------------------------
zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", :]
print("\nZimbabwe data:")
print(zimbabwe_data)
#First year: 1990, Last year: 2019 for Zimbabwe DALYs data

# --------------------------
# Section 5: Countries with max & min DALYs in 2019
# --------------------------
#Select data for the recent year
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
# Find country with maximum DALYs in 2019
max_country = recent_data.loc[recent_data["DALYs"].idxmax(), "Entity"]
# Find country with minimum DALYs in 2019
min_country = recent_data.loc[recent_data["DALYs"].idxmin(), "Entity"]
print("\n2019 Max DALYs country:", max_country)
print("2019 Min DALYs country:", min_country)
# 2019 max DALYs: [max_country], min DALYs: [min_country]

# --------------------------
#  Plot DALYs over time for one country (max/min country)
# --------------------------
# Extract data for the country with maximum DALYs in 2019
country_plot = dalys_data.loc[dalys_data["Entity"] == max_country, :]
plt.figure(figsize=(10, 5))
plt.plot(country_plot.Year, country_plot.DALYs, 'bo-')
#change the "bo-" into "b+" and "r+" to see what's different
#The color and shape of the dot change
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.title(f"DALYs Over Time in {max_country} (2019 Max DALYs Country)")
plt.xticks(country_plot.Year, rotation=-90)
plt.tight_layout()
plt.show()

# --------------------------
# Section 6: Answer one custom question
# --------------------------
# Question: What was the distribution of DALYs across all countries in 2019?
plt.figure(figsize=(8, 4))
plt.hist(recent_data["DALYs"], bins=20, color="green", edgecolor="black")
plt.xlabel("DALYs Rate")
plt.ylabel("Number of Countries")
plt.title("Distribution of DALYs Across Countries in 2019")
plt.show()