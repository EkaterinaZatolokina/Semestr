import cx_Oracle

class SportsDatabase:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, user="stud04", password="stud04", dsn="82.179.14.185:1521/nmics/"):
        try:
            self.connection = cx_Oracle.connect(
                user=user,
                password=password,
                dsn=dsn
            )
            self.cursor = self.connection.cursor()
            return True
        except cx_Oracle.DatabaseError as e:
            print(f"Ошибка подключения: {e}")
            return False

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                column_names = [i[0] for i in self.cursor.description]
                rows = self.cursor.fetchall()
                return column_names, rows
            else:
                self.connection.commit()
                return None, None

        except cx_Oracle.DatabaseError as e:
            self.connection.rollback()
            raise e

    def call_procedure(self, proc_name, params=None):
        try:
            if params:
                self.cursor.callproc(proc_name, params)
            else:
                self.cursor.callproc(proc_name)

            results = []
            for result_cursor in self.cursor.getimplicitresults():
                columns = [i[0] for i in result_cursor.description]
                rows = result_cursor.fetchall()
                results.append((columns, rows))

            self.connection.commit()
            return results

        except cx_Oracle.DatabaseError as e:
            self.connection.rollback()
            raise e

    def get_table_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return self.execute_query(query)

    def insert_sports_facility(self, facility_id, facility_name, facility_type):
        self.call_procedure("sports_pkg.insert_facility", [facility_id, facility_name, facility_type])

    def update_sports_facility(self, facility_id, facility_name=None, facility_type=None):
        params = [facility_id, facility_name, facility_type]
        self.call_procedure("sports_pkg.update_facility", params)

    def delete_sports_facility(self, facility_id):
        self.call_procedure("sports_pkg.delete_facility", [facility_id])

    def insert_athlete(self, athlete_id, first_name, last_name, date_of_birth):
        params = [athlete_id, first_name, last_name, date_of_birth]
        self.call_procedure("sports_pkg.insert_athlete", params)

    def update_athlete(self, athlete_id, first_name=None, last_name=None, date_of_birth=None):
        params = [athlete_id, first_name, last_name, date_of_birth]
        self.call_procedure("sports_pkg.update_athlete", params)

    def delete_athlete(self, athlete_id):
        self.call_procedure("sports_pkg.delete_athlete", [athlete_id])

    def insert_result(self, athlete_id, facility_id, competition_name, sport_name, competition_date, place):
        params = [athlete_id, facility_id, competition_name, sport_name, competition_date, place]
        self.call_procedure("sports_pkg.insert_result", params)

    def update_result(self, result_id, athlete_id=None, facility_id=None, competition_name=None,
                      sport_name=None, competition_date=None, place=None):
        params = [result_id, athlete_id, facility_id, competition_name, sport_name, competition_date, place]
        self.call_procedure("sports_pkg.update_result", params)

    def delete_result(self, result_id):
        self.call_procedure("sports_pkg.delete_result", [result_id])

    def get_audit_log(self, start_date=None, end_date=None, operation_type=None):
        try:
            cursor_var = self.cursor.var(cx_Oracle.CURSOR)

            self.cursor.callproc("sports_pkg.get_audit_log",
                                 [cursor_var, start_date, end_date, operation_type])

            result_cursor = cursor_var.getvalue()

            if result_cursor:
                columns = [i[0] for i in result_cursor.description]
                rows = result_cursor.fetchall()
                return columns, rows
            else:
                return [], []

        except cx_Oracle.DatabaseError as e:
            raise Exception(f"Ошибка при получении лога: {str(e)}")

    def undo_operation(self, log_id):
        self.call_procedure("sports_pkg.undo_operation", [log_id])

    def get_summary_report(self, flag1=False, flag2=False, flag3=False):
        cursor_var = self.cursor.var(cx_Oracle.CURSOR)

        flag1_str = 'TRUE' if flag1 else 'FALSE'
        flag2_str = 'TRUE' if flag2 else 'FALSE'
        flag3_str = 'TRUE' if flag3 else 'FALSE'

        try:
            self.cursor.callproc("sports_pkg.get_summary_report",
                                 [cursor_var, flag1_str, flag2_str, flag3_str])

            result_cursor = cursor_var.getvalue()
            columns = [i[0] for i in result_cursor.description]
            rows = result_cursor.fetchall()

            return columns, rows

        except cx_Oracle.DatabaseError as e:
            raise e