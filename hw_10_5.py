# hw_10_5
def remove_key_from_dict(dictionary):
    dictionary.popitem();

def clear_all(dictionary):
    dictionary.clear();

a = {'x': 1, 'y': 2};
remove_key_from_dict(a);
print(a);

clear_all(a);
print(a);
