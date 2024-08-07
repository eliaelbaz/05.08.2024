# hw_10_3
def get_statistics(numbers):
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
        'count': len(numbers)
    };
print(get_statistics([1, 2, 3, 4, 5]));
