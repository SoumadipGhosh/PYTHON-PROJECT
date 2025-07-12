from PyPDF2 import PdfMerger  # Use PdfMerger, which is better suited for merging

merger = PdfMerger()

pdfs = []
n = int(input("How many PDFs do you want to merge?\n"))

for i in range(n): 
    name = input(f"Enter the file name of PDF {i + 1} (with .pdf extension): ")
    pdfs.append(name)

for pdf in pdfs:
    try:
        merger.append(pdf)
    except FileNotFoundError:
        print(f"File {pdf} not found. Skipping.")
    except Exception as e:
        print(f"Error with file {pdf}: {e}. Skipping.")

output_name = input("Enter name for output file (e.g., merged.pdf): ")
merger.write(output_name)
merger.close()
print(f"Successfully created {output_name}")
