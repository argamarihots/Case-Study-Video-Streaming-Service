# import library
from tabulate import tabulate

#Create Data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

#Create New User Class
class NewUser:
    def __init__(self, username):
        self.username = username
        self.current_plan = None
        self.duration_plan = None 
        self.referal_code = None
        self.referal_code_list = []
    #method to generate referral code based on data
    def generate_referal_code(self, data):
        # iterate date
        for value in data.values():
            #store referal code to vars
            self.current_plan, self.duration_plan, referal_code = value
            # append to empty list 
            self.referal_code_list.append(referal_code)
        print(self.referal_code_list)
       
    #method to new user pick plan
    def pick_plan(self, new_plan, referal_code):
        #init discount
        DISCOUNT_NEW_USER = 0.04
        #valid referal code
        if referal_code in self.referal_code_list:
            # discount logic
            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT_NEW_USER)
                return total_price
            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT_NEW_USER)
                return total_price
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT_NEW_USER)
                return total_price
            else:
                raise Exception("Plan Tidak Tersedia!")
        #not input referal code get normal price
        elif (referal_code == "") or (referal_code == ""):
            if new_plan == "Basic Plan":
                total_price = 120_000
                return total_price
            elif new_plan == "Standard Plan":
                total_price = 160_000
                return total_price
            elif new_plan == "Premium Plan":
                total_price = 200_000
                return total_price
            
            else:
                raise Exception("Plan Tidak Tersedia!")
        #not valid referal code
        else:
            raise Exception("Invalid referal code!")

#Test
#Create New User
faizal = NewUser("faizal_icikiwir")

#Convert data referal code to list
faizal.generate_referal_code(data = data)

#test case new user with referal code
faizal.pick_plan("Basic Plan", "shandy-2134")