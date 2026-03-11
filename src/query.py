import sqlite3

DB_PATH = "customer_data.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def total_customers():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) FROM customers
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print(f"Total customers: {result[0]}")

    conn.close()


def average_age():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT AVG(age) FROM customers
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print(f"Average age: {result[0]}")

    conn.close()


def customers_per_signup_date():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT signup_date, COUNT(*)
    FROM customers
    GROUP BY signup_date
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()