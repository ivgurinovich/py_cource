import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="homework",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )


def multiple_joins_inner():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select 
                        books.title, 
                        authors.first_name, 
                        authors.last_name,
                        books.publication_year,
                        sales.quantity
                    from books
                    inner join authors on books.author_id = authors.id
                    inner join sales on books.id = sales.book_id
                    GROUP BY books.title, authors.first_name, authors.last_name, books.publication_year, sales.quantity
                    '''
                )
                result = cur.fetchall()
                print(f"List of all books with authors and sales:\n")
                print(*result, sep='\n')
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


multiple_joins_inner()
