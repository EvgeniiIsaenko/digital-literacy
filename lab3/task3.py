# Лаба №3: Приглашение 2
from docxtpl import DocxTemplate
import random

def generate_random_data():
    first_names = ["Noah", "Oliver", "Liam", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn", "Ethan", "Mason", "Logan", "Jacob", "Jackson", "Wyatt", "Charlie", "Oliver", "Jack", "Sebastian", "Sofia", "Avery", "Addison", "Ella", "Scarlett", "Grace", "Riley", "Brooklyn", "Chloe", "Zoey"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Anderson", "Taylor", "Thomas", "Wilson", "Moore", "Jackson", "Thompson", "White", "Lewis", "Robinson", "Walker", "Evans", "Carter", "Phillips", "Adams", "Nelson", "Harris", "Clark", "Turner", "Campbell", "Parker", "Martin", "Mitchell", "Bailey", "Gomez", "Perez", "Lopez", "Sanchez", "Scott", "Edwards", "Warren", "Russell", "Bennett"]
    address_names = ["ул. Солнечная", "ул. Центральная", "ул. Мира", "ул. Ленина", "ул. Победы", "ул. Гагарина", "ул. Пушкина", "ул. Горького", "ул. Кирова", "ул. Калинина", "ул. Московская", "ул. Ленинградская", "ул. Садовая", "ул. Березовая", "ул. Осенняя", "ул. Вишневая", "ул. Яблочная", "ул. Лесная", "ул. Почтовая", "ул. Школьная", "ул. Больничная", "ул. Заводская", "ул. Привокзальная", "ул. Набережная", "ул. Парковая", "ул. Спортивная", "ул. Молодёжная", "ул. Весенняя", "ул. Лесная", "ул. Луговая", "ул. Цветочная", "ул. Радужная", "ул. Мирная", "ул. Дружбы", "ул. Согласия", "ул. Новая", "ул. Строителей", "ул. Энергетиков", "ул. Нефтяников", "ул. Газовиков", "ул. Химиков", "ул. Металлургов", "ул. Горняков", "ул. Железнодорожная", "ул. Автомобильная", "ул. Авиационная", "ул. Космическая"]

    data_list = []
    for _ in range(15):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = 2024
        full_name = f"{random.choice(last_names)} {random.choice(first_names)}"
        address = random.choice(address_names)
        time = f"{random.randint(9, 21)}:{random.randint(0, 5)}0"

        data_list.append({
            "date": f"{str(day)}.{str(month)}.{str(year)}",
            "full_name": full_name,
            "time": time,
            "address": address,
        })

    return data_list

# Generate random data and select the template
data_list = generate_random_data()
template = DocxTemplate("template/invitation_tpl.docx")

# All of the invitations put into another folder
for idx, data in enumerate(data_list):
    template.render(data)
    template.save(f"invitations/invitation_{idx + 1}.docx")
