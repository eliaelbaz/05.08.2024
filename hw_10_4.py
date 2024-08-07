# hw_10_4
def string_operations():
    word = input("Enter word: ");
    operation = input("Enter operation name (lower, upper, len, reverse): ");
    oper_dict = {
        'lower': lambda w: w.lower(),
        'upper': lambda w: w.upper(),
        'len': lambda w: len(w),
        'reverse': lambda w: w[::-1]
    };
    result = oper_dict.get(operation, lambda w: 'Invalid operation')(word);
    print(result);
string_operations();
