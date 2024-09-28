'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee daily wages  
'''

import random

WAGE_PER_HOUR=20
FULL_TIME_HOUR=8
PART_TIME_HOUR=4

def attendance():
    
    '''
     Description: 
          The function to check the employee is present or absent 
     Parameters:
          None        
     Return:
          1 (int): If the employee present
          0 (int): If the employee absent
     '''
     
    return random.randint(0,2)

def calculate_wage_for_day(status):
    
    '''
     Description: 
          The function to calculate employee daily wage 
     Parameters:
          work_hour (int): The work hour for the day
     Return:
          wages (int): The daily wage of the employee
     '''

    if status == 1:
        return WAGE_PER_HOUR * FULL_TIME_HOUR, "FullTime"

    elif status == 2:
        return WAGE_PER_HOUR * PART_TIME_HOUR, "PartTime" 

    else:
        return 0, "Absent"

def main():
    print("****Welcome to Employee Wage Computation Program****")

     #  EMPLOYEE ATTEDANCE
    status=attendance()
    
     #  CALCULATE DAILY WAGE
    daily_wage,status=calculate_wage_for_day(status)
    print(f"Employee status: {status}")
    print(f"The employee daily wage: {daily_wage}")   

if __name__ == "__main__":
    main()
