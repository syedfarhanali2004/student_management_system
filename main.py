from connection import *


#adding data

def add_data():
        db=get_connection()
        cursor=db.cursor()
        print('## adding student data ##')
        student_name=input('enter name:')
        
             
        
        try:
             student_rollnumber=int(input('enter roll number:'))
             
             cursor.execute('''select student_rollnumber from students_info where student_rollnumber=%s''',(student_rollnumber,))
             a=cursor.fetchone()
             if a is not None:
                        raise Exception('this number already exist')
                        
        except Exception as e:
                        print(e)
                        while True:
                             student_rollnumber=int(input('enter roll number:'))

                             cursor.execute('''select student_rollnumber from students_info where student_rollnumber=%s''',(student_rollnumber,))
                             a=cursor.fetchone()
                             if a is None:
                                   break
                             print('this roll number already exist')
                       
                        
                                                
        age=int(input('enter age:'))
        student_class=input('enter student class:')
        cursor.execute('''insert into students_info (student_name,student_rollnumber,age,student_class)
                                          values(%s,%s,%s,%s)''',(student_name,student_rollnumber,age,student_class))
        db.commit()
        print('added successful')
        cursor.close()
        db.close()

#/////////////////////////////////////////////////////////////////adding data\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#reading data
def read_data():
    db=get_connection()
    cursor=db.cursor(dictionary=True,buffered=True)
    print('#readding data#')
    while True:
        try:
            student_name=input('enter name:')
            cursor.execute('''select student_name from students_info where student_name=%s''',(student_name,))
            a=cursor.fetchone()
            if a is not None:
                  break
            else:
                  raise Exception('this student not exist in database')
        except Exception as e:
                  print(e)
    while True:              
        try:
            student_rollnumber=int(input('enter roll number:'))
            cursor.execute('''select student_rollnumber from students_info 
                           where student_rollnumber=%s''',(student_rollnumber,))
            a=cursor.fetchone()
            if a is not  None:
                   break
            else:
                   raise Exception('this number not exist in database')
        except Exception as e:
                   print(e)
                   
    cursor.execute('''select * from students_info
                            where student_name=%s AND student_rollnumber=%s''',(student_name,student_rollnumber))
    result=cursor.fetchall()
    if result:
        for i in result:
            
              print("ID:", i['sl_no'])
              print("Name:", i['student_name'])
              print("Roll Number:", i['student_rollnumber'])
              print("Age:", i['age'])
              print("Class:", i['student_class'])
              print("Date:", i['today_date'])
    else:
              print('student not found')
    cursor.close()
    db.close()


#////////////////////////////////////////////////////////////////////////////////read_data\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#updating data
def update_data():
    db=get_connection()
    cursor=db.cursor()
    print('what do you want to update')
    print('1=student_name')
    print('2=student_rollnumber')
    print('3=age')
    print('4=student_class')
    while True:
        try:
            print('## updating something ##')
            a=int(input('enter within 1 to 4:'))
            if 1<=a<=4:
                    break
            else:
                    raise Exception('enter within 1 to 4')
        except Exception as e:
                          print(e)
    if a==1:
        print('#student_name updation#')
        new_name=input('enter new name:')
        while True:
                          try:
                              student_rollnumber=int(input('enter student_rollnumber for reference:'))
                              cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))
                              result = cursor.fetchone()
                              if result is not None:
                                           break
                              else:
                                         print('this number not exist in database')

                          except ValueError:
                                    print("Please enter a valid integer!")
                          
       
        if result:
            cursor.execute('''update students_info
                          set student_name=%s 
                          where  student_rollnumber=%s''',(new_name,student_rollnumber))
            db.commit()
            print('updation successful')
        else:
                          print('this student not in database')
    elif a==2:
        print('#student_rollnumber updation#')
        while True:
                          try:
                              new_roll_number=int(input('enter new roll number for reference:'))
                              cursor.execute("SELECT * FROM students_info WHERE  student_rollnumber= %s",(new_roll_number,))
                              result = cursor.fetchone()
                              if result is None:
                                           break
                              else:
                                           print('this roll number already exist')
                          except ValueError:
                                    print("Please enter a valid integer!")
        while True:
                          try:
                              student_rollnumber=int(input('enter student_rollnumber for reference:'))
                              cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))
                              result = cursor.fetchone()
                              if result is not None:
                                           break
                              else:
                                           print('this roll number not exist')

                          except ValueError:
                                    print("Please enter a valid integer!")
        
        if result:
            cursor.execute('''update students_info
                          set student_rollnumber=%s 
                          where  student_rollnumber=%s''',(new_roll_number,student_rollnumber)) 
            db.commit() 
            print('updation successful')
        else:
                          print('this student not in database')


    elif a==3:
        print('#age updation#')
        while True:
                          try:
                              new_age=int(input('enter age:'))
                              cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))
                              result = cursor.fetchone()
                              if result is not None:
                                           break


                          except ValueError:
                                    print("Please enter a valid integer!")
        while True:
                          try:
                              student_rollnumber=int(input('enter student_rollnumber for reference:'))
                              cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))
                              result = cursor.fetchone()
                              if result is not None:
                                           break
                              else:
                                           print('this roll number not exist')
                          except ValueError:
                                    print("Please enter a valid integer!")
        
        if result:
              cursor.execute('''update students_info
                          set age=%s 
                          where  student_rollnumber=%s''',(new_age,student_rollnumber))
              db.commit()
              print('updation successful')

        else:
                           print('this student not in database')
    elif a==4:
        print('#student_class updation#')
        new_class=input('enter new class name:')
        while True:
                          try:
                              student_rollnumber=int(input('enter student_rollnumber for reference:'))
                              cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))
                              result = cursor.fetchone()
                              if result is not None:
                                           break
                              else:
                                           print('this roll number not exist')

                          except ValueError:
                                    print("Please enter a valid integer!")
        cursor.execute("SELECT * FROM students_info WHERE student_rollnumber = %s",(student_rollnumber,))

        result = cursor.fetchone()
        if result:
              cursor.execute('''update students_info
                          set student_class=%s 
                          where  student_rollnumber=%s''',(new_class,student_rollnumber))
              db.commit()
              print('updation successful')
        else:
                           print('this student not in database') 
    cursor.close()
    db.close()


#///////////////////////////////////////////////////////////////////////////////update_data\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#delete_data  
def delete_data():
    db=get_connection()
    cursor=db.cursor()
    while True:
               print('## deleting student data ##')
               student_name=input('enter student name:')
               while True:
                          try:
                              student_rollnumber=int(input('enter student_rollnumber for reference:'))
                              break
                          except ValueError:
                                    print("Please enter a valid integer!")
               cursor.execute('''select * from students_info where student_name=%s and student_rollnumber=%s ''',(student_name,student_rollnumber))
               result=cursor.fetchone()
               if result is not None:
                                     cursor.execute('''delete from students_info where student_rollnumber=%s and student_name=%s''',(student_rollnumber,student_name))
                                     print('deleted successfully')

                                     break
               else:
                                    print('this is not in database')
                  
    db.commit()
    cursor.close()
    db.close()


    

if __name__ == "__main__":
    print("Main file executed directly")
























	
