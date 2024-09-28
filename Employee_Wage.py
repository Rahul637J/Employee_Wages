'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random

class EmployeeWage:
    
    FULL_TIME_HOUR=8
    PART_TIME_HOUR=4
    
    @classmethod
    def attendance(cls):
        
        '''
        Description: 
            The function to check if the employee is fulltime, part-time, or absent.
            
        Parameters:
            None
                    
        Return:
            1 (str): If the employee is present full-time.
            2 (str): If the employee is working part-time.
            0 (str): If the employee is absent.
        '''
        
        return random.randint(0, 2)
    
    @classmethod
    def calculate_wage_for_day(cls, status, wage_per_hour):
        
        '''
        Description: 
            The function to get the daily wage and hours worked based on the employee's status.
            
        Parameters:
            full_time_hour (int): Full-time working hours.
            part_time_hour (int): Part-time working hours.
            wage_per_hour (int): Wage per hour.
            
        Return:
            wages (int): The daily wage of the employee.
            hours_worked (int): The number of hours worked by the employee that day.
        '''
        
        if status == 1:
            return cls.FULL_TIME_HOUR * wage_per_hour, cls.FULL_TIME_HOUR
        
        elif status == 2:
            return cls.PART_TIME_HOUR * wage_per_hour, cls.PART_TIME_HOUR
        
        else:
            return 0, 0
    
    @classmethod
    def calculate_wage_for_month(cls, company):
        
        '''
        Description: 
            The function to calculate the employee's total monthly wage based on daily attendance for the company.
            
        Parameters:
            company (Company): The company object containing work hours, days, and wage details.
            
        Return:
            monthly_wage (int): The total wage earned by the employee for the month.
            working_days (int): The total number of days worked.
            working_hours (int): The total number of hours worked.
            day_wise_wage (dict): The wages of each day
        '''
        
        day_wise_wage={}
        total_working_hours, total_working_days, monthly_wage = 0, 0, 0
        
        while total_working_hours < company.max_working_hours and total_working_days < company.max_working_days:
            
            # Attendance
            status = cls.attendance()
            
            # Calculate wage for day
            daily_wage, working_hours = cls.calculate_wage_for_day(status, company.wage_per_hour)
            
            key = 'DAY_' + str(total_working_days+1)
            day_wise_wage[key] = daily_wage
            
            monthly_wage += daily_wage
            total_working_hours += working_hours
            
            total_working_days += 1
            
        return monthly_wage, total_working_days, total_working_hours,day_wise_wage


class Company:
    def __init__(self, company_name, max_working_days, max_working_hours, wage_per_hour):
        self.company_name = company_name
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.wage_per_hour = wage_per_hour

def main():
    print("**** Welcome to Employee Wage Computation Program ****")
    companies = []

    while True:
        try:
            option = int(input('''Enter 1 to add company \n 2 to display all companies \n 3 to calculate wages for all companies \n 4 to exit: '''))
            if option == 1:
                company_name = input("Enter the company name: ")
                max_working_days = int(input("Enter the total working days per month: "))
                max_working_hours = int(input("Enter the maximum working hours per month: "))
                wage_per_hour = int(input("Enter the wage per hour: "))

                company = Company(company_name, max_working_days, max_working_hours, wage_per_hour)
                companies.append(company)
                print("-"*40+"\n"+f'Company : {company_name} is added successfully!!!'+"\n"+"-"*40)

            elif option == 2:
                print("List of Company Names:")
                for company in companies:
                    print("-"*40+"\n"+f"Company Name: {company.company_name}"+"\n"+"-"*40)

            elif option == 3:
                for company in companies:
                    monthly_wage, working_days, working_hours,day_wise_wage = EmployeeWage.calculate_wage_for_month(company)
            
                    print("-"*40+"\n"+f"Company Name: {company.company_name}")
                    print(f"Monthly Wage: {monthly_wage}")
                    print(f"Total Working Days: {working_days}")
                    print(f"Total Working Hours: {working_hours}")
                    print(f"Daily wage: {day_wise_wage}"+"\n"+"-"*40)
                    

            elif option == 4:
                break

            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
