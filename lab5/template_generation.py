import pandas as pd
import numpy as np

# Selecting a random seed
np.random.seed(0)

students = ['Иванов Иван', 'Петров Петр', 'Сидоров Сидор', 'Кузнецова Анна', 'Михайлова Мария',
            'Смирнов Алексей', 'Попов Дмитрий', 'Васильев Василий', 'Новикова Наталья', 'Федоров Федор']
groups = ['Группа 1', 'Группа 2']
assignments = ['БЖД', 'ФИЛОСОФИЯ', 'РУССКИЙ', 'АНГЛИЙСКИЙ', 'ФИЗРА']

data = []
for student in students:
    group = np.random.choice(groups)
    grades = np.random.randint(0, 100, len(assignments))
    data.append([student, group] + list(grades))

columns = ['Student', 'Group'] + assignments
df = pd.DataFrame(data, columns=columns)

csv_file = 'template/test_table.csv'
df.to_csv(csv_file, index=False)

print(f'Test CSV file "{csv_file}" generated successfully.')
