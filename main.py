# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import import_csv
from graphs import add_csv_content, get_cheapest_path, try_all_LA_Port


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = add_csv_content(f'C:\\Users\\chris\\PycharmProjects\\Logistics\\venv\\data.csv')
 #   get_cheapest_path()
    try_all_LA_Port()
    print_hi('Done')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
