'''
@Author: Rahul 
@Date: 2024-08-08
@Last Modified by: Rahul 
@Last Modified time: 2024-08-08
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random

class Company:

    def __init__(self, company_name, max_working_days, max_working_hours, wage_per_hour):
        self.company_name = company_name
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.wage_per_hour = wage_per_hour

class EmployeeWage:
    
    def __init__(self):
        self.full_time_hour =8
        self.part_time_hour=4
    
    def attendance(self):
        
        """
        Description: 
            The function to determine if the employee is present full-time, part-time, or absent.
        
        Parameter:
            None

        Return:
            int: 1 for full-time presence, 2 for part-time, and 0 for absence.
        """
        
        return random.randint(0, 2)
    
    def calculate_wage_for_day(self, status,company):
        
        """
        Description: 
            The function to get the daily wage and hours worked based on the employee's status.

        Parameters:
            status (int): The employee's attendance status (1 for Present, 2 for PartTime, 0 for Absent).

        Return:
            tuple: (wages (int), hours_worked (int))
                - wages: The daily wage of the employee.
                - hours_worked: The number of hours worked by the employee that day.
        """
        
        if status == 1:  # Present
            return self.full_time_hour * company.wage_per_hour, self.full_time_hour
        
        elif status == 2:  # PartTime
            return self.part_time_hour * company.wage_per_hour, self.full_time_hour
        
        else:  # Absent
            return 0, 0
    
    def calculate_wage_for_month(self,company):
        
        """
        Description: 
            The function to calculate the employee's total monthly wage based on daily attendance.
            
        Parameter:
            None

        Return:
             monthly_wage (int): Total wage earned by the employee for the month.
             total_working_days (int): Total number of days worked.
             total_working_hours (int): Total number of hours worked.
             day_wise_wage (dict): The wages of each day
        """
        
        day_wise_wage={}
        total_working_hours, total_working_days, monthly_wage = 0, 0, 0
        
        while total_working_hours < company.max_working_hours and total_working_days < company.max_working_days:
            
            status = self.attendance()
            daily_wage, working_hours = self.calculate_wage_for_day(status,company)
            
            key = 'DAY_' + str(total_working_days+1)
            day_wise_wage[key] = daily_wage
            
            monthly_wage += daily_wage
            total_working_hours += working_hours
            total_working_days += 1
        
        return monthly_wage, total_working_days, total_working_hours,day_wise_wage

class EmpWageBuilder:
    
    def __init__(self):
        self.companies = []
        self.empwage=EmployeeWage()

    def add_company(self, company_name, max_working_days, max_working_hours, wage_per_hour):
        
        """
        Description: 
            The function to add a company with its wage details to the list.

        Parameters:
            company_name (str): Name of the company.
            max_working_days (int): Maximum working days in a month.
            max_working_hours (int): Maximum working hours in a month.
            wage_per_hour (int): Wage per hour for employees.
        
        Return:
            None
        """
        
        company = Company(company_name,max_working_days,max_working_hours,wage_per_hour)
        self.companies.append(company)

    def calculate_wages_for_all_companies(self):
        
        """
        Description: 
            The function to calculate and print the monthly wage, working days, and working hours for all companies in the list.
    
        Parameters:
            None
    
        Return:
            company_name (str): The name of the company.
            monthly_wage (int): The total wage calculated for the month.
            working_days (int): The total number of days the employee worked in the month.
            working_hours (int): The total number of hours the employee worked in the month.
            day_wise_wage (list): A list of wages earned day by day throughout the month.
        """
        
        for company in self.companies:
            
            monthly_wage, working_days, working_hours,day_wise_wage = self.empwage.calculate_wage_for_month(company)
            
            return company.company_name,monthly_wage, working_days, working_hours,day_wise_wage

def main():
    
    print("**** Welcome to Employee Wage Computation Program ****")
    
    emp_wage_builder = EmpWageBuilder()

    while True:
        
        try:
            option = int(input('''Enter 1 to add company \n 2 to display all companies \n 3 to calculate wages for all companies \n 4 to exit: '''))
            
            if option == 1:
                company_name = input("Enter the company name: ")
                max_working_days = int(input("Enter the total working days per month: "))
                max_working_hours = int(input("Enter the maximum working hours per month: "))
                wage_per_hour = int(input("Enter the wage per hour: "))
                emp_wage_builder.add_company(company_name, max_working_days, max_working_hours, wage_per_hour)
                print(f'Company : {company_name} added successfully!')
                
            elif option == 2:
                
                print("List of Company Names:")
                
                for company in emp_wage_builder.companies:
                    print(f"Company Name: {company.company_name} ")
                    
            elif option == 3:
                company_name,monthly_wage, working_days, working_hours,day_wise_wage = emp_wage_builder.calculate_wages_for_all_companies()
                
                print("-"*40+"\n"+f"Company Name: {company_name}")
                print(f"Monthly Wage: {monthly_wage}")
                print(f"Total Working Days: {working_days}")
                print(f"Total Working Hours: {working_hours}")
                print(f'Daily wage: {day_wise_wage}',"\n"+"-"*40)
                    
            elif option == 4:
                break
                
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
    