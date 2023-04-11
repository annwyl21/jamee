import pymysql


class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'password'
        database = 'budget_management'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

        # %s are placeholders for values that will be passed into the SQL query

    def add_form_data(self, salary, other, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes):
        sql = """insert into form (salary, other, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes) values (%s, %s)"""
        input_values = (salary, other, food_drink, housing, energy, petrol, train, bus, eating, holidays, clothes)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_form_id = "select id from form order by id desc limit 1"
        self.cursor.execute(sql_new_form_id)
        new_form = self.cursor.fetchone()
        return new_form[0]

    def get_form_data(self, form_id=None, limit=None):
        all_form_data = []
        if form_id is None:
            sql = "SELECT * FROM person order by id desc"
            self.cursor.execute(sql)
            all_form_data = self.cursor.fetchall()
        else:
            sql = """Select * from person where id = %s"""
            input_values = (form_id,)
            self.cursor.execute(sql, input_values)
            all_form_data = self.cursor.fetchone()
        return all_form_data
    
    def get_benefits_data(self, benefit_requested):
        sql = "SELECT benefit_name, how, what FROM benefits where benefit_name = '" + benefit_requested + "'"
        self.cursor.execute(sql)
        retrieved_data = self.cursor.fetchall()
        unpacked_benefit_data = retrieved_data[0]
        return unpacked_benefit_data
    
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

    def get_average_monthly_expense_data_for_page_table(self):
        sql = "SELECT expense_source, expense_total FROM expense"
        self.cursor.execute(sql)
        expenses = self.cursor.fetchall()
        return expenses
    
    def add_debt_data(self, debt_total_figure, debt_source):
        sql = """insert into debt (debt_total_figure, debt_source) values (%s, %s)"""
        input_values = (debt_total_figure, debt_source)
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
    
    def average_debt_report(self):
        sql = """select avg(debt_total_figure) from debt"""
        self.cursor.execute(sql)
        average_debt_entered = self.cursor.fetchone()
        return average_debt_entered[0]
    
    def frequency_debt_report(self):
        sql = """SELECT debt_source, COUNT(*) AS freq FROM debt group by debt_source"""
        self.cursor.execute(sql)
        frequency_debt_type_entered = self.cursor.fetchall()
        return frequency_debt_type_entered
