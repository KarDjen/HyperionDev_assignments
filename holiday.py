# Note: we could alternatively use openpyxl and work out data from a xl sheet
#       with price for flights, car rental, and hotel cost. However, we
#       have followed the instructions as provided

# We initialize a list of cities which includes European capitals
# We assume that the user will be flying from London
cities = ['amsterdam', 'andorra la vella', 'ankara', 'astana', 'athens',
           'baku', 'belgrade', 'berlin', 'bern', 'bratislava', 'brussels',
           'bucharest', 'budapest', 'chisinau', 'copenhagen', 'dublin',
           'helsinki', 'kiev', 'lisbon', 'ljubljana', 'luxembourg',
           'madrid', 'minsk', 'monaco', 'moscow', 'nicosia', 'oslo', 'paris',
           'podgorica', 'prague', 'reykjavík', 'riga', 'rome', 'san marino',
           'sarajevo', 'skopje', 'sofia', 'stockholm', 'tallinn', 'tbilisi',
           'tirana', 'vaduz', 'valletta', 'vatican city', 'vienna', 'vilnius',
           'warsaw', 'yerevan', 'zagreb']

# We initialize a list of prices for flights with random values from 20 to 50
price = [104, 108, 39, 24, 144, 70, 150, 91, 56, 97, 55, 65, 23, 128, 144, 31,
         82, 148, 48, 40, 134, 41, 147, 90, 64, 102, 124, 80, 70, 138, 147,
         112, 148, 118, 131, 65, 146, 50, 130, 125, 71, 89, 80, 115, 100, 109,
         68, 144, 150]

# We create a dict with key/value
list_of_cities_with_price = dict(zip(cities, price))

# Inputs from the user relating to:
#       - city_flight: city they will be flying to
#       - num_nights: number of nights they will be staying at the hotel
#       - rental_days: number of days they will be hiring a car for
# We also provide error handling for values provided
while True:
    try:
        city_flight = str(input('Please enter the city you will be flying to: '))
        lowercase_input = city_flight.lower()
        if lowercase_input not in cities:
                raise ValueError('Oops...I do not know this city. Please try a capital city located in Europe.')
        break
    except ValueError as err:
        print(err)
        continue

while True:

    try:
        num_nights = int(input('Please enter the number of nights you will be staying at the hotel: '))
        rental_days = int(input('Please enter the number of days you will be hiring a car for: '))
        break
    except ValueError:
        print('Invalid input. Please try again')
        continue


# We randomly provide the price of 54 per night
# Note: we could alternatively use the same approach taken for plane_cost
def hotel_cost(num_nights: int) -> int:
    price = 54
    total_hotel_cost = num_nights * price
    return total_hotel_cost

# We didn't use if/else, but instead we use dict from previous task as a way to practice
# We assume a price including returns
def plane_cost(city_flight: str) -> int:
        return list_of_cities_with_price[lowercase_input]

# We randomly provide the price of 54 per day of rental
def car_rental(rental_days: int) -> int:
    daily_rental_price = 50
    total_car_rental = daily_rental_price * rental_days
    return total_car_rental

# We provide the function holiday_cost that will reuse the previous functions
# Note : alternatively, we could have used the usual def_main
def holiday_cost(num_nights: int, city_flight: int, rental_days: int) -> int:
    total_holiday_cost = car_rental(rental_days) + plane_cost(city_flight) + hotel_cost(num_nights)
    return total_holiday_cost

# We display all the details about the holiday in a readable way
print(f'You will be flying to {city_flight}.')
print(f'You will stay {num_nights} night(s). ')
print(f'You will rent a car for {rental_days} day(s).')
print(f'The total cost of your holiday is {holiday_cost(num_nights, city_flight, rental_days)}.')