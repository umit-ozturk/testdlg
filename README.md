# DLG - Test

## Installation
Clone the repository and create a virtual environment.

    $ git clone https://github.com/umit-ozturk/testdlg.git
	$ cd testdlg
	$ virtualenv -p python3 env
	$ source env/bin/activate
    $ pip install -r requirements.txt

## Running

Basically to see all data,

    $ python manage.py runserver


Visit http://127.0.0.1:8000/api/v1/total

## Test

    $ pytest
