#!/usr/bin/env python3
from datetime import date
import psycopg2

''' This function executes queries and fetches result.'''


def query_executer(query):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

''' This function tells 3 most popular articles of all time.'''


def popular_articles():
    query = '''select articles.title, views.num from articles, (select path,
    count(*) as num from log group by path) as views where views.path = concat
    ('/article/', articles.slug) order by num desc limit 3; '''
    result = query_executer(query)
    f = open("popular_articles.txt", "a")
    ''' Writing to popular_articles.txt file.'''
    f.write('''What are the most popular three articles of all time?\n\n''')
    for el in result:
        formatted_output = str(el[0]) + ' -- ' + str(el[1]) + ' views\n'
        f.write(str(formatted_output))

    f.close()


''' This function tells most popular article author of all time.'''


def popular_authors():
    query = '''select authors.name, count(*) as num from log,articles, authors
     where authors.id=articles.author and log.path = concat
     ('/article/', articles.slug)
     group by authors.name order by num desc; '''
    result = query_executer(query)
    f = open("popular_authors.txt", "a")
    # Writing to popular_articles.txt file.
    f.write('''Who are the most popular article authors of all time?\n\n''')
    for el in result:
        formatted_output = str(el[0]) + ' -- ' + str(el[1]) + ' views\n'
        f.write(str(formatted_output))

    f.close()

''' This function tells on which day more than 1% of requests
 lead to errors.'''


def request_error():
    query = '''select error.day, (error.num*100)/cast(ok.num as float) from
    (select cast(time as date) as day, count(*) as num from log where
    status='404 NOT FOUND' group by day) as error, (select cast(time as date)
    as day, count(*) as num from log group by day) as ok where
    error.day=ok.day and (error.num*100)/cast(ok.num as float)>1; '''
    result = query_executer(query)
    f = open("status.txt", "a")
    ''' Writing to popular_articles.txt file.'''
    f.write('''On which days did more than 1% of requests lead to\
 errors?\n\n''')
    for el in result:
        formatted_output = '''{:%B %d, %Y} -- {:.2f}% error\
        s\n'''.format(el[0], el[1])
        f.write(str(formatted_output))

    f.close()


popular_articles()
popular_authors()
request_error()
