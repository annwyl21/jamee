class Debt:
    def __init__(self, debt_total_figure, debt_source, debt_interest, debt_term, repayment):
        self._debt_total_figure = debt_total_figure
        self._debt_source = debt_source
        self._debt_interest = debt_interest
        self._debt_term = debt_term
        self._repayment = repayment

        if self._debt_total_figure:
            self._debt_total_figure = int(self._debt_total_figure)
        else:
            self._debt_total_figure = 0

        if self._debt_interest:
            self._debt_interest = int(self._debt_interest)
        else:
            self._debt_interest = 5

        if self._debt_term:
            self._debt_term = int(self._debt_term)
        else:
            self._debt_term = 24
        
        if self._repayment:
            self._repayment = abs(int(self._repayment))

        else:
            self._repayment = 10
            # entering a repayment of zero will break our debt calculators 
            # (there is a while loop that continues until a loan amount is paid - reaches a zero value, if repayment = 0 it creates an infinite loop) 
            # so we have a default repayment of 10
        
    
    def get_debt_total_figure(self):
        return self._debt_total_figure
    
    def get_debt_source(self):
        return self._debt_source
    
    def get_debt_interest(self):
        return self._debt_interest
    
    def get_debt_term(self):
        return self._debt_term
    
    def get_repayment(self):
        return self._repayment
    
    def get_stack_months(self):
        return self._stack_months
    
    def get_stack_years(self):
        return self._stack_years
    
    def get_snowball_months(self):
        return self._snowball_months
    
    def get_snowball_years(self):
        return self._snowball_years
    
    def get_avalanche_months(self):
        return self._avalanche_months
    
    def get_avalanche_years(self):
        return self._avalanche_years
    
    def get_debt_list(self):
        return [self._debt_total_figure, self._debt_source, self._debt_interest, self._debt_term, self._repayment]

    def set_stack_months(self, months):
        self._stack_months = months
        self._stack_years = int(months/12)
    
    def set_snowball_months(self, months):
        self._snowball_months = months
        self._snowball_years = int(months/12)
    
    def set_avalanche_months(self, months):
        self._avalanche_months = months
        self._avalanche_years = int(months/12)
    
    def set_comparison_type_months(self, num_of_months, comparison_type):
        if comparison_type == 'stack':
            self.set_stack_months(num_of_months)
        elif comparison_type == 'snowball':
            self.set_snowball_months(num_of_months)
        elif comparison_type == 'avalanche':
            self.set_avalanche_months(num_of_months)
        else:
            raise "I don't know the comparison_type"
    
    def comparison_dict(self):
        return {
            'debt_source': self._debt_source,
            'debt_total_figure': self._debt_total_figure,
            'debt_interest': self._debt_interest,
            'debt_repayment': self._repayment,
            'stack_paid_months': self._stack_months,
            'stack_paid_years': self._stack_years,
            'snowball_paid_months': self._snowball_months,
            'snowball_paid_years': self._snowball_years,
            'avalanche_paid_months': self._avalanche_months,
            'avalanche_paid_years': self._avalanche_years
        }