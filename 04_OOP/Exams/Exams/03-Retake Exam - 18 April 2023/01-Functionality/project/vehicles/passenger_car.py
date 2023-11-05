from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00
    VEHICLE_TYPE = "PassengerCar"

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_battery = round((mileage * 100) / self.max_mileage)
        self.battery_level -= reduce_battery
