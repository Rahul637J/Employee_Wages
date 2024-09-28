'''
@Author: Rahul 
@Date: 2024-08-12
@Last Modified by: Rahul 
@Last Modified time: 2024-08-12
@Title: Employee wages - Python program to demonstrate crud operation of Employee Wages  
'''

import random

class Employee:
    
    _emp_id_counter = 1

    def __init__(self, emp_name, role):
        self.emp_name = emp_name
        self.emp_id = Employee._emp_id_counter
        Employee._emp_id_counter += 1
        self.role = role
        self.total_wage = 0

class Company:

    def __init__(self, company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour):
        self.company_name = company_name
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.employees = []

class CompanyEmployeeWage:

    @staticmethod
    def check_attendance():
        
        '''
        Description:
            Checks the attendance of an employee randomly.
        Parameters:
            None
        Return:
            int: 0, 1 and 2 based on the random attendance check.
        '''
        
        return random.randint(0, 2)

    def get_wage_per_day(self, status, wage_per_hour, full_time_hour, part_time_hour):
        
        '''
        Description:
            Calculates the wage per day based on employee status (Present, PartTime, Absent).
        Parameters:
            status (int): The attendance status of the employee (0,1,2).
            wage_per_hour (int): The wage earned by the employee per hour.
            full_time_hour (int): The number of hours considered full-time.
            part_time_hour (int): The number of hours considered part-time.
        Return:
            tuple: A tuple containing the daily wage and the number of hours worked.
        '''
        
        if status == 1:
            return full_time_hour* wage_per_hour, full_time_hour
        
        elif status == 2:
            return part_time_hour * wage_per_hour, part_time_hour
        
        else:
            return 0, 0

    def calculate_monthly_wage(self, company):
        
        '''
        Description:
            Calculates the monthly wage of all employees in a company based on maximum working hours and days.
        Parameters:
            company (Company): The company object for which the wages are being calculated.
        Return:
            monthly_wage (int): The total monthly wage for the company's employees.
            day_wise_wage (dict): The wages of each day
        '''
        
        day_wise_wage={}
        tot_working_hours, tot_working_days, monthly_wage = 0, 0, 0
        
        while tot_working_hours < company.max_working_hours and tot_working_days < company.max_working_days:
            
            status = self.check_attendance()
            daily_wage, working_hours = self.get_wage_per_day(status, company.wage_per_hour, company.full_time_hour, company.part_time_hour)
            
            key = 'DAY_' + str(tot_working_days+1)
            day_wise_wage[key] = daily_wage
            
            monthly_wage += daily_wage
            tot_working_hours += working_hours
            tot_working_days += 1
            
        return monthly_wage,day_wise_wage

class CompanyEmployeeWageBuilder:   
    
    def __init__(self):
       '''
       Description:
           Initializes the EmpWageBuilder object with an empty dictionary to store companies.
       Parameters:
           None
       Return:
           None
       '''
       self.companies = {}   
       self.obj=CompanyEmployeeWage()  
       
    def add_company(self, company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour):
        
        '''
        Description:
            Adds a new company to the EmpWageBuilder.
        Parameters:
            company_name (str): The name of the company.
            max_working_days (int): The maximum number of working days in a month for the company.
            max_working_hours (int): The maximum number of working hours in a month for the company.
            wage_per_hour (int): The wage per hour for employees in the company.
            full_time_hour (int): The number of hours considered full-time.
            part_time_hour (int): The number of hours considered part-time.
        Return:
            company_name (str): The comapny name which is added
        '''
        
        company = Company(company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour)
        self.companies[company_name] = company
         
        return company_name
            
    def update_company(self, company_name, max_working_days=None, max_working_hours=None, wage_per_hour=None, full_time_hour=None, part_time_hour=None):
        
        '''
        Description:
            Updates the details of an existing company in the EmpWageBuilder.
        Parameters:
            company_name (str): The name of the company to be updated.
            max_working_days (int, optional): The updated maximum number of working days.
            max_working_hours (int, optional): The updated maximum number of working hours.
            wage_per_hour (int, optional): The updated wage per hour.
            full_time_hour (int, optional): The updated number of hours considered full-time.
            part_time_hour (int, optional): The updated number of hours considered part-time.
        Return:
            None
        '''
        
        if company_name in self.companies:
            company = self.companies[company_name]
            
            if max_working_days:
                company.max_working_days = max_working_days
                
            if max_working_hours:
                company.max_working_hours = max_working_hours
                
            if wage_per_hour:
                company.wage_per_hour = wage_per_hour
                
            if full_time_hour:
                company.full_time_hour = full_time_hour
                
            if part_time_hour:
                company.part_time_hour = part_time_hour
                
            print("-"*40+"\n"+f"Updated Company: {company_name}"+"\n"+"-"*40)
            
        else:
            print("-"*40+"\n"+f"Company: {company_name}  does not exist"+"\n"+"-"*40)


    def delete_company(self, company_name):
        
        '''
        Description:
            Deletes a company from the EmpWageBuilder.
        Parameters:
            company_name (str): The name of the company to be deleted.
        Return:
            None
        '''
        
        if company_name in self.companies:
            del self.companies[company_name]
            
            print("-"*40+"\n"+f"Deleted Company: {company_name}"+"\n"+"-"*40)
            
        else:
            print("-"*40+"\n"+f"Company: {company_name}   does not exist"+"\n"+"-"*40)


    def add_employee_to_company(self, company_name, emp_name, role):
        
        '''
        Description:
            Adds an employee to a specific company.
        Parameters:
            company_name (str): The name of the company to which the employee will be added.
            emp_name (str): The name of the employee.
            role (str): The role of the employee within the company.
        Return:
            None
        '''
        
        if company_name in self.companies:
            company = self.companies[company_name]
            employee = Employee(emp_name, role)
            company.employees.append(employee)
            
            print("-"*60+"\n"+f"Added Employee: {emp_name} with ID: {employee.emp_id} to {company_name} as a {role}"+"\n"+"-"*60)
            
        else:
            print("-"*40+"\n"+f"Company: {company_name}   does not exist"+"\n"+"-"*40)

    def update_employee_in_company(self, company_name, emp_id, emp_name=None, role=None):
        
        '''
        Description:
            Updates an employee's details in a specific company.
        Parameters:
            company_name (str): The name of the company in which the employee works.
            emp_id (int): The ID of the employee to be updated.
            emp_name (str, optional): The updated name of the employee.
            role (str, optional): The updated role of the employee.
        Return:
            None
        '''
        
        if company_name in self.companies:
            
            company = self.companies[company_name]
            
            for employee in company.employees:
                if employee.emp_id == emp_id:
                    if emp_name:
                        employee.emp_name = emp_name
                    if role:
                        employee.role = role
                        
                    print("-"*40+"\n"+f"Updated Employee ID: {emp_id} with new details."+"\n"+"-"*40)
                    return
            print("-"*40+"\n"+f"Employee ID: {emp_id} not found in {company_name}."+"\n"+"-"*40)
            
        else:
            print("-"*40+"\n"+f"Company {company_name} not found."+"\n"+"-"*50)

    def delete_employee_from_company(self, company_name, emp_id):
        '''
        Description:
            Deletes an employee from a specific company.
        Parameters:
            company_name (str): The name of the company from which the employee will be deleted.
            emp_id (int): The ID of the employee to be deleted.
        Return:
            None
        '''
        if company_name in self.companies:
            company = self.companies[company_name]
            for employee in company.employees:
                if employee.emp_id == emp_id:
                    company.employees.remove(employee)
                    print(f"Deleted Employee ID: {emp_id} from {company_name}.")
                    return
            print("-"*50+"\n"+f"Employee ID: {emp_id} not found in {company_name}."+"\n"+"-"*50)
        else:
            print("-"*50+"\n"+f"Company {company_name} not found."+"\n"+"-"*50)

    def display_companies(self):
        
        '''
        Description:
            Displays all companies and their employees.
        Parameters:
            None
        Return:
            None
        '''
        
        if not self.companies:
            print("-"*50+"\n"+"No companies found."+"\n"+"-"*50)
            return
        
        for company_name, company in self.companies.items():
            
            print("-"*50+"\n"+f"\nCompany: {company_name}"+"\n"+"-"*50)
            
            if not company.employees:
                print("-"*50+"\n"+"No employees found."+"\n"+"-"*50)
                
            else:
                for employee in company.employees:
                    print("-"*50+"\n"+f"  Employee ID: {employee.emp_id}, Name: {employee.emp_name}, Role: {employee.role}"+"\n"+"-"*50)

    def calculate_wages_for_specific_company(self, company_name):
        
        '''
        Description:
            Calculates wages for all employees in a specific company.
        Parameters:
            company_name (str): The name of the company for which wages will be calculated.
        Return:
            int: The total monthly wage for the company's employees.
        '''
        
        if company_name in self.companies:
            company = self.companies[company_name]
            total_wage = 0
            
            for employee in company.employees:
                employee_wage ,day_wise_wage= self.obj.calculate_monthly_wage(company)
                total_wage += employee_wage
                print("-"*50+"\n"+f"Employee ID: {employee.emp_id}, Monthly Wage: {employee_wage}"+"\n"+"-"*50)
                print("-"*50+"\n"+f'Daily wage {day_wise_wage}'+"\n"+"-"*50)
                
            print("-"*50+"\n"+f"Total Monthly Wage for {company_name}: {total_wage}"+"\n"+"-"*50)
            return total_wage    
        
        else:
            print("-"*50+"\n"+f"Company {company_name} not found."+"\n"+"-"*50)

    def calculate_wages_for_all_companies(self):
        
        '''
        Description:
            Calculates wages for all employees in all companies.
        Parameters:
            None
        Return:
            int: The total wage for all companies' employees.
        '''
        
        total_wage = 0
        
        for company_name, company in self.companies.items():
            print(f"\nCalculating wages for company: {company_name}")
            total_wage += self.calculate_wages_for_specific_company(company_name)
            
        print("-"*50+"\n"+f"Total Wage for All Companies: {total_wage}"+"\n"+"-"*50)


def main():

    print("-"*55+"\n"+"|    Welcome to Employee Wage Computation Program    |"+"\n"+"-"*55)

    builder = CompanyEmployeeWageBuilder()

    while True:
        try:
            option = int(input('''Enter           
1: to add company 
2: to update company details
3: to delete company 
4: to add employee to company 
5: to update employee details 
6: to delete employee from company
7: to display all companies and their employees
8: to calculate wages for a specific company
9: to calculate wages for all companies
10: to exit
Enter your choice: '''))
            
            if option == 1:
                
                company_name = input("Enter company name: ")
                max_working_days = int(input("Enter maximum working days: "))
                max_working_hours = int(input("Enter maximum working hours: "))
                wage_per_hour = float(input("Enter wage per hour: "))
                full_time_hour = int(input("Enter full-time working hours: "))
                part_time_hour = int(input("Enter part-time working hours: "))
                
                company_name=builder.add_company(company_name, max_working_days, max_working_hours, wage_per_hour, full_time_hour, part_time_hour)
                print("-"*40+"\n"+f"Added Company: {company_name}"+"\n"+"-"*40)

            
            elif option == 2:
                
                company_name = input("Enter company name: ")
                max_working_days = input("Enter new maximum working days: ")
                max_working_hours = input("Enter new maximum working hours : ")
                wage_per_hour = input("Enter new wage per hour : ")
                full_time_hour = input("Enter new full-time working hours: ")
                part_time_hour = input("Enter new part-time working hours: ")
                
                builder.update_company(
                    company_name,
                    int(max_working_days) if max_working_days else None,
                    int(max_working_hours) if max_working_hours else None,
                    float(wage_per_hour) if wage_per_hour else None,
                    int(full_time_hour) if full_time_hour else None,
                    int(part_time_hour) if part_time_hour else None
                )

            elif option == 3:
                
                company_name = input("Enter company name: ")
                builder.delete_company(company_name)
            
            elif option == 4:
                
                company_name = input("Enter company name: ")
                emp_name = input("Enter employee name: ")
                role = input("Enter employee role : ")
                builder.add_employee_to_company(company_name, emp_name, role)
            
            elif option == 5:
                
                company_name = input("Enter company name: ")
                emp_id = int(input("Enter employee ID: "))
                emp_name = input("Enter new employee name : ")
                role = input("Enter new role: ")
                builder.update_employee_in_company(company_name, emp_id, emp_name if emp_name else None, role if role else None)
            
            elif option == 6:
                
                company_name = input("Enter company name: ")
                emp_id = int(input("Enter employee ID to delete: "))
                builder.delete_employee_from_company(company_name, emp_id)
            
            elif option == 7:
                
                builder.display_companies()

            elif option == 8:
                
                company_name = input("Enter company name to calculate wages: ")
                builder.calculate_wages_for_specific_company(company_name)

            elif option == 9:
                
                builder.calculate_wages_for_all_companies()
            
            elif option == 10:
                
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid option! Please try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()    