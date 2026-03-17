# Practical 5 - Population Growth Rate Analysis
# Import matplotlib for bar chart
import matplotlib.pyplot as plt
# Define population data 
# Dictionary format: Country: [pop2020, pop2024]
population = {
    "UK": [66.7, 69.2],
    "China": [1426, 1410],
    "Italy": [59.4, 58.9],
    "Brazil": [208.6, 212.0],
    "USA": [331.6, 340.1]
}

#  Calculate percentage population change for each country
# Formula: % change = [(pop2024 - pop2020)/pop2020] × 100 (exact as assignment)
percent_change = {}
for country, pops in population.items():
    pop2020 = pops[0]
    pop2024 = pops[1]
    change = ((pop2024 - pop2020) / pop2020) * 100
    percent_change[country] = round(change, 2)  # Round to 2 decimal places for readability

# Print percentage change for each country
print("Percentage population change (2020-2024) for each country:")
for country, pct in percent_change.items():
    print(f"{country}: {pct}%")
# Sort percentage changes in DESCENDING order (largest increase → largest decrease)
sorted_countries = sorted(percent_change.items(), key=lambda x: x[1], reverse=True)
# Print sorted list
print(f"\nPopulation change sorted (largest increase → largest decrease):")
for country, pct in sorted_countries:
    print(f"{country}: {pct}%")
# Identify largest increase and largest decrease countries
largest_increase_country = sorted_countries[0][0]
largest_increase_pct = sorted_countries[0][1]
largest_decrease_country = sorted_countries[-1][0]
largest_decrease_pct = sorted_countries[-1][1]
# Print required statement 
print(f"\nLargest population increase: {largest_increase_country} ({largest_increase_pct}%)")
print(f"Largest population decrease: {largest_decrease_country} ({largest_decrease_pct}%)")

# Create well-labelled bar chart for population percentage change
# Extract data for bar chart
countries = [c for c, p in sorted_countries]
changes = [p for c, p in sorted_countries]

# Set up bar chart (color code: positive=green, negative=red)
plt.figure(figsize=(10, 6))
colors = ['green' if c > 0 else 'red' for c in changes]
plt.bar(countries, changes, color=colors)

# Add labels, title and grid
plt.xlabel('Country')
plt.ylabel('Percentage Population Change (%)')
plt.title('Population Percentage Change (2020-2024) by Country')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Add horizontal line at 0 for reference (separate increase/decrease)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)

# Save chart 
plt.savefig('population_change_bar_chart.png')
plt.close()
print("\nPopulation change bar chart saved as 'population_change_bar_chart.png'")