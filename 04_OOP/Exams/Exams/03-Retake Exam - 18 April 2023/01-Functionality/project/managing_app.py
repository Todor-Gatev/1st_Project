from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_object(self.users, "driving_license_number", driving_license_number)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.find_object(self.vehicles, "license_plate_number", license_plate_number)

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                route.is_locked = True

        route_id = len(self.routes) + 1
        self.routes.append(Route(start_point, end_point, length, route_id))

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.find_object(self.users, "driving_license_number", driving_license_number)
        vehicle = self.find_object(self.vehicles, "license_plate_number", license_plate_number)
        route = self.find_object(self.routes, "route_id", str(route_id))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = []

        for v in self.vehicles:
            if v.is_damaged:
                damaged_vehicles.append(v)

        damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        count_of_repaired_vehicles = min(count, len(damaged_vehicles))

        for i in range(count_of_repaired_vehicles):
            damaged_vehicles[i].is_damaged = False
            damaged_vehicles[i].recharge()

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        self.users = sorted(self.users, key=lambda x: -x.rating)
        res = ["*** E-Drive-Rent ***", *[str(u) for u in self.users]]

        return "\n".join(res)

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj
    # endregion
