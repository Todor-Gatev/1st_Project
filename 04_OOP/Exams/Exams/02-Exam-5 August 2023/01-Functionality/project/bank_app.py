from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        self.loans.append(self.LOAN_TYPES[loan_type]())

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_object(self.clients, "client_id", client_id)
        loan = self.find_object(self.loans, "LOAN_TYPE", loan_type)

        if client.POSSIBLE_LOAN_TYPE != loan_type:
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_object(self.clients, "client_id", client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.LOAN_TYPE == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        # total_clients_income = sum(client.income for client in self.clients)
        # loans_count_granted_to_clients = sum(len(client.loans) for client in self.clients)
        # granted_sum = sum(sum(loan.amount for loan in client.loans) for client in self.clients)
        # not_granted_sum = sum(loan.amount for loan in self.loans)

        # region Float problem

        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        clients_interest_rate = 0
        not_granted_sum = sum(loan.amount for loan in self.loans)

        for client in self.clients:
            clients_interest_rate += client.interest
            total_clients_income += client.income
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += sum(loan.amount for loan in client.loans)

        avg_client_interest_rate = clients_interest_rate / len(self.clients) if self.clients else 0

        # endregion

        # avg_client_interest_rate = (
        #     sum(client.interest for client in self.clients) / len(self.clients) if self.clients else 0
        # )

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
