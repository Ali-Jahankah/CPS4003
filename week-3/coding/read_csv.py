#-------Extract data from CSV file in Python------
import csv
import os
print(os.getcwd())
def read(file_path):
    with open (file_path) as file:
        csv_reader = csv.reader(file)
        headings=next(csv_reader)
        print(f"""
          Headings:
          {headings}
          --- Values below ----
          """)
        for row in csv_reader:
            print(row)
        

def run():
    read('./week-3/coding/sample.csv')


if __name__ == "__main__":
    run()