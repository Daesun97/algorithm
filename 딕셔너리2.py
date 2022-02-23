n = int(input())

Country_Capital = {}

for i in range(n):
    Country, Capital = input().split()
    Country_Capital[Country] = Capital


input_country=input()

print(Country_Capital.get(input_country, "Unknown Country"))