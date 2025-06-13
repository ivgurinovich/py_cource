import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="homework",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )


def select_all(table):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"select * from {table}",
                )
                print(f"{cur.fetchall()}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


get_connection()


def create_author():
    conn = get_connection()
    authors = [
        ('George', 'Orwell'),
        ('Jane', 'Austen'),
        ('Mark', 'Twain'),
        ('Ivan', 'Ivanov')
    ]
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    'insert into authors (first_name,last_name) values (%s, %s)',
                    authors
                )
                print(f"Authors are added:\n")
                for first_name, last_name in authors:
                    print(f"- {first_name} {last_name}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def add_books():
    conn = get_connection()
    books = [
        ('1984', 1, 1949),
        ('Animal Farm', 1, 1945),
        ('Pride and Prejudice', 2, 1813),
        ('Adventures of Huckleberry Finn', 3, 1884),
        ('Unnamed Book', None, 2001)
    ]
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    'insert into books (title, author_id, publication_year) values (%s, %s, %s)',
                    books
                )
                print(f"Books are added:\n")
                for title, author_id, publication_year in books:
                    print(f"- {title} ")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def add_sales():
    conn = get_connection()
    sales = [
        (1, 3),
        (2, 1),
        (3, 2),
        (4, 5)
    ]
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    'INSERT INTO sales (book_id, quantity) VALUES (%s, %s)',
                    sales
                )
                print("Sales records added:\n")
                for book_id, quantity in sales:
                    print(f"- Book ID: {book_id}, Quantity: {quantity}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


create_author()
add_books()
add_sales()
select_all('authors')
select_all('books')
select_all('sales')
