#!/usr/bin/env python3
import psycopg2

def postgres_connect():
   """
   Create database connection and return connection string
   """
   try:
       connection = psycopg2.connect(user = "appadmin",
				     password = "password123",
				     host = "127.0.0.1",
				     port = "5432",
				     database = "studentdb")

       return connection
   except (Exception, psycopg2.Error) as error :
       print ("Error while connecting to PostgreSQL", error)



def create_table(db_connect):
    """
    Create table in existing database
    """
    cursor = db_connect.cursor()
    
    create_table_query = '''CREATE TABLE test_db_table
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
    
    cursor.execute(create_table_query)
    db_connect.commit()
    print("Table created successfully in PostgreSQL ")
    cursor.close()
    db_connect.close()



def insert_ops(db_connect, db_table):
    """
    Insert data into existing table in database
    """
    cursor = db_connect.cursor()
    try:
        insert_table_query = """ INSERT INTO """+db_table+""" (student_regnum,student_fname,student_lname,student_grade) 
                             VALUES (%s,%s,%s,%s)"""
        record_value_to_insert = ('stdsc-005', 'Michael', 'Evans', 'Grade 7')
        cursor.execute(insert_table_query, record_value_to_insert)

        db_connect.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
        cursor.close()
        db_connect.close()
    except (Exception, psycopg2.Error) as error :
        if(db_connect,):
            print("Failed to insert record into ",db_table," table", error)



def update_ops(db_connect, db_table, studentid, gradelevel):
    """
    Update data in existing table in database. Update Grade for existing student
    """
    cursor = db_connect.cursor()
    try:
        update_query = """ UPDATE """+db_table+""" set student_grade = %s WHERE student_regnum = %s"""
        cursor.execute(update_query, (gradelevel,studentid))

        db_connect.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into",db_table,"table")
        cursor.close()
        db_connect.close()
    except (Exception, psycopg2.Error) as error :
        if(db_connect,):
            print("Failed to insert record into ",db_table," table", error)




def table_list_ops(db_connect, db_table):
    """
    List Table Contents
    """
    cursor = db_connect.cursor()
    try:
        select_query = """ select * from """+db_table
        cursor.execute(select_query)

        db_connect.commit()
        student_records = cursor.fetchall()
        print("Existing Records")
        for row in student_records:
            print("Student Registration Number = ", row[0],)
            print("Student First Name          = ", row[1])
            print("Student Last Name           = ", row[2])
            print("Student Grade               = ", row[3],"\n")
        cursor.close()
        db_connect.close()
    except (Exception, psycopg2.Error) as error :
        if(db_connect,):
            print("Failed to insert record into ",db_table," table", error)






if __name__ == '__main__':
    db_connect_string = postgres_connect()
    #create_table(db_connect_string)
    table_name = "student_table"

    # Insert Into Database
    # ---------------------------
    ###insert_ops(db_connect_string, table_name)
    
    # List Table
    # ---------------------------
    table_list_ops(db_connect_string, table_name)

    # Update Database
    # ---------------------------
    """
    student_id = "stdsc-002"
    student_new_grade = "First Grade" 
    update_ops(db_connect_string, table_name, student_id, student_new_grade)
    """
