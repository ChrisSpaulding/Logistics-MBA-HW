import csv


def get_csv_content(file_name: str):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        return dict(csv_reader)
