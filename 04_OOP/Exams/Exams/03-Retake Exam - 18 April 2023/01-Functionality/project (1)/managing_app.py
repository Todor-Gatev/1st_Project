from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
    route_id = 0

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if next(filter(lambda x: x.driving_license_number == driving_license_number, self.users), None):
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles), None):
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next(filter(lambda x: x.start_point == start_point, self.routes), None)

        if route:
            if route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                route.is_locked = True

        self.route_id += 1
        self.routes.append(Route(start_point, end_point, length, self.route_id))

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self,
                  driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda x: x.route_id == route_id, self.routes))

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

        return (f"{vehicle.brand} {vehicle.model} "
                f"License plate: {vehicle.license_plate_number} "
                f"Battery: {vehicle.battery_level}% "
                f"Status: {'Damaged' if is_accident_happened else 'OK'}")

    def repair_vehicles(self, count: int):
        damaged = [x for x in self.vehicles if x.is_damaged]
        damaged = sorted(damaged, key=lambda x: (x.brand, x.model))
        count_of_repaired_vehicles = min(count, len(damaged))

        for i in range(count_of_repaired_vehicles):
            damaged[i].is_damaged = False
            damaged[i].recharge()

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        res = ["*** E-Drive-Rent ***", *[str(u) for u in sorted_users]]

        return "\n".join(res)

