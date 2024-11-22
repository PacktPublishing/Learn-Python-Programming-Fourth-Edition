# Chapter 15 - Command Line Interfaces

This chapter is about Command Line Interfaces (CLI).

In the folder for this chapter you will find the following:

- `README.md`: This file.
- `argument_parsing/`: Contains some examples to introduce argument parsing in Python.
- `project/`: Contains the railway_cli project.
- `project/railway_cli/`: contains a commandline application to interact with the railway API from Chapter 14.
- `project/.env.example`: An example configuration file for the `railway_cli` application.
- `project/secrets/`: An example secrets directory for the `railway_cli` application.
- `requirements/`: The requirements files for the `railway_cli` application.

## Setup

Run the railway API from Chapter 14.

Make a copy  of the `.env.example` file, called `.env` in the same folder. If necesary, edit the
`railway_api_url` value in your `.env` file to match the actual URL of the railway API.

Create a virtual environment, and install the requirements for running the railway_cli application:

    $ pip install -r requirements/requirements.txt

## Running the CLI

To run the CLI, activate the virtual environment, switch to the `project` directory, and run the `railway_cli` module:

    $ python -m railway_cli -h

This will show you the help message for the CLI, including a list of available commands.

To get help for a specific command, run:

    $ python -m railway_cli <command> -h

For example, to get help for the `get-station` command, run:

    $ python -m railway_cli get-station -h
