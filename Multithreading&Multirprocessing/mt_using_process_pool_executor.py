from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"Square of {number}: {number * number}"

numbers = [1, 2, 4, 5, 6]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)