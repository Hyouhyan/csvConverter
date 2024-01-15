import sys

from pdf2csv import pdf2csv
from xlsx2csv import xlsx2csv

import os

args = sys.argv

if len(args) == 1:
    print("引数にファイルを指定してください")
    sys.exit()


# pdfファイルのとき
if os.path.splitext(args[1])[1] == ".pdf":
    pdf_path = args[1]
    if len(args) == 3:
        csv_path = args[2]
    else:
        csv_path = ""
    pdf2csv(pdf_path, csv_path)

# xlsxファイルのとき
if os.path.splitext(args[1])[1] == ".xlsx":
    xlsx_path = args[1]
    if len(args) == 3:
        csv_path = args[2]
    else:
        csv_path = ""
    xlsx2csv(xlsx_path, csv_path)
