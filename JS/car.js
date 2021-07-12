function Car(license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger;
}

Car.prototype.printDataCar = function () {
    console.log(this.driver)
    console.groupCollapsed(this.driver.name)
    console.log(this.driver.document)
}