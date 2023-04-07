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
        database = 'form_db'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

        # %s are placeholders for values that will be passed into the SQL query

    def add_form_data(self, salary, other, rent, electricity, gas, water, council, phone, subscriptions, savings):
        sql = """insert into form (salary, other, rent, electricity, gas, water, council, phone, subscriptions, savings) values (%s, %s)"""
        input_values = (salary, other, rent, electricity, gas, water, council, phone, subscriptions, savings)
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
