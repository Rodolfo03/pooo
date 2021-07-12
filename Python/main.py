from car import Car


if __name__ == "__main__":
    print("hola mundo")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = car()
    car2.license = "nose"
    car2.driver = "nose2.0"
    print(vars(car2))