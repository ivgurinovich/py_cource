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


def drop_all_tables():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE IF EXISTS sales;")
                cur.execute("DROP TABLE IF EXISTS books;")
                cur.execute("DROP TABLE IF EXISTS authors;")
                print("Tables dropped successfully.")
    except Exception as e:
        print("An error occurred while dropping tables:", e)
    finally:
        conn.close()


def create_all_tables():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE authors (
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(100),
                        last_name VARCHAR(100)
                    );
                ''')
                cur.execute('''
                    CREATE TABLE books (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(100),
                        author_id INT,
                        publication_year INT,
                        FOREIGN KEY (author_id) REFERENCES authors(id)
                    );
                ''')
                cur.execute('''
                    CREATE TABLE sales (
                        id SERIAL PRIMARY KEY,
                        book_id INT,
                        quantity INT,
                        FOREIGN KEY (book_id) REFERENCES books(id)
                    );
                ''')
                print("Tables created successfully.")
    except Exception as e:
        print("An error occurred while creating tables:", e)
    finally:
        conn.close()


get_connection()
create_all_tables()
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
# drop_all_tables()
