# Create a Python class named Fraudster with the following attributes:
# email_domain: A string representing the email domain associated with fraudulent activities (e.g., "@gmail.com").
# amount: An integer representing the total amount fraudulently approved.
# number_of_users: An integer representing the number of users associated with the specified email domain.
# Implement two methods within the class:
# fraud_amount_by_domain(): This method should return a string indicating the amount that was fraudulently received with the specified email domain.
# users_by_domain(): This method should return a string indicating the number of users using the specified email domain.
# initiate three classes:
# Spain_fraud -> email_domain="@gmail.com", amount=100000, number_of_users=5
# French_fraud -> email_domain="@yahoo.com", amount=453295, number_of_users=19
# Latin_america_fraud = "@yandex.ru", amount=1036594, number_of_users=2
 
# implement methods created in the class to return various information about these fraud rings

class Fraudsters:
    def __init__(self, email_domain:str, amount: int, number_of_users:int) -> None:
        self.email_domain = email_domain
        self.amount = amount
        self.number_of_users = number_of_users
    
    def fraud_amount_by_domain(self) -> str:
        return f"{self.amount} was approved with {self.email_domain} domain"

    def users_by_domain(self) -> str:
        return f"{self.number_of_users} were observed using {self.email_domain} domain"

if __name__ == "__main__":
    spain_fraud = Fraudsters(email_domain="@gmail.com", amount=100000, number_of_users=5)
    french_fraud = Fraudsters(email_domain="@yahoo.com", amount=453295, number_of_users=19)
    latin_america_fraud = Fraudsters(email_domain="@yandex.ru", amount=1036594, number_of_users=2)
    print(spain_fraud.fraud_amount_by_domain())