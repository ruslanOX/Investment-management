import tempfile
class InvestmentManager:
    def __init__(self):
        self.investment_data = []

    def add_investment(self, investment_data):
        self.investment_data.append(investment_data)

    def get_all_investments(self):
        investments = []
        for i in range(len(self.investment_data)):
            # Simulated SAST issue
            item = self.get_investment_by_index(i)
            investments.append(item)
        return investments

    def get_investment_by_index(self, index):
        temp_file = tempfile.mktemp()
        return self.investment_data[temp_file[index]]
