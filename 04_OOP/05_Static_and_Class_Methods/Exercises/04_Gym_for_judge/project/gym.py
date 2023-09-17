from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.find_object(self.subscriptions, "id", subscription_id)
        customer = self.find_object(self.customers, "id", subscription.customer_id)
        trainer = self.find_object(self.trainers, "id", subscription.trainer_id)
        plan = self.find_object(self.plans, "id", subscription.exercise_id)
        equipment = self.find_object(self.equipment, "id", plan.equipment_id)

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

    @staticmethod
    def find_object(collection: list, attribute: str, value: int):
        for obj in collection:
            if getattr(obj, attribute) == value:
                return obj
