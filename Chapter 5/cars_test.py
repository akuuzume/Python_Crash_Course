shipment_cars = ['Maybach','tesla','ferrari']
for car in shipment_cars:
    if car == 'tesla':
        print(f"{car.title()} not available in your region")
    else:
        print(f"{car.title()} is on its way to you!")