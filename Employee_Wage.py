'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random
 
WORKING_DAYS_PER_MONTH = 20
WAGE_PER_HOUR = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4

def attendance():
    
    '''
     Description: 
          The function to check the employee is present or absent 
     Parameters:
          None        
     Return:
          1 (1): If the employee is present
          0 (0): If the employee is absent
     '''
     
    return random.randint(0, 2)

def calculate_wage_for_day(status):
    
     '''
     Description: 
          The function to calculate employee daily wage based on attendance status
     Parameters:
          status (int): The employee's attendance status (Present/PartTime/Absent)
     Return:
          wages (int): The daily wage of the employee
     '''
     
     if status == 1:
        return FULL_TIME_HOUR * WAGE_PER_HOUR, "FullTime"

     elif status == 2:
        return PART_TIME_HOUR * WAGE_PER_HOUR, "PartTime"

     else:
        return 0, "Absent"

def calculate_monthly_wage():
    
    '''
     Description: 
          The function to calculate employee monthly wage 
     Parameters:
          None
     Return:
          total_wage (int): The total monthly wage of the employee
     '''
    
    total_wage = 0
    
    for day in range(WORKING_DAYS_PER_MONTH):
        status = attendance()
        daily_wage,status = calculate_wage_for_day(status)
        total_wage += daily_wage
    
    return total_wage

def main():
    
    print("****Welcome to Employee Wage Computation Program****")
    
    # CALCULATE MONTHLY WAGE
    monthly_wage = calculate_monthly_wage()
    print(f"The employee's total monthly wage: {monthly_wage}")
    
if __name__ == "__main__":
    main()
