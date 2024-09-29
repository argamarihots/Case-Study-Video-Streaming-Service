# Import Library 
from tabulate import tabulate

#Create Data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

#Create user class
class User:  
    #define attribute username, then current_plan and duration_plan as none
    def __init__(self, username):
        self.username = username
        self.current_plan = None
        self.duration_plan = None
    #create method to check all plans pacflix
    def check_benefit(self):
        #init column names
        headers = ["Basic plan", "Standard Plan", "Premium Plan", "Benefit"]
        # init data
        tables = [
                 ['✓', '✓', '✓', "Bisa Stream"],
                 ['✓', '✓', '✓', "Bisa Download"],
                 ['✓', '✓', '✓', "Kualitas SD"],
                 ['✗', '✓', '✓', "Kualitas HD"],
                 ['✗', '✗', '✓', "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
        print("====Pacflix Plan List===")
        print("")
        print(tabulate(tables, headers, tablefmt = "simple"))
    # method to check current plan based on username
    def check_plan(self):
    #iterte keys and value based on data
        for keys, values in data.items():
            #branching to filter username
            if self.username == keys:
            #create variable to store the values
                self.current_plan, self.duration_plan, referal_code = values
                
                print(f"Username: {self.username}")
                print(f"Current Plan = {self.current_plan}")
                print(f"Duration_plan = {self.duration_plan}")
    #Method to upgrade plan
    def upgrade_plan(self,upgrade_plan):
        #define discount
        DISCOUNT_UPGRADE = 0.05

        #Iterate keys and values based on data
        for keys, values in data.items():
            #branching to filter username
            if self.username == keys:
                #get current plan and duration plan data 
                self.current_plan, self.duration_plan, referal_code = values
                #logic filter not to pick same plan
                if upgrade_plan != self.current_plan:
                    #branching if duration plan >= 12 Month
                    if self.duration_plan >= 12:
                        #logic discount
                        if upgrade_plan == "Basic Plan":
                            total_price = 120_000 - (120_000 * DISCOUNT_UPGRADE)
                            return total_price
                        elif upgrade_plan == "Standard Plan":
                            total_price = 160_000 - (160_000 * DISCOUNT_UPGRADE)
                            return total_price
                        elif upgrade_plan == "Premium Plan":
                            total_price = 200_000 - (200_000 * DISCOUNT_UPGRADE)
                            return total_price
                        else:
                            raise Exception("Plan Tidak Ada")
                    else:
                        #Branching if not discount
                        if upgrade_plan == "Basic Plan":
                            total_price = 120_000
                            return total_price
                        elif upgrade_plan == "Standard Plan":
                            total_price = 160_000 
                            return total_price
                        elif upgrade_plan == "Premium Plan":
                            total_price = 200_000
                            return total_price
                        else:
                            raise Exception("Plan Tidak Ada")

#TEST
#Check User Current Plan
user_1 = User(username = "Shandy")
user_1.check_plan()

#Check Current User Benefit
user_1.check_benefit()

#Test if user upgrade Plan
calculate_shandy_plan = user_1.upgrade_plan(upgrade_plan = "Standard Plan")
print(f"Plan baru yang Shandy harus bayar {calculate_shandy_plan}")