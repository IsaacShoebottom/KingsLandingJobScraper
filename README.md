# Kings Landing Job Scraper

A simple python script that scrapes from their site, checks if there is a new job, and then if there is, it tells you and sends a console bell command to your terminal.

The default interval for checking is 3 hours, but can be changed with an argument.

## Installation

1. Clone the repo
2. Install the requirements with `pip install -r requirements.txt`

You might want to create a virtual environment for this, if you don't know how to do that, [here's a guide](https://docs.python.org/3/library/venv.html).
Then, you can activate it with `source venv/bin/activate` on Linux and `venv\Scripts\activate` on Windows.


Virtual environments are a good way to keep your system clean and avoid conflicts with other projects. If you do not have any other projects or are fine with installing the requirements globally, you can skip this step.

## Usage
1. Run the script with `python scraper.py`
2. If you want to change the interval, run the script with `python scraper.py <interval in hours>`

If you want to turn off the bell sound, you can do so by commenting out the `print("\a")` line.

## Exiting the program
To exit the program, press `Ctrl+C` or close the terminal window.

## License
See [LICENSE](LICENSE)