from calorie import Calorie
from temperature import Temperature


current_country = input("Enter your current living country: ").lower()
if ' ' in current_country:
    current_country = current_country.replace(' ', '-')
current_city = input("Enter your current living city: ").lower()
if ' ' in current_city:
    current_city = current_city.replace(' ', '-')

current_temp = Temperature(city=current_city, country=current_country)

user_weight = float(input("Enter your weight: "))
user_height = int(input("Enter your height: "))
user_age = int(input("Enter your age:"))


calorie_calculator = Calorie(weight=70, height=175, age=25, temperature=current_temp.get_temperature())
print(calorie_calculator.calculating_calories())