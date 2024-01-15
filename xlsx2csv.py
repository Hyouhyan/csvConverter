import pandas as pd
# require openpyxl

def xlsx2csv(xlsx_file, csv_file):
    data_xlsx = pd.read_excel(xlsx_file)
    data_xlsx.to_csv(csv_file, encoding='utf-8', index = None, header=True)
