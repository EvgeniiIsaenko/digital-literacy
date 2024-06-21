# Лаба №4: Конвертер
import argparse
import csv
import xlsxwriter

def csv_to_xlsx(input_file, output_file, delimiter):
    # Create the xlsx file itself
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()
    print(f"Created file {output_file}..")

    # Rewriting all cells into new file
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        for row_idx, row in enumerate(csvreader):
            for col_idx, cell in enumerate(row):
                worksheet.write(row_idx, col_idx, cell)
    
    print("Filled all of the cells..")
    workbook.close()

# Console parser
parser = argparse.ArgumentParser(description='Конвертация CSV в XLSX.')
parser.add_argument('input_file', type=str, help='Имя входного CSV файла')
parser.add_argument('output_file', type=str, help='Имя выходного XLSX файла')
parser.add_argument('-d', '--delimiter', type=str, default=';', help='Разделитель в CSV файле (по умолчанию ;)')

# Container for all arguments from the cmd
args = parser.parse_args()

print(f"Converting {args.input_file} into {args.output_file}..")

csv_to_xlsx(args.input_file, args.output_file, args.delimiter)
print("Done!")
