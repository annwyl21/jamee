import pymysql
import sys
from application.debt import Debt

class EmptyTuple(Exception):
    pass

class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        #password = 'password'
        database = 'budget_management'
        if sys.platform == 'win32':
            password = 'password'
        else:
            # this below I had to change to password = "password" (instead of empty) as otherwise it doesn't load for me
            password = "password"
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

    # INSERT DATA
    def add_username(self, username):
        sql = 'INSERT INTO budget_user(username) VALUES (%s)'
        input_values = (username)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print('rolled back')
        sql_new_user_id = 'SELECT user_id FROM budget_user ORDER BY user_id DESC LIMIT 1'
        self.cursor.execute (sql_new_user_id)
        user_id = self.cursor.fetchone()
        return user_id[0]
    
    def add_income_data(self, user_id, income_source, income_total):
        sql = """insert into income (income_source, income_total, user_id) values (%s, %s, %s)"""
        input_values = (income_source, income_total, user_id)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_form_id = "select user_id from income order by user_id desc limit 1"
        self.cursor.execute(sql_new_form_id)
        new_form = self.cursor.fetchone()
        return new_form[0]

    
    def add_form_data(self, user_id, food_drink=None, housing=None, energy=None, petrol=None, train=0, bus=None, eating=None, holidays=None, clothes=None):
        sql = """insert into form (user_id, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        input_values = (user_id, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_form_id = "select user_id from form order by id desc limit 1"
        self.cursor.execute(sql_new_form_id)
        new_form = self.cursor.fetchone()
        return new_form[0]
    
    def add_debt_data(self, debt_total_figure, debt_source='Personal Loan', debt_interest=None, **kwargs):
        if 'debt_term' not in kwargs:
            debt_term = None
        else:
            debt_term = kwargs['debt_term']
        if 'repayment' not in kwargs:
            repayment = None
        else:
            repayment = kwargs['repayment']
        sql = """insert into debt (debt_total_figure, debt_source, debt_interest, debt_term, repayment) values (%s, %s, %s, %s, %s)"""
        input_values = (debt_total_figure, debt_source, debt_interest, debt_term, repayment)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_form_id = "select debt_total_id from debt order by debt_total_id desc limit 1"
        self.cursor.execute(sql_new_form_id)
        new_form = self.cursor.fetchone()
        return new_form[0]
    
    def add_savings_data(self, savings_total_figure, savings_source, monthly_saving_amount, savings_interest, savings_term):
        sql = """insert into savings (savings_total_figure, savings_source, monthly_saving_amount, savings_interest, savings_term) values (%s, %s, %s, %s, %s)"""
        input_values = (savings_total_figure, savings_source, monthly_saving_amount, savings_interest, savings_term)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_form_id = "select savings_total_id from savings order by savings_total_id desc limit 1"
        self.cursor.execute(sql_new_form_id)
        new_form = self.cursor.fetchone()
        return new_form[0]

    # RETRIEVE DATA
    def get_form_data(self, user_id=None, limit=None):
        #single_user_data = []
        if user_id is None:
            sql = "SELECT * FROM form order by id desc limit 1"
            self.cursor.execute(sql)
            user_data = self.cursor.fetchall()
        else:
            sql = """Select food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes from form where user_id = %s"""
            input_values = (user_id)
            self.cursor.execute(sql, input_values)
            retrieved_data = self.cursor.fetchone()
            user_data = list(retrieved_data)
            user_data = [int(value or 0) for value in user_data] # recast as an integer or make it equal to 0 if 'Nonetype'
        return user_data
    
    def get_debt_data_from_id(self, table, table_id, id):
        data = []
        sql = 'Select debt_total_figure, debt_source, debt_interest, debt_term, repayment from ' + table + ' where ' + table_id + ' = %s'
        self.cursor.execute(sql, id)
        data = self.cursor.fetchone()
        debt_instance= Debt(debt_total_figure=data[0], debt_source=data[1], debt_interest=data[2], debt_term=data[3], repayment=data[4])
        #debt_list = Debt.get_debt_data(debt_instance)
        return debt_instance
    
    def get_data_from_id(self, table, table_id, id):
        data = []
        sql = 'Select * from ' + table + ' where ' + table_id + ' = %s'
        self.cursor.execute(sql, id)
        data = self.cursor.fetchone()
        return data
    
    def get_average_monthly_expense_data_for_graph(self):
        data = []
        unpacked_data = []
        self.cursor.callproc('average_monthly_data')
        retrieved_data = self.cursor.fetchall()
        # unpacking a tuple to a list so the decimal objects returned can be recast as integers
        for item in retrieved_data:
            unpacked = item
            data.append(unpacked)
        for tuple in data:
            value = int(tuple[0])
            unpacked_data.append(value)
        return unpacked_data



# retrieve data for benefits pages
    def get_benefits_data(self, benefit_requested):
        try:
            sql = "SELECT benefit_name, how, what FROM benefits where benefit_name = '" + benefit_requested + "'"
            self.cursor.execute(sql)
            retrieved_data = self.cursor.fetchall()
        except Exception as ex:
            print("Failed to query CMD for benefits data - possible problem with an element on nav bar, the endpoint wasn't passed as an argument and the query failed")
        if retrieved_data == (None,):
            raise EmptyTuple("Query Returns Empty Tuple - possibly database problem")
        else:
            return retrieved_data
    


# retrieve data for site stats pages
    def average_debt_report(self):
        try:
            sql = """select avg(debt_total_figure) from debt"""
            self.cursor.execute(sql)
            average_debt_entered = self.cursor.fetchone()
        except Exception as ex:
            print("Failed to query database for average debt total")
        if average_debt_entered == (None,):
            raise EmptyTuple("Query Returns Empty Tuple - Debt data missing from database")
        else:
            return average_debt_entered[0]
        # this try/ exception can be viewed when you comment out, teardown and reload your database without debt data (lines 309+ in the jamee*.sql script)
        # don't forget to comment it back in, teardown and re-load your database before the presentation though!
    
    def frequency_debt_report(self):
        try:
            sql = """SELECT debt_source, COUNT(*) AS freq FROM debt group by debt_source order by freq desc"""
            self.cursor.execute(sql)
            frequency_debt_type_entered = self.cursor.fetchall()
        except Exception as ex:
            print("Failed to query database for debt frequency data")
        if frequency_debt_type_entered == (None,):
            raise EmptyTuple("Query returns empty Tuple - Debt data missing from database")
        else:
            return frequency_debt_type_entered
    
    def average_savings_report(self):
        try:
            sql = """select avg(savings_total_figure) from savings"""
            self.cursor.execute(sql)
            average_savings_entered = self.cursor.fetchone()
        except Exception as ex:
            print("Failed to query database for average savings data")
        if average_savings_entered == (None,):
            raise EmptyTuple("Query returns empty tuple - Savings data missing from database")
        else:
            return average_savings_entered[0]
    
    def frequency_savings_report(self):
        try:
            sql = """SELECT savings_source, COUNT(*) AS freq FROM savings group by savings_source order by freq desc"""
            self.cursor.execute(sql)
            frequency_savings_type_entered = self.cursor.fetchall()
        except Exception as ex:
            print("Failed to query database for savings frequency data")
        if frequency_savings_type_entered == (None,):
            raise EmptyTuple("Query returns empty tuple - Savings data missing from database")
        else:
            return frequency_savings_type_entered

