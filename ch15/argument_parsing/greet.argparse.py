# argument_parsing/greet.argparse.py
import argparse


def main():
    args = parse_arguments()
    print(args)

    msg = "{greet} {name}. You are {age} years old.".format(
        **vars(args)
    )

    if args.reverse:
        msg = msg[::-1]

    print(msg)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Your name")
    parser.add_argument("age", type=int, help="Age")
    parser.add_argument("-r", "--reverse", action="store_true")
    parser.add_argument(
        "-g", default="Hi", help="Custom greeting", dest="greet"
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()


"""
$ python argument_parsing/greet.argparse.py
usage: greet.argparse.py [-h] [-g GREET] [-r] name age
greet.argparse.py: error: the following arguments are required:
→ name, age

$ python argument_parsing/greet.argparse.py -h
usage: greet.argparse.py [-h] [-r] [-g GREET] name age

positional arguments:
  name           Your name
  age            Age

options:
  -h, --help     show this help message and exit
  -r, --reverse
  -g GREET       Custom greeting

$ python argument_parsing/greet.argparse.py -g -r Heinrich 42
usage: greet.argparse.py [-h] [-r] [-g GREET] name age
greet.argparse.py: error: argument -g: expected one argument

$ python argument_parsing/greet.argparse.py 42
usage: greet.argparse.py [-h] [-g GREET] [-r] name age
greet.argparse.py: error: the following arguments are required:
→ age

$ python argument_parsing/greet.argparse.py Heinrich 42
Namespace(name='Heinrich', age=42, reverse=False, greet='Hi')
Hi Heinrich. You are 42 years old.

$ python argument_parsing/greet.argparse.py -g Hello Heinrich 42
Namespace(name='Heinrich', age=42, reverse=False, greet='Hello')
Hello Heinrich. You are 42 years old.

$ python argument_parsing/greet.argparse.py -g Hey Heinrich -r 42
Namespace(name='Heinrich', age=42, reverse=True, greet='Hey')
.dlo sraey 24 era uoY .hcirnieH yeH

$ python argument_parsing/greet.argparse.py Heinrich -r 42
Namespace(name='Heinrich', age=42, reverse=True, greet='Hi')
.dlo sraey 24 era uoY .hcirnieH iH
"""
