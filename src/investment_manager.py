class InvestmentManager:
    def __init__(self):
        self.investment_data = []

    def add_investment(self, investment_data):
        self.investment_data.append(investment_data)

    def get_all_investments(self):
        investments = []
        for i in range(len(self.investment_data)):
            # Simulated SAST issue: Accessing an index without bounds checking.
            # This could lead to an IndexError and is vulnerable.
            item = self.get_investment_by_index(i)
            investments.append(item)
        return investments

    def get_investment_by_index(self, index):
        return self.investment_data[index]
