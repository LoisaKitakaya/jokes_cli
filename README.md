# jokes_cli

A jokes CLI application.

> Package used: [py-jokes-py](https://pypi.org/project/py-jokes-py/)

## Usage

Clone this project into your local machine and install the dependencies by running the following commands:

```
# clone the project
git clone https://github.com/LoisaKitakaya/jokes_cli.git

# change directory
cd jokes_cli

# create virtual environment
python -m venv .env

# activate the virtual environment
source .env/bin/activate

# install required dependencies
pip install -r requirements.txt
```

To run the application, use the following commands:

```
# without providing options
python app.py

# show all available options
python app.py --help

# with options
python app.py --category=Any type=twopart --amount=2
```

Alternatively, you can download the bundled version of the application using the link below.

[download jokes cli app](https://drive.google.com/file/d/1zyzQnd3KbvT1mgjAaqWNcmiEf9JY4Arl/view?usp=sharing)

Once you have downloaded the app (.tar.xz file), open the terminal in the location where the app was downloaded, and follow the following steps:

```
# extract the app folder
tar -xf jokes_cli_app.tar.xz

# run the app
./joke_cli_app/app

# show all available options
./joke_cli_app/app --help

# run the app with options
./joke_cli_app/app --category=Any type=twopart --amount=2
```

> NOTE: The bundled version of the application only runs on linux.
