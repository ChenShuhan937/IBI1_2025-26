#Practical 5 - Heart Rate Analysis
#Import matplotlib for pie chart
import matplotlib.pyplot as plt
import numpy as np #for mean calculation
#Define the heart rate list
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
#print number of patients and mean heart rate
num_patients = len(heart_rates)
mean_hr = np.mean(heart_rates)
print(f"Number of patients in the dataset: {num_patients}, mean heart rate: {mean_hr:.2f} bpm")
#Categorize heart rates (Low: <60, Normal: 60-120, High: >120)
low = 0
normal = 0
high = 0
#loop through all heart rates to count categories
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else: #hr > 120
        high += 1
#print number of patients in each category
print(f"\nNumber of patients in each heart rate catergory:")
print(f"Low (<60 bpm): {low}")
print(f"normal (60-120 bpm): {normal}")
print(f"High (>120 bpm): {high}")
#Identify and print the largest category
#Create a dictionary to map categories to counts for easy max check
category_counts = {
    "Low": low,
    "Normal": normal,
    "High": high
}
largest_category = max(category_counts, key=category_counts.get)
largest_count = category_counts[largest_category]
print(f"\nThe largest category is'{largest_category}' with {largest_count} patients.")
#Create well-labelled pie chart for category distribution
#Data for pie chart
labels = list(category_counts.keys())
sizes = list(category_counts.values())
colors = ['lightcoral', 'lightgreen', 'lightskyblue']
explode = (0.05, 0.05, 0.05) #Slightly explode all slices for readability
#set up pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=90)
plt.axis('equal') #ensure pie chart is a circle
#Add title
plt.title('Distribution of Heart Rate Categories in Patients')
#Save chart
plt.savefig('heart_rate_pie_chart.png')
plt.close()
print("\nPie chart saved as 'heart_rate_pie_chart.png'")