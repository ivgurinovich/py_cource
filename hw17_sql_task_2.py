import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="homework",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )


def inner_join_books_on_authors():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select books.title, authors.first_name, authors.last_name, books.publication_year
                    from books
                    inner join authors on books.author_id = authors.id
                    '''

                )
                result = cur.fetchall()
                print(f"Books and their authors:\n")
                for title, first_name, last_name, year in result:
                    print(f"{title} ({year}) — {first_name} {last_name}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def left_join_authors_on_books():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select authors.first_name, authors.last_name, books.title
                    from authors
                    left join books on authors.id = books.author_id;
                    '''
                )
                result = cur.fetchall()
                print(f"Authors and their books (including those without books):\n")
                for first_name, last_name, title in result:
                    print(f"{first_name} {last_name} - {title}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()

def right_join_books_on_authors():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select books.title, authors.first_name, authors.last_name, books.publication_year
                    from authors
                    right join books on authors.id = books.author_id
                    '''

                )
                result = cur.fetchall()
                print(f"Books and their authors:\n")
                for title, first_name, last_name, year in result:
                    print(f"{title} ({year}) — {first_name} {last_name}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()

inner_join_books_on_authors()
left_join_authors_on_books()
right_join_books_on_authors()
