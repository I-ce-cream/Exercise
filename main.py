# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test():
    mydataset = {
        'sites': ["Google", "Runoob", "Wiki"],
        'number': [1, 2, 3],
    }
    myvar = pd.DataFrame(mydataset)
    print(myvar)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






