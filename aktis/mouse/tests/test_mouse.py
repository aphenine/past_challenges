from pathlib import Path
from unittest import TestCase

from mouse.mouse import determine_mouse_type, do_mouse_determination


class MouseTest(TestCase):
    def setUp(self):
        pass

    def test_mouse_determination_with_basic_sentence(self):
        reference_string = "The complete mouse reference genome was sequenced in 2002."

        mouse_type = determine_mouse_type(reference_string)

        assert mouse_type == "animal"

    def test_mouse_case_00(self):
        input_file_name = Path("Data/mouse-vs-mouse/input00.txt")
        output_file_name = Path("Data/mouse-vs-mouse/output00.txt")

        calculated_values = do_mouse_determination(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(line.strip())

        assert calculated_values == correct_values

    def test_mouse_case_01(self):
        input_file_name = Path("Data/mouse-vs-mouse/input01.txt")
        output_file_name = Path("Data/mouse-vs-mouse/output01.txt")

        calculated_values = do_mouse_determination(input_file_name, output=True)

        correct_values = list()
        with open(output_file_name) as file:
            for line in file:
                if line != "\n":
                    correct_values.append(line.strip())

        assert calculated_values == correct_values
