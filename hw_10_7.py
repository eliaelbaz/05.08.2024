# hw_10_7
countries = [
    {'name': 'Israel', 'population': 9.3, 'birth': 1948},
    {'name': 'United States', 'population': 331.9, 'birth': 1776},
    {'name': 'Japan', 'population': 125.8, 'birth': 660},
    {'name': 'Australia', 'population': 25.7, 'birth': 1901},
    {'name': 'Canada', 'population': 38.0, 'birth': 1867}
];
# 1
populated_countries = list(filter(lambda c: c['population'] > 30, countries));
print("1. Countries with population > 30 million:");
for country in populated_countries:
    print(country);
# 2
modern_countries = list(filter(lambda c: c['birth'] > 1800, countries));
print("\n2. Countries founded after 1800:");
for country in modern_countries:
    print(country);
# 3
country_names = list(map(lambda c: c['name'], countries));
print("\n3. Country names:");
print(country_names);
# 4
country_birth_years = list(map(lambda c: c['birth'], countries));
print("\n4. Country birth years:");
print(country_birth_years);
# 5
sorted_by_birth = sorted(countries, key=lambda c: c['birth']);
print("\n5. Countries sorted by birth year:");
for country in sorted_by_birth:
    print(country);
# 6
sorted_by_population = sorted(countries, key=lambda c: c['population']);
print("\n6. Countries sorted by population:");
for country in sorted_by_population:
    print(country);
