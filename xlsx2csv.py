import pandas as pd
# require openpyxl
import os

def xlsx2csv(xlsx_file, csv_file):
    # xlsx_fileが指定されていない場合は、処理終了
    if xlsx_file == '':
        print('xlsxファイルを指定してください')
        return

    # ファイル名がxlsxで終わるか確認
    if os.path.splitext(xlsx_file)[1] != '.xlsx':
        print('xlsxファイルを指定してください')
        return
    
    # csv_fileが指定されていない場合は、xlsx_fileと同じ場所にcsvファイルを作成
    if csv_file == '':
        csv_file = os.path.splitext(xlsx_file)[0] + '.csv'
    
    # xlsxファイルを読み込み
    data_xlsx = pd.read_excel(xlsx_file)
    data_xlsx.to_csv(csv_file, encoding='utf-8', index = None, header=True)
