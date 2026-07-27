import csv
import os


folder = os.path.join(os.path.dirname(__file__), "work_with_csv")

file1 = os.path.join(folder, "random-michaels.csv")
file2 = os.path.join(folder, "random.csv")
result_file = os.path.join(folder, "result_Shanava.csv")


all_rows = []

for file in [file1, file2]:
    with open(file, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row not in all_rows:
                all_rows.append(row)


with open(result_file, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_rows)