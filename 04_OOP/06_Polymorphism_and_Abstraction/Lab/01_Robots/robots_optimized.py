class Robot:
    _diodes_amount = "d1"

    def __init__(self, name):
        self.name = name

    @classmethod
    def diodes_amount(cls):
        return cls._diodes_amount

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    _diodes_amount = "d6"

    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    _diodes_amount = "d4"

    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    _diodes_amount = "d12"

    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    try:
        print(robot.sensors_amount())
    except AttributeError:
        print("unknown robot")


def number_of_robot_diodes(robot):
    try:
        print(robot.diodes_amount())
    except AttributeError:
        print("unknown robot")


class Person:
    def __init__(self, name):
        self.name = name


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
p = Person("asd")

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
number_of_robot_sensors(p)

number_of_robot_diodes(basic_robot)
number_of_robot_diodes(da_vinci)
number_of_robot_diodes(moley)
number_of_robot_diodes(griffin)
number_of_robot_diodes(p)

print(isinstance(moley, Robot))
