# Railway CLI

A railway CLI application to demonstrate packaging and distribution of a Python project for
Chapter 16 of "Learn Python Programming, 4d Edition", by Fabrizio Romano and Heinrich Kruger. At the
same time, it acts as an example of an application built around the trains API project from Chapter
14 of the same book.

## Usage

The application provides a command-line interface for interacting with the railway API.

To get help on the available commands, run:

    $ railway-cli -h

To get help for a specific command, run:

    $ python -m railway_cli <command> -h

For example, to get help for the `get-station` command, run:

    $ python -m railway_cli get-station -h
