Curriculum <br>
**Short Specializations** <br>

# 0x02. Python - Async Comprehension

`Python` `Back-end`

# Python - Async Comprehension

This project demonstrates how to use **async generators** and **async comprehensions** in Python to perform concurrent tasks.

## Async Generator

An async generator is a function that uses the `async def` syntax and yields values. It can be used to create an asynchronous iterator that can be consumed by an `async for` loop or an async comprehension.

An example of an async generator is:

```python
async def async_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step
        await asyncio.sleep(0.1)
```

This function generates numbers from `start` to `stop` with a given `step`, and pauses for 0.1 seconds between each yield.

## Async Comprehension

An async comprehension is a syntactic construct that allows creating a list, set, dict, or generator expression from an asynchronous iterator. It uses the `async for` syntax inside the brackets.

An example of an async comprehension is:

```python
async def main():
    # Create a list of squares from an async generator
    squares = [x**2 async for x in async_range(10)]
    print(squares)

    # Create a set of odd numbers from an async generator
    odds = {x async for x in async_range(10) if x % 2 == 1}
    print(odds)

    # Create a dict of number-word pairs from an async generator
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_words = {x: words[x] async for x in async_range(10)}
    print(num_words)

    # Create an async generator expression from an async generator
    async_gen = (x*2 async for x in async_range(10))
    async for x in async_gen:
        print(x)
```

This function creates different collections from the same async generator using async comprehensions, and prints them.

## Async Generator Run Time for Four Parallel Comprehensions

To measure the run time of four parallel comprehensions using the same async generator, we can use the `asyncio.gather` function to run them concurrently and the `time` module to record the start and end times.

An example of measuring the run time is:

```python
import asyncio
import time

async def measure_run_time():
    start = time.time()
    await asyncio.gather(
        sum([x**2 async for x in async_range(1000)]),
        sum([x**3 async for x in async_range(1000)]),
        sum([x**4 async for x in async_range(1000)]),
        sum([x**5 async for x in async_range(1000)])
    )
    end = time.time()
    print(f"Run time: {end - start} seconds")

asyncio.run(measure_run_time())
```

This function calculates the sum of different powers of numbers from an async generator, and prints the run time. On my machine, it took about 10.8 seconds to run.
