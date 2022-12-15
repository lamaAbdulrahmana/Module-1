class NotEnoughMoneyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return (repr(self.value))

class Credit_Card():

    def __init__(self,cc_name,cc_number,cc_cvv,cc_bank,cc_balance):
        self.__cc_name = cc_name
        self.__cc_number = cc_number
        self.__cc_cvv = cc_cvv
        self.__cc_bank = cc_bank
        self.__cc_balance = cc_balance

    #getters
    def get_cc_name(self): return self.__cc_name
    def get_cc_number(self): return self.__cc_number
    def get_cc_cvv(self): return self.__cc_cvv
    def get_cc_bank(self): return self.__cc_bank
    def get_cc_balance(self): return self.__cc_balance

    #setters
    def set_cc_name(self,new_val): self.__cc_name = new_val
    def set_cc_number(self,new_val): self.__cc_number = new_val
    def set_cc_cvv(self,new_val): self.__cc_cvv = new_val
    def set_cc_bank(self,new_val): self.__cc_bank = new_val
    def set_cc_balance(self,new_val): self.__cc_balance = new_val



class ATM():
    def __init__(self,credit_card):
        self.__credit_card = credit_card

    def withdraw(self,amount):
        try:
            if amount > self.__credit_card.get_cc_balance():
                raise NotEnoughMoneyError("You dont have enough money to withdraw")
        except NotEnoughMoneyError:
            print("You dont have enough money to withdraw")
        else:
            self.__credit_card.set_cc_balance(self.__credit_card.get_cc_balance()-amount)
            print("you withdraw {} from your credit card and your balance is {}".format(amount,self.__credit_card.get_cc_balance()))


def main():
    cc = Credit_Card("Lama Almutai",1234123412341234,123,"SNB",500)
    atm = ATM(cc)
    atm.withdraw(5000)

main()