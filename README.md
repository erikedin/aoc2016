# Advent of Code, 2016
My solutions for http://adventofcode.com, 2016.

I'm using this as an exercise for learning Behaviour Driven Development (BDD).

## Solving a puzzle
To run a solution for day 1 (for example), ensure the virtual environment is activated, as below, and run

    $ python aoc.py day1

It will print the solution for each implemented step.

## Preparation
This requires Python 2.7, and obviously git.

To prepare, install `virtualenv` via

    $ pip install virtualenv

Clone the repository

    $ git clone https://github.com/erikedin/aoc2016.git

Create a virtual environment, and install the requirements

    $ cd aoc2016
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

## Structure
All files with extension `.features` in the directory `features` are the behaviour specifications for each day and step.

The "step definitions" are stored in `features/steps`, and this contains the code that runs each specification.

The actual solutions are in `aoc2016`. Each day is represented by a module, which contains only a `parse` function which
is provided a list of lines from `input.txt` and parses the input appropriately. The day module also contains one or both
of the functions `step1` and `step2`, which of course runs first and second step of the days puzzle. The actual solutions
are placed in appropriate modules for each day. For instance, the solution for day 4 is primarily in the module `rooms.py`.

## Running executable specifications
To run the executable specifications (run this with the virtual environment activated)

    $ behave

## Input files
The input files are expected to be in `input/day<n>/input.txt`.

## License
This code is licensed by the MIT license, with the exception of any `input.txt` files in `input`. 
The input files are not licensed by me, but are provided by [Advent of Code](http://adventofcode.com).

See `LICENSE` for the MIT license.

