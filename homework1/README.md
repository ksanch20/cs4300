# Repository layout:

cs4300/
└── homework1/
    ├── src/
    │   ├── task1.py
    │   ├── task2.py
    │   ├── task3.py
    │   ├── task4.py
    │   ├── task5.py
    │   ├── task6.py
    │   └── task7.py
    ├── tests/
    │   ├── test_task1.py
    │   ├── test_task2.py
    │   ├── test_task3.py
    │   ├── test_task4.py
    │   ├── test_task5.py
    │   ├── test_task6.py
    │   └── test_task7.py
    ├── task6_read_me.txt
    └── README.md

## Requirements
This project uses Python and requires the following packages:
    -pytest (for testing)
    -numpy (used in Task 7)


## Running Code

Navigate into homework1 directory:
cd cs4300/homework1

Each task is implememted in a seperate file under src/. 
Run scripts using:
python src/<file_name>.py

Example:
python src/task1.py


## Running Tests

Tests are stored in the tests/ folder and are grouped by task.

Run all tests with:
pytest
