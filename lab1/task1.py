# Счет на оплату

import random
import docxtpl
import uuid # for random cheque values
from dataclasses import dataclass # for @dataclass decorator

first_names = ["Noah", "Oliver", "Liam", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn", "Ethan", "Mason", "Logan", "Jacob", "Jackson", "Wyatt", "Charlie", "Oliver", "Jack", "Sebastian", "Sofia", "Avery", "Addison", "Ella", "Scarlett", "Grace", "Riley", "Brooklyn", "Chloe", "Zoey"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Anderson", "Taylor", "Thomas", "Wilson", "Moore", "Jackson", "Thompson", "White", "Lewis", "Robinson", "Walker", "Evans", "Carter", "Phillips", "Adams", "Nelson", "Harris", "Clark", "Turner", "Campbell", "Parker", "Martin", "Mitchell", "Bailey", "Gomez", "Perez", "Lopez", "Sanchez", "Scott", "Edwards", "Warren", "Russell", "Bennett"]
address_names = ["ул. Солнечная", "ул. Центральная", "ул. Мира", "ул. Ленина", "ул. Победы", "ул. Гагарина", "ул. Пушкина", "ул. Горького", "ул. Кирова", "ул. Калинина", "ул. Московская", "ул. Ленинградская", "ул. Садовая", "ул. Березовая", "ул. Осенняя", "ул. Вишневая", "ул. Яблочная", "ул. Лесная", "ул. Почтовая", "ул. Школьная", "ул. Больничная", "ул. Заводская", "ул. Привокзальная", "ул. Набережная", "ул. Парковая", "ул. Спортивная", "ул. Молодёжная", "ул. Весенняя", "ул. Лесная", "ул. Луговая", "ул. Цветочная", "ул. Радужная", "ул. Мирная", "ул. Дружбы", "ул. Согласия", "ул. Новая", "ул. Строителей", "ул. Энергетиков", "ул. Нефтяников", "ул. Газовиков", "ул. Химиков", "ул. Металлургов", "ул. Горняков", "ул. Железнодорожная", "ул. Автомобильная", "ул. Авиационная", "ул. Космическая"]

def create_random_name():
    return str.join("ИП " + random.choice(last_names) + " " + random.choice(first_names)) 

def create_random_date(): # lazy date generation
    month = random.randint(1, 12)
    year = random.randint(2000, 2024)

    if month == 2:
        if year / 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month / 2 != 1:
        day = random.randint


@dataclass
class Bill_Info:
    check_number: int = random()
    organization_name: str = create_random_name
    seller_name: str = create_random_name
    address: str = str.join("Улица " + random.choice(address_names) + ", дом " + random.randint(0, 127))
    OGRN: uuid
    day: int = 

    
