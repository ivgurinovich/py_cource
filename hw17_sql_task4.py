import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="homework",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )


def aggregate_total_sales_inner():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select 
                        authors.id,
                        authors.first_name, 
                        authors.last_name,
                        SUM(sales.quantity) as total_sales
                    from authors
                    inner join books on books.author_id = authors.id
                    inner join sales on sales.book_id = books.id
                    GROUP BY authors.id, authors.first_name, authors.last_name;
                   '''
                )
                result = cur.fetchall()
                print(f"List of all authors with sales:\n")
                print(*result, sep='\n')
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


def aggregate_total_sales_left():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    '''
                    select 
                        authors.id,
                        authors.first_name, 
                        authors.last_name,
                        coalesce(sum(sales.quantity), 0) as total_sales
                    from authors
                    left join books on books.author_id = authors.id
                    left join sales on sales.book_id = books.id
                    GROUP BY authors.id, authors.first_name, authors.last_name;
                   '''
                )
                result = cur.fetchall()
                print(f"List of all authors with total sales:\n")
                print(*result, sep='\n')
    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()


aggregate_total_sales_inner()
aggregate_total_sales_left()
