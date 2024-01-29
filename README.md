# Movie Project (PAC4, programming for Data Science)

# Table of Contents

- [Description](#description)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Install movie_project as a package](#install-movie_project-as-package)
- [Run](#run)
  - [Run all](#run-all)
  - [Run parts](#run-parts)
  - [Input](#input)
  - [Output](#output)
- [Error Handling](#error-handling)
  - [Too many CSV files](#too-many-csv-files)
  - [Error with hardcoded file paths, import, or module not found](#error-with-hardcoded-filepaths-import-or-module-not-found)
- [Modularity](#modularity)
- [Reports](#reports)
- [Run Tests](#run-tests)
- [Further Development](#further-development)



## Description
This program was written to analyze the TMBD and extract some meaningful data from it.

The pipeline includes decompressing the zip file, reading the .csv files, processing them, filtering and then generating some plots.

To view what was requested to do, check [the exercise (in catalan)](exercise.md)

To view the full report check it here: [report](movie_project/reports/pac4_report.md)

## Installation
This installation assumes that the user knows how to handle a virtual environment.

It is recommended to create a new virtual env to run this project.

### Requirements
The requirements for this package are in the requirements.txt file.

To intall them do:
```bash
pip install -r requirements.txt
```

### Install movie_project as package
To run the code in this package you also need to install it.

Go to the main directory of the package and then:
```bash
cd package_directory
pip install .
```

For example:
```bash
cd movie_project
pip install .
```

## Run
### Run all
The program can run all the parts or only some parts.

To run all together do:
```bash
python movie_project/main.py --all
```
If you get an error here, see the Error handling part.

### Run parts
The code is modular with the following blocks:
1. Decompress
2. Read and merge
3. Process
4. Filter
5. Plot

To run parts 2-5 you have to have decompressed the data first.

To run 3-5 you have to read and merge the data first.

**!IMPORTANT!** This version of the code does not handle all the errors that would occur if you don't run the sequence properly.

If you only wish to decompress run:
```bash
python movie_project/main.py --decompress
```

If you want to process the data, run: (it will also read, assumes you have decompressed before)
```bash
python movie_project/main.py --process
```

If you want to filter the data, run: (it will also read, assumes you have decompressed before)
```bash
python movie_project/main.py --filter
```

If you want to plot the data, run: (it will also read, assumes you have decompressed before)
```bash
python movie_project/main.py --plot
```
### Input
The scripts take as input the .zip file or the .csv files that are generated after decompressing.

### Output
The outputs are some dataframes, dictionaries or processed or filtered dataframes that will be shown on the terminal.
Some code has been written to save them as csv in in reports/data. But the code is commented or not implemented for all outputs.

The exercise has questions like: What are the differeces in reading the data with a dictionary or a dataframe? This questions are answered in the report in the [report](movie_project/reports/pac4_report.md) and are not printed in the terminal.

## Error handling

### Too many csv files
Important: Do not copy nor write any csv file into data folder, as the code will not work properly.

The data folder should only contain csv files that belong to a same "dataset" and share and id column.

If you need to have some csv files within the project, please write/copy them elsewhere, like in reports/data/ or dev/data/.

### Error with hard coded filepaths, import or module not found
The filepaths to the data are hard coded, so the code will not work if you are not in the parent movie_project folder.

```bash
# This will not work
cd movie_project/movie_project
python main.py -all
```

To be sure you are in the correct directory, you should see this when you type ls:
```bash
ls
CONTRIBUTING.md		LICENSE			build			movie_project		requirements.txt	setup.py
INSTALL.md		README.md		exercise.md		movie_project.egg-info	requirements_short.txt
```

## Modularity

### Organization
Decompress and read functions are called from main, but are in the /movie_project/src/decompress_read.py module

Processing functions are in the /movie_project/src/processing.py module

Filtering functions are in the /movie_project/src/filtering.py module

Plotting functions are in the /movie_project/src/plotting.py module

Finally, there is a tests.py module that can be found in: /movie_project/test/tests.py

### Reusability
The exercise explicitly asks for questions like: Show movies that started in 2023 and were cancelled.

Althought the functions have been written to be able to answer to questions more broadly, the specific answer to these questions is hard coded in the main.py output.

One can reuse the functions to answer similar questions:

Show movies that have ended and started in 1989
```python
year = 1989
status = "Ended"

year_df = filter_by_starting_year(merged_df, start_year=year)
status_year_df = filter_by_status(year_df, status=status)
print(status_year_df)
```

## Reports
The report for this exercise can be found in the [report](movie_project/reports/pac4_report.md)

The figures are in the reports/figures/ folder too, as .png file.

## Run tests
A unit test has been written to test if the code works properly.

It has been written to check for basic functioning of the code and is not an in depth test suite, but it has a coverage above 50% as required.

To run it do:
```bash
python movie_project/test/test.py
```

## Further development
As mentioned above some functions could be done more modular if further datasets were to be analyzed with the same code, or if different analysis to take place. For the present scope of the project they fullfill the purpose.

More detailed tests would also improve the quality of the code.