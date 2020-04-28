import re
from pathlib import Path


animal_words = [
    "legs",
    "ears",
    "cheese",
    "house",
    "tail",
    "genome",
    "breeding",
    "rodent",
    "evolutionary",
    "breeding",
    "rat",
    "pest",
    "phylogenies",
    "sanitation",
]

computer_device_words = [
    "laser",
    "device",
    "computer",
    "ergonomics",
    "hand",
    "screen",
    "grip",
    "button",
    "elbow",
    "practice",
    "sensor",
    "object",
    "wireless",
    "hold",
    "surface",
    "optical",
]


def determine_mouse_type(sentence: str) -> (str, None):
    """
    Given a sentence, determine what kind of mouse we're talking about

    Returns:
        computer-mouse if computer mouse
        animal if animal
        None if not about mouses at all
    """

    # Keep it really simple for first attempt

    # If no mentions of mouses or mice
    if "mouse" not in sentence and "mice" not in sentence:
        return None
    if any([re.search(word, sentence, re.IGNORECASE) for word in computer_device_words]):
        return "computer-mouse"
    if any([re.search(word, sentence, re.IGNORECASE) for word in animal_words]):
        return "animal"

    return None


def do_mouse_determination(input_file_name: Path, output=False):
    outputs = list()
    first = True
    with open(input_file_name, "r") as file:
        for line in file:
            if line != "\n":
                # Bypass first value (bit clunky, but not sure if you can readline an element out if using as iterator)
                if first:
                    first = False
                    continue

                determination = determine_mouse_type(line)
                if determination:
                    if output:
                       outputs.append(determination)
                    else:
                        print(determination)

    if output:
        return outputs

def main():
    # ToDo Argparse the filename
    input_file_name = Path("Data/mouse-vs-mouse/input01.txt")

    do_mouse_determination(input_file_name)


if __name__ == "__main__":
    main()
