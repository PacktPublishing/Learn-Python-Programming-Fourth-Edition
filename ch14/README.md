# CH14 - Readme

This chapter is about APIs. You will find two main folders:

1. `api_code` contains the FastAPI project about Railways
2. `samples`. This folder contains the examples that went in the chapter, so you can ignore it.

## Setup

Make sure you make a copy of the `.env.example` file, called `.env` in the
same folder.

Install requirements with pip from their folder:

    $ pip install -r requirements.txt

If you want to create your own dummy data, please also install the dev requirements:

    $ pip install -r dev.txt

To generate a new database with random data, activate the virtual environment and then:

    $ cd api_code
    $ python dummy_data.py

This will generate a new `train.db` file for you.

## Running the API

Open a terminal window, change into the `api_code` folder and type this command:

    $ uvicorn main:app --reload

The `--reload` flag makes sure uvicorn is reloaded if you make changes to the
source while the app is running.

### Documentation

To see the documentation and try out the endpoints, run the app and go to:

http://localhost:8000/docs

