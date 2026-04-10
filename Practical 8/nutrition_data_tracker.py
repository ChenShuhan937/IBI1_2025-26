# Task 2: Nutrition Data Tracker
# Define a class to represent a food item
class food_item:
    # Initialize food item with name, calories, protein, carbs, fat
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name             # Name of the food
        self.calories = calories     # Calorie amount
        self.protein = protein       # Protein in grams
        self.carbs = carbs           # Carbohydrates in grams
        self.fat = fat               # Fat in grams

# Function to calculate total daily nutrition
# Input: list of food_item objects
# Output: print total nutrition and warnings
def calculate_daily_nutrition(food_list):
    # Initialize total values to zero
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    # Loop through each food in the list
    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # Display total nutrition summary
    print("=== 24H Nutrition Summary ===")
    print(f"Total Calories: {total_cal} kcal")
    print(f"Total Protein:  {total_pro} g")
    print(f"Total Carbs:    {total_carbs} g")
    print(f"Total Fat:      {total_fat} g")

    # Check warnings for over limit
    if total_cal > 2500:
        print("⚠️ Warning: Calories exceed 2500 kcal!")
    if total_fat > 90:
        print("⚠️ Warning: Fat exceeds 90 g!")


print("=== Task 2 Example Output ===")
# Create food objects
apple = food_item("Apple", 60, 0.3, 15, 0.5)
banana = food_item("Banana", 90, 1.1, 23, 0.3)
rice = food_item("Rice", 130, 2.7, 28, 0.3)

# List of foods eaten in a day
daily_food = [apple, banana, rice]

# Calculate and show results
calculate_daily_nutrition(daily_food)