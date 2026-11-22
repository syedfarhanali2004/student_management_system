from main import *

def selection():
               print('1=add_data')
               print('2=read_data')
               print('3=update_data')
               print('4=delete_data')
               while True:
                   try:
                        choice=int(input('enter choice betweem 1 to 4:'))
                        if 1<=choice<=4:
                                 break
                        else:
                                 raise Exception('##enter choice within 1 to 4##')
                   except Exception as e: 
                                 print(e)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               if choice==1:
                           while True:
                                     add_data()
                                     try:
                                         decision = input('Do you want to add next student (y/n): ')
                                         if decision.lower()=='y':
                                                              continue
                                         elif decision.lower()=='n':
                         
                                                              print('Program stopped')
                                                              break

                                         else:
                                                              raise Exception('enter between y or n')
                                     except Exception as n:
                                                              print(n)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               elif choice==2:
                           while True:
                                     read_data()
                                     try:
                                         decision = input('Do you want to read next student (y/n): ')
                                         if decision.lower()=='y':
                                                              continue
                                         elif decision.lower()=='n':
                         
                                                              print('Program stopped')
                                                              break

                                         else:
                                                              raise Exception('enter between y or n')
                                     except Exception as n:
                                                              print(n)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               elif choice==3:
                           while True:
                                     update_data()
                                     try:
                                         decision = input('Do you want to update next student (y/n): ')
                                         if decision.lower()=='y':
                                                              continue
                                         elif decision.lower()=='n':
                         
                                                              print('Program stopped')
                                                              break

                                         else:
                                                              raise Exception('enter between y or n')
                                     except Exception as n:
                                                              print(n)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               elif choice==4:
                           while True:
                                     delete_data()
                                     try:
                                         decision = input('Do you want to delete next student (y/n): ')
                                         if decision.lower()=='y':
                                                              continue
                                         elif decision.lower()=='n':
                         
                                                              print('Program stopped')
                                                              break

                                         else:
                                                              raise Exception('enter between y or n')
                                     except Exception as n:
                                                              print(n)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    selection()