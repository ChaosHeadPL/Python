import csv


with open("python\snippets\\test.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(type(line))
