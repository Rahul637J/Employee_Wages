'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random

MAXIMUM_WORKING_HOURS=100
MAXIMUM_WORKING_DAYS=20
WAGE_PER_HOUR=20
FULL_TIME_HOUR=8
PART_TIME_HOUR=4

def attendance():
    
    '''
    Description: 
        The function to check if the employee is present, part-time, or absent.
        
    Parameters:
        None        
        
    Return:
        1 (int): If the employee is present full-time.
        2 (int): If the employee is working part-time.
        0 (int): If the employee is absent.
    '''
    
    return random.randint(0, 2)

def calculate_wage_for_day(status):
    
    '''
    Description: 
        The function to get the daily wage and hours worked based on the employee's status.
        
    Parameters:
        status (int): The employee's attendance status (0,1,2).
        
    Return:
        wages (int): The daily wage of the employee.
        hours_worked (int): The number of hours worked by the employee that day.
    '''
    
    if status == 1:
        return FULL_TIME_HOUR * WAGE_PER_HOUR, FULL_TIME_HOUR
    
    elif status == 2:
        return PART_TIME_HOUR * WAGE_PER_HOUR, PART_TIME_HOUR
    
    else:
        return 0, 0

def calculate_wage_for_month():
    
    '''
    Description: 
        The function to calculate the employee's total monthly wage based on daily attendance.
        
    Parameters:
        None
        
    Return:
        monthly_wage (int): The total wage earned by the employee for the month.
        tot_working_days (int): The total number of days worked.
        tot_working_hours (int): The total number of hours worked.
    '''
    
    day_wise_wage = {}
    tot_working_hours, tot_working_days, monthly_wage = 0, 0, 0
    
    while tot_working_hours < MAXIMUM_WORKING_HOURS and tot_working_days < MAXIMUM_WORKING_DAYS:
        
        status = attendance()
        daily_wage, working_hours = calculate_wage_for_day(status)
        
        key = 'DAY_' + str(tot_working_days+1)
        day_wise_wage[key] = daily_wage

        # Calculating the wages
        monthly_wage += daily_wage
        tot_working_hours += working_hours

        tot_working_days+=1

    return monthly_wage, tot_working_days, tot_working_hours, day_wise_wage

def main():
    
    print("\n"+"**** Welcome to Employee Wage Computation Program ****"+"\n")

    monthly_wage, tot_working_days, tot_working_hours, day_wise_wage = calculate_wage_for_month()
    
    print(f"Your monthly wage is: RS {monthly_wage}")
    print(f"Total working days: {tot_working_days}")
    print(f"Total working hours: {tot_working_hours}")
    print("Day wise wages :\n",day_wise_wage,"\n")

if __name__ == "__main__":
    main()
