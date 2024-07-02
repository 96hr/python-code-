def km_to_miles(km):
    miles = km * 0.621371
    return miles
if _name_ == "_main_":
    km = float(input("Enter distance in kilometers: "))
    miles = km_to_miles(km)
    print(f"{km} kilometers is equal to {miles} miles")
