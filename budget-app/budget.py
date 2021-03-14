class Category(object):

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if amount < self.balance:
            self.balance -= amount
            self.ledger.append({"amount": -1* amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if amount < self.balance:
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        for dic in self.ledger:
            title = title + f"{dic['description'][0:23].ljust(23)}{format(dic['amount'], '.2f').rjust(7)} \n"
        title = title + f"Total: {format(self.balance, '.2f')}"
        return title


def create_spend_chart(categories):
    names = []
    spent = []
    percent_spent = []
    sum_spent = 0

    for i in categories:
        # Get names from each category in a list:
        names.append(i.name)
        # Get total withdraw values from each category in a list:
        spent_parcial = 0
        for j in i.ledger:
            if j["amount"] < 0:
                spent_parcial -= j["amount"]
        spent.append(round(spent_parcial,2))
        
    # Get spent in total:
    sum_spent = sum(spent)
        
    # Get percentages spent in a list, by categories:
    for i in spent:
        # Rounded to 2 decimals in percent:
        percent_spent.append(round(i / sum_spent, 2) * 100)
        

    # Now we can go to create the bar chart:
    bar_chart = "Percentage spent by category" + "\n"
    # Create a counter to have from 100 to 0:
    counter = 100
    # With this we have the layout of the bar:
    while counter >= 0:
        # Added align to right with width 4 to adjust the percentages:
        bar_chart += (str(counter) + "|").rjust(4)
        
        # If the percentage is greater or equal than the counter, add a bar:
        for i in percent_spent:
            if i >= counter:
                bar_chart += " o "
            # If the percentage is lesser than the counter, add only spaces:
            else:
                bar_chart += "   "    
        # Substract then 10 to the counter to keep writing the bar:
        counter -= 10
        # And start the next iteration of the loop in a new line:
        bar_chart += "\n"
            
    # Add necessary spaces in the horizontal line, and depending on the number of
    # categories, enlarge the line. Also we add a newline and the respective spaces
    # to align correctly the posterior names:
    bar_chart += "    " + "---" * len(percent_spent) + "-" + "\n" + "    "

    # Check the number of letters of the longest category name:
    longest_name = 0
    for i in names:
        if len(i) > longest_name:
            longest_name = len(i)
            
    # Loop through each letter of each category in one line:
    for i in range(longest_name):
        for j in names:
            if len(j) > i:
                bar_chart += " " + j[i] + " "
            else:
                bar_chart += "   "
        if i < longest_name - 1:
            bar_chart += "\n    "
    # Return the string containing the bar chart
    return bar_chart