# Лаба №1: Счет на оплату
from docxtpl import DocxTemplate
import uuid
import random

def generate_random_data():
    first_names = ["Noah", "Oliver", "Liam", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn", "Ethan", "Mason", "Logan", "Jacob", "Jackson", "Wyatt", "Charlie", "Oliver", "Jack", "Sebastian", "Sofia", "Avery", "Addison", "Ella", "Scarlett", "Grace", "Riley", "Brooklyn", "Chloe", "Zoey"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Anderson", "Taylor", "Thomas", "Wilson", "Moore", "Jackson", "Thompson", "White", "Lewis", "Robinson", "Walker", "Evans", "Carter", "Phillips", "Adams", "Nelson", "Harris", "Clark", "Turner", "Campbell", "Parker", "Martin", "Mitchell", "Bailey", "Gomez", "Perez", "Lopez", "Sanchez", "Scott", "Edwards", "Warren", "Russell", "Bennett"]
    address_names = ["ул. Солнечная", "ул. Центральная", "ул. Мира", "ул. Ленина", "ул. Победы", "ул. Гагарина", "ул. Пушкина", "ул. Горького", "ул. Кирова", "ул. Калинина", "ул. Московская", "ул. Ленинградская", "ул. Садовая", "ул. Березовая", "ул. Осенняя", "ул. Вишневая", "ул. Яблочная", "ул. Лесная", "ул. Почтовая", "ул. Школьная", "ул. Больничная", "ул. Заводская", "ул. Привокзальная", "ул. Набережная", "ул. Парковая", "ул. Спортивная", "ул. Молодёжная", "ул. Весенняя", "ул. Лесная", "ул. Луговая", "ул. Цветочная", "ул. Радужная", "ул. Мирная", "ул. Дружбы", "ул. Согласия", "ул. Новая", "ул. Строителей", "ул. Энергетиков", "ул. Нефтяников", "ул. Газовиков", "ул. Химиков", "ул. Металлургов", "ул. Горняков", "ул. Железнодорожная", "ул. Автомобильная", "ул. Авиационная", "ул. Космическая"]
    products = ["диван", "кресло", "стол", "стул", "кровать", "шкаф", "комод", "тумбочка", "книжная полка", "письменный стол"]
    companies = ["DNS", "Добрыня и Аня", "Феникс", "Эльдорадо", "Чебуречная"]

    data_list = []
    check_number = 0

    for _ in range(15):
        check_number += 1
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = 24
        company = random.choice(companies)
        seller = (random.choice(last_names) + random.choice(first_names))
        address = random.choice(address_names)
        ORGN = random.randint(100000, 999999)

        product_list = []
        for _ in range(random.randint(1, 5)):
            product = {
                "title": random.choice(products),
                "code": uuid.uuid4,
                "unit": "pcs",
                "amount": random.randint(1, 10),
                "price": round(random.uniform(10.0, 100.0), 2),
            }
            product["sum"] = round(product["amount"] * product["price"], 2)
            product_list.append(product)

        general_sum = round(sum(p["sum"] for p in product_list), 2)

        data_list.append({
            "check_number": check_number,
            "day": str(day) + ".",
            "month": str(month) + ".",
            "year": year,
            "company": company,
            "seller": seller,
            "address": address,
            "ORGN": ORGN,
            "products": product_list,
            "general_sum": general_sum,
        })

    return data_list

# Generate random data and select the template
data_list = generate_random_data()
template = DocxTemplate("bill.docx")

# All of the bills put into another folder
for idx, data in enumerate(data_list):
    template.render(data)
    template.save(f"bills/bill_{idx + 1}.docx")
