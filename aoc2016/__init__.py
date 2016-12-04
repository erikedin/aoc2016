import os.path
import importlib

def main(day_name):
    module_name = "aoc2016.{}".format(day_name)
    day = importlib.import_module(module_name)

    input_path = os.path.join("input", day_name, "input.txt")
    with open(input_path, 'r') as fh:
        input_lines = fh.readlines()

    input = day.parse(input_lines)

    if hasattr(day, "step1"):
        solution = day.step1(input)
        print "Step 1:", solution

    if hasattr(day, "step2"):
        solution = day.step2(input)
        print "Step 2:", solution