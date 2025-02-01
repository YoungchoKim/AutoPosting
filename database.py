import json
import mysql.connector
from datetime import datetime
from mysql.connector import Error


def get_db_connection():
    with open("config.json", "r") as f:
        config = json.load(f)

    try:
        connection = mysql.connector.connect(
            host=config['database']['host'],
            port=config['database']['port'],
            user=config['database']['user'],
            password=config['database']['password'],
            database=config['database']['database_name']
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def insert_problem_name(problem_name, daily_date):
    try:
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        insert_query = "INSERT INTO Post (problem_name, daily_date) VALUES (%s, %s)"
        cursor.execute(insert_query, (problem_name, daily_date.strftime("%Y-%m-%d"),))
        connection.commit()
        print(f"Inserted '{problem_name} {daily_date}' into Post table.")
        return True
    except Error as e:
        print(f"Error while inserting data: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def is_problem_name_exists(problem_name):
    try:
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        select_query = "SELECT COUNT(*) FROM Post WHERE problem_name = %s"
        cursor.execute(select_query, (problem_name,))
        result = cursor.fetchone()
        return result[0] > 0  # 0보다 크면 존재함
    except Error as e:
        print(f"Error while checking existence: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def is_daily_date_exists(daily_date):
    """Check if a given daily_date exists in the database."""
    try:
        connection = get_db_connection()
        if connection is None:
            return False

        cursor = connection.cursor()
        select_query = "SELECT COUNT(*) FROM Post WHERE daily_date = %s"
        cursor.execute(select_query, (daily_date.strftime("%Y-%m-%d"),))
        result = cursor.fetchone()
        return result[0] > 0  # 0보다 크면 존재함
    except Error as e:
        print(f"Error while checking existence: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    if insert_problem_name("Two Sum", datetime.now()):
        print("Data inserted successfully.")

    if is_daily_date_exists(datetime.now()):
        print("Problem name 'Two Sum' already exists.")
    else:
        print("Problem name 'Two Sum' does not exist.")

