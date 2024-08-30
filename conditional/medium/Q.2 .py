# Q.Write a program to calculate BMI (Body Mass Index) and categorize it into underweight, 
# normal, overweight, or obese based on the calculated value.

weight = float(input("please enter your weight (in pounds): "))
height = float(input("please enter your height (in inches): "))



def BMI_Indicator():
    x = weight* 703 / height**2 
    print("your BMI is:", x)
    if x < 18.5:
        return "underweight"
    elif 18.5 <= x < 25:
        return "normal"
    elif 25 <= x < 30:
        return "over weight"
    elif 30 <= x:
        return "obese"
    
print(BMI_Indicator())
