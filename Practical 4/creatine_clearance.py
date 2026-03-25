#Practical4 part7:Creatine clearance calculator
#define patient data
age=35
weight=65
gender="male"
cr=80 #serum creatine concentration in μmol/l
#input validation
is_valid=True
#validate age
if age >= 100:
    print("Error:Age is invalid(must be less than 100 years)")
    is_valid=False
#Validate weight
if weight <= 20 or weight >=80:
    print("Error:Weight is invalid(must between 20 and 80kg)")
    is_valid=False
#Validate creatine concentration
if cr<=0 or cr >= 100:
    print("Error: Creatine concentration(Cr) is invalid (must be between 0 and 100μmol/l)")
    is_valid=False
#Validate gender
if gender not in ["male","female"]:
    print("Error:Gender is invalid (must be'male' or 'female')")
    is_valid=False
#Calculate and display result if all inputs are valid
if is_valid:
    crcl_male=(140-age)*weight/(72*cr)
    if gender == "female":
        crcl=crcl_male*0.85
    else:
        crcl=crcl_male
    #print result with 2 decimal places for readability
    print(f"Creatine Clearance (CrCl):{crcl:.2f} ml/min")
