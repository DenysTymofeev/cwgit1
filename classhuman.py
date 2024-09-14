class Human:
    def __init__(self, full_name, birth_date, phone_number, city, country, home_address):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def display_info(self):
        print(f"ПІБ: {self.full_name}")
        print(f"Дата народження: {self.birth_date}")
        print(f"Контактний телефон: {self.phone_number}")
        print(f"Місто: {self.city}")
        print(f"Країна: {self.country}")
        print(f"Домашня адреса: {self.home_address}")

    def update_phone(self, new_phone):
        self.phone_number = new_phone