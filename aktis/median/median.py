from bisect import bisect_left
from math import floor
from pathlib import Path
from typing import List


def read_file(file_name: str) -> List[float]:
    """
    Read our lists of numbers in (legacy, left in to show thinking pattern)
    """
    file = open(file_name, "r")

    file_array = file.readlines()

    output = list()
    for line in file_array:
        if line != "\n":
            output.append(float(line))

    file.close()

    # The first number is the length of the numbers, so raise an error:
    if output[0] + 1 != len(output):
        raise ValueError("The number of elements read in do not match the number specified in the file.")

    return output[1:]


def median(numbers: List[float]) -> float:
    """
    Calculate the median value from a list of variables
    """
    # Odd case
    if len(numbers) % 2:
        return numbers[floor(len(numbers) / 2)]
    # Even case
    else:
        return (numbers[floor(len(numbers)/2)-1] + numbers[floor(len(numbers)/2)]) / 2.0


def print_running_median(numbers: List[float]):
    """
    For a given set of inputs, print a set of running median data to stdout (legacy, left in to show thinking pattern)
    """
    running_list = list()
    for number in numbers:
        running_list.append(number)
        print(median(running_list))


def do_running_median(input_file_name: Path, output=False):
    """We need to read the file in line be line and do all calculation on the fly, as this is easier"""
    input_values = list()
    values = list()
    outputs = list()
    first = True
    with open(input_file_name, "r") as file:
        for line in file:
            if line != "\n":
                parsed_value = float(line)
                # Maintain a list of read in values
                input_values.append(parsed_value)
                # Bypass first value (bit clunky, but not sure if you can readline an element out if using as iterator)
                if first:
                    first = False
                    continue

                # Try using bisect to speed things up, as previous sorting method too clunky for large arrays.
                insert_position = bisect_left(values, parsed_value)
                values.insert(insert_position, parsed_value)

                if values:
                    median_value = median(values)
                    if output:
                        outputs.append(median_value)
                    else:
                        print(median_value)

    if output:
        return outputs


def main():
    # ToDo Argparse the filename
    input_file_name = Path("Data/running-median/input02.txt")
    #
    # """We need to read the file in line be line and do all calculation on the fly, as this is easier"""
    # input_values = list()
    # values = list()
    # with open(input_file_name, "r") as file:
    #     for line in file:
    #         if line != "\n":
    #             input_values.append(float(line))
    #             values = sorted(input_values[1:])
    #             if values:
    #                 print(median(values))

    do_running_median(input_file_name)


if __name__ == "__main__":
    main()
