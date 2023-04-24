class Savings:
    def __init__(self, savings_total_figure, savings_source, monthly_saving_amount, savings_interest, savings_term):
        self._savings_total_figure = savings_total_figure
        self._savings_source = savings_source
        self._monthly_saving_amount = monthly_saving_amount
        self._savings_interest = savings_interest
        self._savings_term = savings_term


    # getters


    def get_savings_total_figure(self):
        return self._savings_total_figure

    def get_savings_source(self):
        return self._savings_source

    def get_monthly_saving_amount(self):
        return self._monthly_saving_amount

    def get_savings_interest(self):
        return self._savings_interest

    def get_savings_term(self):
        return self._savings_term
