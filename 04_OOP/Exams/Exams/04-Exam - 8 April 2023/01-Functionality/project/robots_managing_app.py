from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[FemaleRobot, MaleRobot] = []
        self.services: List[MainService, SecondaryService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICE_TYPES[service_type](name))

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOT_TYPES[robot_type](name, kind, price))

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_object(self.robots, "name", robot_name)
        service = self.find_object(self.services, "name", service_name)

        if not robot.POSSIBLE_SERVICE == service.__class__.__name__:
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_object(self.services, "name", service_name)
        robot = self.find_object(service.robots, "name", robot_name)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_object(self.services, "name", service_name)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.find_object(self.services, "name", service_name)

        return f"The value of service {service_name} is {sum(r.price for r in service.robots):.2f}."

    def __str__(self):
        return "\n".join(s.details() for s in self.services)

    # supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj
