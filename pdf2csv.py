from tabula import read_pdf

def pdf2csv(pdf_path, csv_path):
    df = read_pdf(pdf_path, pages="all")
    export_data = df[0]
    export_data.to_csv(csv_path, index=False)