# Assignment.

Write a program to consolidate risk reporting for clients with assets under our management, for a date before today.

The program should perform the following:
1. load all data from portfolios.xlsx. This represents the start of our report.
2. based on the data from step 1., find the risks associated with all portfolios. Sources to be used are the cashrisks.csv spreadsheet, and the two APIs.
3. per client, calculate the hedge ratio (risk of all assets over risks of all liabilities, in absolute value).
4. display the results in a manner of your choosing.

Next to that, please make sure to accomplish the following:
* write the most well-structured, production-like code you are able to - including documentation via docstrings.
* the code you write should be unit-tested.
* add all dependencies necessary to the requirements.txt file (e.g. if you use pandas, please add it to the file).
* make sure you work in your own virtual environment, with Python 3.11.x.

## Data.
There are a few sources of data to query for the required data:
1. portfolios.xlsx: spreadsheet containing all clients and their portfolio data.
2. cashrisks.csv: text file containing risks associated to cash portfolio, i.e. liabilities.
3. fx API: API with available risk data for FX portfolios.
4. derivatives API: API with available risk data for derivatives portfolios.

## Assumptions.
* .src/app/app.py has a main() function: this represents the entry point of your program.
* You are free to add as much code as needed to the ./src folder, as long as you keep the ./app/app.py file.
* The folders ./api, ./resources, and the root folder itself should not be touched or modified in any way (except for the requirements.txt file).