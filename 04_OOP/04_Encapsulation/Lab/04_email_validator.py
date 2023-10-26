from typing import List


class EmailValidator(object):
    def __init__(self, min_length: int, mails_list: list, domains_list: list) -> None:
        self.min_length = min_length
        self.mails: List[str] = mails_list
        self.domains: List[str] = domains_list

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        data = email.split('@')
        name = data[0]
        data1 = data[1].split(".")
        mail = data1[0]
        domain = data1[-1]

        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True

        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
