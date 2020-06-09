def cars(mark, model, **car_info):
    car_info['marka'] = mark
    car_info['model'] = model
    return car_info


car = cars('Audi', "A8", color='black', age=2)
print(car)
