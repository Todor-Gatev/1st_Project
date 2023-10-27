from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails_lst: list, domains_lst: list):
        self.min_length = min_length
        self.mails: List[str] = mails_lst
        self.domains: List[str] = domains_lst

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        n_data = email.split('@')
        name = n_data[0]
        m_data = n_data[1].split('.')
        mail = m_data[0]
        domain = m_data[-1]

        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
