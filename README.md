# csvConverter

# main.py
コマンドラインでの実行を想定。  
pdfかxlsxかを自動判別し、適切な関数を実行してくれる。  
例 `$ python main.py "pdf-file.pdf"`  

# pdf2csv.py
## pdf2csv(pdf_path, csv_path)
tabula-pyを使用。  
pdf_pathの指定は必須。  
csv_pathは指定がない場合、pdf同一名称で拡張子のみ変更して出力する。

