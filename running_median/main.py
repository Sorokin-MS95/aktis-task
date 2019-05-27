from utils import parse_args

import math
import re
import sys


def main():
    args = parse_args()

    app = RunningMedianApp(args=args)
    app.run()


class RunningMedianApp:

    def __init__(self, args):
        self._filename = args.input
        self._median_elements = []

    def _read_file(self):
        with open(self._filename, 'r+') as content:
            number_of_elems = content.readline().rstrip('\n')
            # Checking if number is digit. If so, convert it to integer.
            if number_of_elems.isdigit():
                number_of_elems = int(number_of_elems)
                # Use range to make sure we read only that number of lines that is required.
                for line_number in range(number_of_elems):
                    el = content.readline().rstrip('\n')
                    # Matching floats or integer here
                    if re.match("\d*?\.?\d+?", el):
                        self._median_elements.append(float(el))
                    else:
                        print('`{}` is not a valid element in input file.'.format(el))
                        sys.exit(1)

            else:
                print('`{}` is not a valid number of elements in input file.'.format(number_of_elems))
                sys.exit(1)

    def run(self):
        self._read_file()
        self._print_running_median()

    def _print_running_median(self):
        for elem in self._median_elements:
            self._print_median(elem)

    def _print_median(self, elem, median_list=[]):
        median_list.append(elem)
        # Sort list first.
        median_list = sorted(median_list)
        median_list_len = len(median_list)
        if median_list_len % 2 == 0:
            median = (median_list[int(median_list_len / 2 - 1)] + median_list[int(median_list_len / 2)]) / 2
        else:
            median = median_list[math.floor(median_list_len / 2)]
        print("{0:0.1f}".format(median))


if __name__ == "__main__":
    main()
