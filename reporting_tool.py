#!Python 3.5.2
from datetime import date
import psycopg2

# This function tells 3 most popular articles of all time.


def popular_articles():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute("select articles.title, views.num from articles\
, (select path, count(*) as num from log group by path) as \
views where views.path=concat('/article/', articles.slug) \
order by num desc; ")
    result = cursor.fetchall()
    f = open("popular_articles.txt", "a")
    for el in result:
        formatted_output = str(el[0]) + ' -- ' + str(el[1]) + ' views\n'
        f.write(str(formatted_output))  # Writing to popular_articles.txt file.

    f.close()
    conn.close()


# This function tells most popular article author of all time.


def popular_authors():
    conn = psycopg2.connect("dbname = news")
    cursor = conn.cursor()
    cursor.execute("select authors.name, count(*) as num from log,\
articles, authors where authors.id=articles.author and log.path=\
concat('/article/', articles.slug) group by authors.name order \
by num desc limit 3; ")
    result = cursor.fetchall()
    f = open("popular_authors.txt", "a")
    for el in result:
        formatted_output = str(el[0]) + ' -- ' + str(el[1]) + ' views\n'
        f.write(str(formatted_output))  # Writing to popular_authors.txt file.

    f.close()
    conn.close()

# This function tells on which day more than 1% of requests lead to errors.


def request_error():
    conn = psycopg2.connect("dbname = news")
    cursor = conn.cursor()
    cursor.execute("select error.day, (error.num*100)/cast(ok.num as \
        float) from (select cast(time as date) as day, count(*) as \
        num from log where status='404 NOT FOUND' group by day) as \
        error, (select cast(time as date) as day, count(*) as num \
        from log group by day) as ok where error.day=ok.day and \
        (error.num*100)/cast(ok.num as float)>1; ")
    result = cursor.fetchall()
    f = open("status.txt", "a")
    for el in result:
        formatted_output = str(el[0]) + ' -- ' + str(round(el[1], 2)) +\
            '% errors\n'
        f.write(str(formatted_output))  # Writing to status.txt file.

    f.close()
    conn.close()


popular_articles()
popular_authors()
request_error()
