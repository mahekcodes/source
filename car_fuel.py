fuel_average = 10 # km/liter
fuel_quantity = 5 #liter


def get_kms(fuel_quantity, fuel_average):
	car_range = fuel_quantity * fuel_average
	return car_range

def main():
	print(get_kms(2, 10))

if __name__== "__main__":
    main()