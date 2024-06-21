import pandas as pd
import xlsxwriter

# Calculate the grades
def calculate_grade(avg_rating):
    if avg_rating >= 80:
        return 5
    elif avg_rating >= 70:
        return 4
    elif avg_rating >= 50:
        return 3
    elif avg_rating >= 40:
        return 2
    else:
        return 1

data = pd.read_csv('template/test_table.csv' )
data['Average'] = data.iloc[:, 3:].mean(axis=1) # iloc is used to choose what data we look at and .mean() allows us to compute the average (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
# Final grade
data['Grade'] = data['Average'].apply(calculate_grade)

# Creation of xlsx file
workbook = xlsxwriter.Workbook('grades/students_grades.xlsx')

# Gruping by unique
groups = data['Group'].unique()

for group in groups:
    group_data = data[data['Group'] == group]
    worksheet = workbook.add_worksheet(group)
    
    headers = list(group_data.columns)
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
    
    for row_num, row in enumerate(group_data.itertuples(index=False), start=1):
        for col_num, value in enumerate(row):
            worksheet.write(row_num, col_num, value)
    
    # Pie chart render
    grade_counts = group_data['Grade'].value_counts()
    chart1 = workbook.add_chart({'type': 'pie'})
    for i, (grade, count) in enumerate(grade_counts.items()):
        chart1.add_series({
            'name': f'Grade {grade}',
            'categories': [group, 1, 6, len(grade_counts), 6],
            'values': [group, 1, 7, len(grade_counts), 7],
            'points': [{'fill': {'color': 'blue'}}, 
                       {'fill': {'color': 'green'}}, 
                       {'fill': {'color': 'yellow'}}, 
                       {'fill': {'color': 'red'}}]
        })
    
    chart1.set_title({'name': 'Grade Distribution'})
    chart1.set_style(10)
    worksheet.insert_chart('L2', chart1)
    
    # Column chart for average in every subject
    avg_scores = group_data.iloc[:, 3:-2].mean() 
    chart2 = workbook.add_chart({'type': 'column'})
    chart2.add_series({
        'categories': [group, 0, 3, 0, len(avg_scores) + 2],
        'values': [group, 1, 3, 1, len(avg_scores) + 2],
        'fill': {'color': 'blue'}
    })
    
    chart2.set_title({'name': 'Average Scores by Assignment'})
    chart2.set_x_axis({'name': 'Assignment'})
    chart2.set_y_axis({'name': 'Average Score'})
    chart2.set_style(10)
    worksheet.insert_chart('L16', chart2)

workbook.close()
