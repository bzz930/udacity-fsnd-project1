import psycopg2

DBNAME = 'news'

# 1. What are the most popular three articles of all time?
query1 = '''select articles.title, count(*) as views
            from articles join log on log.path
            like concat('%', articles.slug)
            where log.status like '%200%'
            group by articles.title
            order by views DESC limit 3'''

# 2. Who are the most popular article authors of all time?
query2 = '''select authors.name, count(*) as views
            from articles join authors on articles.author = authors.id
            join log on log.path like concat('%', articles.slug)
            where log.status like '%200%'
            group by authors.name
            order by views DESC'''

# 3. On which days did more than 1% of requests lead to errors?
query3 = '''select * from (
            select date(time) as day,
            round(100.0*sum(case when status like '%404%' then 1 else 0 end)/count(*), 2) as error_percent
            from log
            group by day
            order by error_percent) as subq
            where error_percent > 1'''

def run_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    return results
    db.close()

def print_query1_results(query):
    results = run_query(query)
    print('\n1. The three most popular articles of all time are:\n')
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views\n')

def print_query2_results(query):
    results = run_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views\n')

def print_query3_results(query):
    results = run_query(query)
    print('\n3. Days with over 1% of requests that lead to an error are:\n')
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + '%\n')

print_query1_results(query1)
print_query2_results(query2)
print_query3_results(query3)
