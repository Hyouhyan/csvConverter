from tabula import read_pdf
import csv

df = read_pdf("愛知工業大学 1月出店スケジュール.pdf", pages="all")
export_data = df[0]
print(export_data)

export_data.to_csv("output.csv", index=False)