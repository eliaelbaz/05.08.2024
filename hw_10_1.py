# hw_10_1
israel = {
    'name': 'Israel',
    'birth': 1948,
    'population_millions': 9.3,
    'capital': 'Jerusalem',
    'language': 'Hebrew',
    'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
    'currency': 'ILS',
    'area_Kilometer': 22145,
    'gdp_billion': 450
};
# a
print("a:", israel.get('capital'));
# b
print("b:", israel.keys());
# c
keys_uppercase = [key.upper() for key in israel.keys()];
print("c:", keys_uppercase);
# d
print("d:", israel.values());
# e
values_lengths = [len(str(value)) for value in israel.values()];
print("e:", values_lengths);
# f
print("f:", israel.items());
# g
israel_copy = israel.copy();
print("g:", israel_copy);
# h
israel_copy.clear();
print("h:", israel_copy);
# i
israel_none = dict.fromkeys(israel.keys(), None);
print("i:", israel_none);
# j
del israel['currency'];
print("j:", israel);
# k
israel.pop('area_Kilometer');
print("k:", israel);
# l
israel['national_sport'] = 'Soccer';
israel['population_millions'] = 9.4;
print("l:", israel);
