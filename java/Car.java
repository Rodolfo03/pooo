class Car {
    Integer id;
    String license;
    String driver;
    Integer passegenger;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {
        System.out.println("license: " + license +  " Driver: " + driver);
    }
}