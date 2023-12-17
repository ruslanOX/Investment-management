import subprocess
class InvestmentManager:
    def __init__(self):
        self.investment_data = []

    def add_investment(self, investment_data):
        self.investment_data.append(investment_data)

    def get_all_investments(self, investment_type):
        investments = []
        for i in range(len(self.investment_data)):
            # Simulated SAST issue
            item = self.get_investment_by_index(i, investment_type)
            investments.append(item)
        return investments

    def get_investment_by_index(self, index, investment_type):
        output = subprocess.run(
                self.investment_data[index] + investment_type,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        return output 
