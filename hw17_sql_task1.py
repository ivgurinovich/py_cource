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


def create_author(first_name, last_name):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    'insert into authors (first_name,last_name) values (%s, %s)',
                    (first_name, last_name)
                )
                print(f"Authors are added:\n")
                print(f"{first_name} {last_name}")


    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def add_books(books):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    'insert into books (title, author_id, publication_year) values (%s, %s, %s)',
                    books
                )
                print("Books are added:\n")
                for title, author_id, year in books:
                    print(f"{title}, {author_id}, {year}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def add_sales(sales):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    'insert into sales (book_id, quantity) values (%s, %s)',
                    sales
                )
                print("Sales records added:")
                for book_id, qty in sales:
                    print(f"Book ID {book_id}, Quantity {qty}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


get_connection()
create_author('George', 'Orwell')
create_author('Jane', 'Austen')
create_author('Mark', 'Twain')
create_author('Ivan', 'Ivanov')
add_books([
    ('1984', 1, 1949),
    ('Animal Farm', 1, 1945),
    ('Pride and Prejudice', 2, 1813),
    ('Adventures of Huckleberry Finn', 3, 1884),
    ('Unnamed Book', None, 2001)
])
add_sales([
    (1, 3),
    (2, 1),
    (3, 2),
    (4, 5)
])
select_all('authors')
select_all('books')
select_all('sales')
