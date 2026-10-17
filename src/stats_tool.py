import math

def std_dev(numbers):
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
