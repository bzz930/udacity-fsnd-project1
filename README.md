# Logs Analysis Project

## About the Project
This is the first project of Udacity's Full Stack Web Developer Nanodegree.
The project aims to create a reporting tool which queries the "news" database
to answer the three questions below:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How the Tool is Created
The reporting tool is written as a Python script. To answer each of the three
questions, SQL is used to compose the queries that extract the relevant data
from the database.

## How to Run the Reporting Tool
### Programs
- **Python**

The reporting tool is written in Python programming language. To execute the
file you'll need to have Python installed on your computer.
(Download [here](https://www.python.org/downloads/).)

- **PostgreSQL**

This project uses PostgreSQL and the Python code calls `pysopg2`. For this
project it is easier to install the virtual machine recommended below which
comes with the right settings.

- **VirtualBox** (download [here](https://www.virtualbox.org/))
- **Vagrant** (download [here](https://www.vagrantup.com/))

### Data
The database can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Unzip the file after downloading and save `newsdata.sql` into the `vagrant` directory.

To load the data, `cd` into the `vagrant` directory and use command `psql -d news -f newsdata.sql`.

### Run the Reporting tool
Steps:
1. Save the `logs-analysis.py` file into the `vagrant` directory.
2. Open the terminal or a command line tool.
3. At the prompt, type `python logs-analysis.py` and press `enter`.

The results should appear momentarily.
