import sys

from pdf2csv import pdf2csv
from xlsx2csv import xlsx2csv

import os

args = sys.argv

if len(args) == 1:
    print("引数にファイルを指定してください")
    sys.exit()

if len(args) >= 2:
    input_path = args[1]
    output_path = ""

if len(args) == 3:
    output_path = args[2]

if len(args) > 3:
    print("引数が多すぎます")
    sys.exit()


# pdfファイルのとき
if os.path.splitext(args[1])[1] == ".pdf":
    pdf2csv(input_path, output_path)

# xlsxファイルのとき
if os.path.splitext(args[1])[1] == ".xlsx":
    xlsx2csv(input_path, output_path)
