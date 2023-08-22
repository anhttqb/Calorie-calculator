class Calorie:
    """This class is used for receiving user's data and calculating the
    needed calories intake based on that information
    BMR = 10*weight(kg) + 6.25*height(cm) -5*age + 5 - 10*temperature"""
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculating_calories(self):
        calorie_intake = self.weight * 10 + 6.25 * self.height + 5 * self.age - 10 * self.temperature
        return calorie_intake
