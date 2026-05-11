# infection.py - Practical 4

# 1. Set total number of students 
# 2. Set initial infected students
# 3. Set daily growth rate 
# 4. Set day counter to 0
# 5. Loop: while infected < total students
# 6. Increase day by 1
# 7. Calculate new infections 
# 8. Update total infected
# 9. Print day and number of infected
# 10. After loop, print total days taken

# Initial variables
total_students = 91
infected = 5
growth_rate = 0.4
day = 0

# Print header
print("Day | Infected")

# Loop until all students are infected
while infected < total_students:
    day = day + 1
    new_infections = infected * growth_rate
    infected = infected + new_infections
    # Print daily result
    print(f"{day}   | {infected:.1f}")

# Print final result
print("\nAll students infected after", day, "days")
    

    
