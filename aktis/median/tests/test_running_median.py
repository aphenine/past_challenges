from pathlib import Path
from unittest import TestCase

from median.median import do_running_median


class RunningMedianTest(TestCase):
    """
    Simple test of the functions
    """
    def setUp(self):
        pass

    def test_median_case_00(self):
        input_file_name = Path("Data/running-median/input00.txt")
        output_file_name = Path("Data/running-median/output00.txt")

        calculated_values = do_running_median(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(float(line))

        assert calculated_values == correct_values

    def test_median_case_01(self):
        input_file_name = Path("Data/running-median/input01.txt")
        output_file_name = Path("Data/running-median/output01.txt")

        calculated_values = do_running_median(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(float(line))

        assert calculated_values == correct_values

    def test_median_case_02(self):
        input_file_name = Path("Data/running-median/input02.txt")
        output_file_name = Path("Data/running-median/output02.txt")

        calculated_values = do_running_median(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(float(line))

        assert calculated_values == correct_values

    def test_median_case_04(self):
        input_file_name = Path("Data/running-median/input04.txt")
        output_file_name = Path("Data/running-median/output04.txt")

        calculated_values = do_running_median(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(float(line))

        assert calculated_values == correct_values
