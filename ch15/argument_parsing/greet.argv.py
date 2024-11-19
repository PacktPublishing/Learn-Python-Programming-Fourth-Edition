# argument_parsing/greet.argv.py
import sys


def main():
    args = parse_arguments()
    print(args)

    msg = "{greet} {name}. You are {age} years old.".format(
        **args
    )

    if args["reverse"]:
        msg = msg[::-1]

    print(msg)


def parse_arguments():
    greet = "Hi"
    reverse = False
    positionals = []

    cmdline = sys.argv[1:]

    while cmdline:
        arg = cmdline.pop(0)
        if arg == "-g":
            if not cmdline or cmdline[0].startswith("-"):
                sys.exit("Please provide a greeting")
            greet = cmdline.pop(0)
        elif arg in ("-r", "--reverse"):
            reverse = True
        elif arg.startswith("-"):
            sys.exit(f"Unknown option: {arg}")
        else:
            positionals.append(arg)

    try:
        name, age = positionals
    except ValueError:
        sys.exit("Please provide a name and age")

    try:
        age = int(age)
    except ValueError:
        sys.exit("Age must be an integer")

    return {
        "name": name,
        "age": age,
        "reverse": reverse,
        "greet": greet,
    }


if __name__ == "__main__":
    main()


"""
$ python argument_parsing/greet.argv.py
Please provide a name and age

$ python argument_parsing/greet.argv.py -g -r Heinrich 42
Please provide a greeting

$ python argument_parsing/greet.argv.py 42
Please provide a name and age

$ python argument_parsing/greet.argv.py Heinrich 42
{'name': 'Heinrich', 'age': 42, 'reverse': False, 'greet': 'Hi'}
Hi Heinrich. You are 42 years old.

$ python argument_parsing/greet.argv.py -g Hello Heinrich 42
{'name': 'Heinrich', 'age': 42, 'reverse': False,
→ 'greet': 'Hello'}
Hello Heinrich. You are 42 years old.

$ python argument_parsing/greet.argv.py -g Hey Heinrich -r 42
{'name': 'Heinrich', 'age': 42, 'reverse': True, 'greet': 'Hey'}
.dlo sraey 24 era uoY .hcirnieH yeH

$ python argument_parsing/greet.argv.py Heinrich -r 42
{'name': 'Heinrich', 'age': 42, 'reverse': True, 'greet': 'Hi'}
.dlo sraey 24 era uoY .hcirnieH iH
"""
