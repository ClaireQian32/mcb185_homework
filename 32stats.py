import sys
import mathimport sys
import math

def stats(numbers):
    count = len(numbers)
    if count == 0:
        sys.exit("Error: No numbers provided.")

    mini = min(numbers)
    maxi = max(numbers)
    mean = sum(numbers) / count

    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)

    sorted_numbers = sorted(numbers)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]

    print(f"Count: {count}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Median: {median}")

stats(numbers)