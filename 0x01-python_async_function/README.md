Python - Async task
This project demonstrates how to use Python async features to perform asynchronous tasks without blocking the main thread.

Requirements
Python 3.7 or higher
asyncio library (built-in)
Installation
No installation is required. Just clone this repository and run the main.py file.

Usage
The main.py file contains a simple example of creating and running two async tasks using the asyncio.create_task() function. The tasks are defined as coroutines using the async/await syntax. The tasks print some messages with delays to simulate some IO operations.

To run the example, execute the following command in your terminal:

python main.py

You should see the following output:

Task 1: Hello
Task 2: World
Task 1: Hello again
Task 2: World again
Done

Note that the tasks run concurrently without waiting for each other to finish.

Documentation
For more information on how to use Python async features, please refer to the following resources:

Coroutines and Tasks — Python 3.12.0 documentation
Getting Started With Async Features in Python – Real Python
asyncio — Asynchronous I/O — Python 3.12.0 documentation

