# Basic Banking System Challenge

#  Define a class called Account with the following attributes and methods:
#  - Attributes: account_number, account_holder, balance
#  - Methods: display_account_info() - prints information about the account

#  Create two subclasses, SavingsAccount and CheckingAccount, that inherit from Account.
#  Each subclass should have its own unique method, for example, earn_interest() for SavingsAccount
#  and deduct_fees() for CheckingAccount.

# for interest we need time, interest and initial funds


class Account:
    def __init__(self, account_number, account_holder, balance) -> None:
        self._account_number = account_number
        self._account_holder = account_holder
        self.balance = balance

    def display_account_info(self) -> None:
        print(
            f"{self._account_number} is owned by {self._account_holder} and has a balance of {self.balance}"
        )


class SavingsAccount(Account):
    def __init__(
        self, account_number, account_holder, balance, interest_rate, years
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
        self.years = years

    def earn_interest(self):
        self.balance += self.balance * self.interest_rate * self.years / 100

    def get_possible_interest(self) -> None:
        print(self.balance * self.interest_rate * self.years / 100)


class CheckingAccount(Account):
    def __init__(
        self, account_number, account_holder, balance, fee_rate, years
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.fee_rate = fee_rate
        self.years = years

    def deduct_fees(self, *args) -> None:
        self.balance -= self.fee_rate / 100 * self.years - sum(args)

    def get_possible_fee(self, *args) -> None:
        print(self.fee_rate * self.years + sum(args))


checkingacc = CheckingAccount(
    account_number=4123548826,
    account_holder="Vardernis Pavardenis",
    balance=7888,
    fee_rate=752,
    years=4,
)
checkingacc.display_account_info()
checkingacc.deduct_fees(564, 755)
checkingacc.get_possible_fee(564, 755)
checkingacc.display_account_info()


saving_acc = SavingsAccount(
    account_number=4123548826,
    account_holder="Vardernis Pavardenis",
    balance=7888,
    interest_rate=15,
    years=4,
)

saving_acc.display_account_info()
saving_acc.earn_interest()
saving_acc.get_possible_interest()
saving_acc.display_account_info()
