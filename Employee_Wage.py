'''
@Author: Rahul 
@Date: 2024-08-09
@Last Modified by: Rahul 
@Last Modified time: 2024-08-11
@Title: Employee wages - Python program to calculate employee monthly wage 
'''

import random

class Company:
    def __init__(self, company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour):
        self.company_name = company_name
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.employees = {}

class Employee:
    _emp_id_counter = 1

    def __init__(self, emp_name, role):
        self.emp_name = emp_name
        self.emp_id = Employee._emp_id_counter
        Employee._emp_id_counter += 1
        self.role = role

class CompanyEmployeeWage:

    def check_attendance(self):
        
          '''
          Description:
              Determines the attendance status of the employee for the day.
          Parameters:
              None
          Return:
              int: A random integer representing the attendance status where:
                  0 - Absent
                  1 - PartTime
                  2 - Present
          '''
          
          return random.randint(0, 2)

    def calculate_wage_for_day(self, status, wage_per_hour, full_time_hour, part_time_hour):
        
         '''
         Description:
             Calculates the wage per day based on the employee's attendance status.
         Parameters:
             status (int): The attendance status of the employee (0 for Absent, 1 for Present, 2 for PartTime).
             wage_per_hour (int): The wage earned by the employee per hour.
             full_time_hour (int): The number of hours considered full-time for the employee.
             part_time_hour (int): The number of hours considered part-time for the employee.
         Return:
             tuple: A tuple where the first element is the daily wage (int) and the second element is the number of hours worked (int).
         '''
         
         if status == 1:
             return wage_per_hour * full_time_hour, full_time_hour
         elif status == 2:
             return wage_per_hour * part_time_hour, part_time_hour
         else:
             return 0, 0

    def calculate_wage_for_month(self, company):
        
          '''
          Description:
              Calculates the monthly wage for an employee based on their attendance and the company's wage policy.
          Parameters:
              company (Company): The company object containing wage policy details like maximum working hours, maximum working days, wage per hour, etc.
              employee (Employee): The employee object for whom the wage is being calculated.
          Return:
              tuple: A tuple containing:
                  - monthly_wage (int): The total wage earned by the employee for the month.
                  - tot_working_days (int): The total number of days the employee worked.
                  - tot_working_hours (int): The total number of hours the employee worked.
                  - day_wise_wage (dict): The wage for each day.
          '''
          
          day_wise_wage={}
          tot_working_hours, tot_working_days, monthly_wage = 0, 0, 0
          
          while tot_working_hours < company.max_working_hours and tot_working_days < company.max_working_days:
              
              status = self.check_attendance()
              daily_wage, working_hours = self.calculate_wage_for_day(status, company.wage_per_hour, company.full_time_hour, company.part_time_hour)
              
              key = 'DAY_' + str(tot_working_days+1)
              day_wise_wage[key] = daily_wage
              
              monthly_wage += daily_wage
              tot_working_hours += working_hours
              tot_working_days += 1
              
          return monthly_wage, tot_working_days, tot_working_hours, day_wise_wage
      
class CompanyEmployeeWageBuilder:
    
    def __init__(self):
        self.company_wages = {}
        self.company_employee_map = {}
        self.obj=CompanyEmployeeWage()

    def add_company(self, company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour):
        
         '''
         Description:
             Adds a new company to the wage builder system by creating a Company object and initializing its employee list.
         Parameters:
             company_name (str): The name of the company.
             max_working_days (int): The maximum number of working days allowed in a month for the company.
             max_working_hours (int): The maximum number of working hours allowed in a month for the company.
             wage_per_hour (int): The wage per hour offered by the company.
             full_time_hour (int): The number of hours considered full-time for the company.
             part_time_hour (int): The number of hours considered part-time for the company.
         Return:
             company (str): The name of the company which added
         '''
         
         company = Company(company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour)
         self.company_wages[company_name] = company
         self.company_employee_map[company_name] = []
         return company_name

    def add_employee_to_company(self, company_name, emp_name, role):
        
        '''
        Description:
            Adds a new employee to a specified company by creating an Employee object and updating the company's employee list.
        Parameters:
            company_name (str): The name of the company where the employee will be added.
            emp_name (str): The name of the employee.
            role (str): The role of the employee within the company.
        Return:
            None
        '''
        
        if company_name in self.company_wages:
            employee = Employee(emp_name, role)
            self.company_wages[company_name].employees[employee.emp_id] = employee
            self.company_employee_map[company_name].append(employee.emp_id)
            
            print(f"Added Employee: {emp_name} with ID: {employee.emp_id} to {company_name} as a {role}")
            
        else:
            print(f"Company '{company_name}' not found!")

    def display_companies(self):
        
        '''
        Description:
            Displays a list of all companies along with their respective employee IDs.
        Parameters:
            None
        Return:
            None
        '''
        
        print("\nList of Companies:")
        for company_name, emp_ids in self.company_employee_map.items():
                return company_name,emp_ids

    def calculate_wages_for_all_companies(self):
        
        '''
        Description:
            Calculates and displays the monthly wages for all employees in all companies.
        Parameters:
            None
        Return:
            None
        '''
        
        for company_name, company in self.company_wages.items():
            
            for emp_id, employee in company.employees.items():
                total_wage, working_days, working_hours, day_wise_wage = self.obj.calculate_wage_for_month(company)
                
                return company_name,emp_id,employee,total_wage,working_days,working_hours, day_wise_wage
             
def main():
    
    print("-"*55+"\n"+"|    Welcome to Employee Wage Computation Program    |"+"\n"+"-"*55)
    builder = CompanyEmployeeWageBuilder()

    while True:
        
        try:
            option = int(input('''Enter           
1: to add company 
2: to add employee to company 
3: to display all companies and their employees
4: to calculate wages for all companies 
5: to exit: '''))
            
            if option == 1:
                
                company_name = input("Enter the company name: ")
                max_working_days = int(input("Enter the total working days per month: "))
                max_working_hours = int(input("Enter the maximum working hours per month: "))
                wage_per_hour = int(input("Enter the wage per hour: "))
                full_time_hour = int(input("Enter the full-time hours per day: "))
                part_time_hour = int(input("Enter the part-time hours per day: "))
                
                company_name=builder.add_company(company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour)
                
                print(f"Company '{company_name}' added successfully!")
                
            elif option == 2:
                
                company_name = input("Enter the company name to add employee to: ")
                emp_name = input("Enter the employee name: ")
                role = input("Enter the role: ")
                
                builder.add_employee_to_company(company_name, emp_name, role)
                
            elif option == 3:
                
                company_name,emp_ids = builder.display_companies()
                
                print("-------------------------------------")
                print(f"Company Name: {company_name}")
                print(f"Employee IDs: {emp_ids}")
                print("-------------------------------------")
                
            elif option == 4:
                
                company_name,emp_id,employee,total_wage,working_days,working_hours, day_wise_wage = builder.calculate_wages_for_all_companies()
                
                print("-"*40+"\n"+f"\nCalculating wages for company: {company_name}")
                print(f"Employee ID: {emp_id}, Name: {employee.emp_name}, Role: {employee.role}, Total Wage: {total_wage}")
                print(f"Total Working Days: {working_days}, Total Working Hours: {working_hours}")
                print(f"Daily wise wage: {day_wise_wage}"+"\n"+"-" * 40)
                
            elif option == 5:
                break
            
            else:
                print("Invalid option. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()