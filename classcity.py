class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def display_info(self):
        print(f"Назва міста: {self.name}")
        print(f"Регіон: {self.region}")
        print(f"Країна: {self.country}")
        print(f"Кількість жителів: {self.population}")
        print(f"Поштовий індекс: {self.postal_code}")
        print(f"Телефонний код: {self.phone_code}")

    def update_population(self, new_population):
        self.population = new_population