# Fuzzing SQLite

## Overview
[SQLite](https://sqlite.org/) is a widely used, lightweight, serverless database engine. It is integrated into mobile devices, major web browsers, and numerous embedded systems, making it a critical component of modern applications. 

This project focuses on **fuzz testing SQLite** to uncover potential vulnerabilities, identify crashes, and improve the security of the database engine. Using both **mutation-based** and **grammar-based fuzzing**, we generate randomized SQL queries to detect flaws in SQLite's query processing.

## Acknowledgements
This project was inspired by [an interactive exercise](https://jzamudio.com/sql-grammar-based-fuzzer/) from the [Fuzzing and Software Security Summer School](https://fuzzing.comp.nus.edu.sg/) and references concepts from [The Fuzzing Book](https://www.fuzzingbook.org/).

## Features
- **Mutation-Based Fuzzing**: Generates new SQL test cases by modifying existing inputs.
- **Grammar-Based Fuzzing**: Uses structured SQL grammar to generate syntactically valid queries.
- **Automated Bug Detection**: Identifies crashes and unexpected behavior.
- **Code Coverage Analysis**: Leverages tools like `gcov` to assess test effectiveness.
- **Docker Support**: Provides ready-to-use Docker configurations for quick deployment.

## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/your-username/Fuzzing-SQLite.git
cd Fuzzing-SQLite

### 2. Build & Run with Docker (Recommended)

####For Intel-based systems:

docker build -t fuzzing-sqlite -f Dockerfile-Intel .
docker run --rm -it fuzzing-sqlite

#### For ARM-based systems:

docker build -t fuzzing-sqlite -f Dockerfile-Arm64 .
docker run --rm -it fuzzing-sqlite

### 3. Manual Setup

Ensure you have Python 3 installed, then install dependencies:

pip install -r requirements.txt

## Running the Fuzzer

#### Run the mutation-based fuzzer:

python system/mutation_fuzzer.py

#### Run the grammar-based fuzzer:

python system/sqlite3.c --fuzzing-mode

##Understanding Results
Generated test cases and PoC exploits are stored in results/.
Coverage reports are visualized in images/gcovr.png and images/plot.png.

## Contributors
This project was developed as part of a collaborative security research effort, and the contributors are listed in group_info.


### 2. 

### 3. Manual Setup 
pip install -r requirements.txt


## Running the Fuzzer