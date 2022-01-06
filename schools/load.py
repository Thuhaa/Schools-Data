from .models import School

import psycopg2

def run():
    try:
        connection = psycopg2.connect(user="joseph",
                                      password="password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="enock")
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from schools"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        school_records = cursor.fetchall()

        print(school_records)
        print("Print each row and it's columns values")
        count = 0
        for row in school_records:
            School.objects.create(
            institute=row[0], 
            building=row[1], 
            floor=row[2], 
            courses=row[3], 
            latitude=row[4], 
            longitude=row[5], 
            altitude=row[6], 
            code=row[7], 
            street=row[8], 
            ownership=row[9]
            )
            count = count+1
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
