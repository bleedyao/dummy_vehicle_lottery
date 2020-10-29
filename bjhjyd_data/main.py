from download_data import *


def start_save_data():
    count, max, valid_code = -1, 0, ''
    while(count < max):
        if max == 0:
            max, valid_code = get_one_page(0)
        else:
            max, valid_code = get_one_page(0, valid_code)
        count += 1

if __name__ == "__main__":
    start_save_data()