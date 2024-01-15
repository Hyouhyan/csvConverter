from tabula import read_pdf
import os

def pdf2csv(pdf_path, csv_path):
    # pdf_pathが指定されていない場合は、処理終了
    if pdf_path == '':
        print('pdfファイルを指定してください')
        return
    
    # ファイル名がpdfで終わるか確認
    if os.path.splitext(pdf_path)[1] != '.pdf':
        print('pdfファイルを指定してください')
        return
    
    # csv_pathが指定されていない場合は、pdf_pathと同じ場所にcsvファイルを作成
    if csv_path == '':
        csv_path = os.path.splitext(pdf_path)[0] + '.csv'

    # pdfファイルを読み込み
    df = read_pdf(pdf_path, pages="all")
    export_data = df[0]
    export_data.to_csv(csv_path, index=False)