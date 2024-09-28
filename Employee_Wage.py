'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random

WAGE_PER_HOUR=20
FULL_DAY_HOUR=8

def attendance():
    
    '''
     Description: 
          The function to check the employee is present or absent 
     Parameters:
          None        
     Return:
          1 (1): If the employee present
          0 (0): If the employee absent
     '''
     
    return random.randint(0,1)

def calculate_daily_wage(status):
    
     '''
     Description: 
          The function to calculate employee daily wage 
     Parameters:
          status (str): The employee is present or parttime or absent
     Return:
          wages (int): The daily wage of the employee
     '''
     
     if status== 1:
        return FULL_DAY_HOUR * WAGE_PER_HOUR, "FullTime"

     else:
        return 0, "Absent"

def main():
    print("****Welcome to Employee Wage Computation Program****")

     #  EMPLOYEE ATTEDANCE
    status=attendance()

     #  DAILY WAGE
    daily_wage, status =calculate_daily_wage(status)
    print(f"Employee status: '{status}'")
    print(f"The employee daily wage: {daily_wage}")
   
if __name__ == "__main__":
    main()
