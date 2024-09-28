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
          status (int): The employee is present or parttime or absent
     Return:
          wages (int): The daily wage of the employee
     '''
     
     match status:
         
      case 1:
          return FULL_TIME_HOUR * WAGE_PER_HOUR, "FullTime"
  
      case 2:
          return PART_TIME_HOUR * WAGE_PER_HOUR, "PartTime"
  
      case 0:
            return 0,"Absent"

def main():
    
    print("****Welcome to Employee Wage Computation Program****")

     #  EMPLOYEE ATTEDANCE
    status=attendance()

     #  DAILY WAGE
    wage,status=calculate_wage_for_day(status)
    print(f'Employee status: {status}')
    print(f"The daily wage: {wage}")

if __name__ == "__main__":
    main()
