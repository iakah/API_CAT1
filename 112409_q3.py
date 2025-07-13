class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        """Display employee details"""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: KSh {self.salary:,.2f}")
    
    def update_salary(self, new_salary):
        """Update employee salary"""
        if new_salary > 0:
            old_salary = self.salary
            self.salary = new_salary
            print(f"Salary updated from KSh {old_salary:,.2f} to KSh {new_salary:,.2f}")
            return True
        else:
            print("Salary must be greater than 0")
            return False
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}) - KSh {self.salary:,.2f}"


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        """Add an employee to the department"""
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"{employee.name} added to {self.department_name} department")
            return True
        else:
            print(f"{employee.name} is already in {self.department_name} department")
            return False
    
    def calculate_total_salary(self):
        """Calculate and return the total salary expenditure for the department"""
        total = sum(employee.salary for employee in self.employees)
        return total
    
    def display_total_expenditure(self):
        """Display the total salary expenditure for the department"""
        total = self.calculate_total_salary()
        print(f"\nTotal salary expenditure for {self.department_name}: KSh {total:,.2f}")
        if self.employees:
            average = total / len(self.employees)
            print(f"Average salary: KSh {average:,.2f}")
    
    def display_all_employees(self):
        """Display all employees in the department"""
        if not self.employees:
            print(f"No employees in {self.department_name} department")
        else:
            print(f"\nEmployees in {self.department_name} Department:")
            print("-" * 50)
            for i, employee in enumerate(self.employees, 1):
                print(f"{i}. {employee}")
    
    def find_employee_by_id(self, employee_id):
        """Find an employee by their ID"""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
    
    def remove_employee(self, employee_id):
        """Remove an employee from the department"""
        employee = self.find_employee_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            print(f"{employee.name} removed from {self.department_name} department")
            return True
        else:
            print(f"Employee with ID {employee_id} not found")
            return False
    
    def get_employee_count(self):
        """Get the number of employees in the department"""
        return len(self.employees)
    
    def __str__(self):
        return f"Department: {self.department_name} ({len(self.employees)} employees)"


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []
    
    def add_department(self, department):
        """Add a department to the company"""
        self.departments.append(department)
        print(f"{department.department_name} department added to {self.company_name}")
    
    def display_departments(self):
        """Display all departments"""
        if not self.departments:
            print("No departments created")
        else:
            print(f"\nDepartments in {self.company_name}:")
            for i, dept in enumerate(self.departments, 1):
                print(f"{i}. {dept}")
    
    def find_department_by_name(self, dept_name):
        """Find a department by name"""
        for dept in self.departments:
            if dept.department_name.lower() == dept_name.lower():
                return dept
        return None


def main():
    print("Welcome to the Employee and Department Management System")
    
    # Create company
    company_name = input("Enter company name: ").strip()
    company = Company(company_name)
    
    # Create sample departments
    departments = [
        Department("Information Technology"),
        Department("Human Resources"),
        Department("Finance"),
        Department("Marketing")
    ]
    
    for dept in departments:
        company.add_department(dept)
    
    # Add sample employees
    sample_employees = [
        Employee("Peter Kamau", "EMP001", 120000),
        Employee("Mary Njeri", "EMP002", 95000),
        Employee("James Otieno", "EMP003", 110000),
        Employee("Sarah Akinyi", "EMP004", 85000),
        Employee("Michael Kiplagat", "EMP005", 130000)
    ]
    
    # Assign sample employees to departments
    departments[0].add_employee(sample_employees[0])  # IT
    departments[0].add_employee(sample_employees[4])  # IT
    departments[1].add_employee(sample_employees[1])  # HR
    departments[2].add_employee(sample_employees[2])  # Finance
    departments[3].add_employee(sample_employees[3])  # Marketing
    
    print(f"\nSample employees added to {company_name}")
    
    while True:
        print(f"\nEmployee Management System - {company_name}")
        print("1. Display all departments")
        print("2. Add new employee")
        print("3. Display employees in a department")
        print("4. Display department expenditure")
        print("5. Update employee salary")
        print("6. Display employee details")
        print("7. Remove employee from department")
        print("8. Company summary")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            # Display all departments
            company.display_departments()
        
        elif choice == '2':
            # Add new employee
            company.display_departments()
            if not company.departments:
                print("No departments available. Please create a department first.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                name = input("Enter employee name: ").strip()
                employee_id = input("Enter employee ID: ").strip()
                
                # Check if employee ID already exists in the department
                if department.find_employee_by_id(employee_id):
                    print(f"Employee with ID {employee_id} already exists in {department.department_name}")
                    continue
                
                try:
                    salary = float(input("Enter employee salary (KSh): "))
                    if salary > 0:
                        new_employee = Employee(name, employee_id, salary)
                        department.add_employee(new_employee)
                    else:
                        print("Salary must be greater than 0")
                except ValueError:
                    print("Please enter a valid number for salary")
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '3':
            # Display employees in a department
            company.display_departments()
            if not company.departments:
                print("No departments available.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                department.display_all_employees()
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '4':
            # Display department expenditure
            company.display_departments()
            if not company.departments:
                print("No departments available.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                department.display_total_expenditure()
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '5':
            # Update employee salary
            company.display_departments()
            if not company.departments:
                print("No departments available.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                if not department.employees:
                    print(f"No employees in {department.department_name} department")
                    continue
                
                department.display_all_employees()
                employee_id = input("\nEnter employee ID: ").strip()
                employee = department.find_employee_by_id(employee_id)
                
                if employee:
                    try:
                        new_salary = float(input("Enter new salary (KSh): "))
                        employee.update_salary(new_salary)
                    except ValueError:
                        print("Please enter a valid number for salary")
                else:
                    print(f"Employee with ID {employee_id} not found")
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '6':
            # Display employee details
            company.display_departments()
            if not company.departments:
                print("No departments available.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                if not department.employees:
                    print(f"No employees in {department.department_name} department")
                    continue
                
                department.display_all_employees()
                employee_id = input("\nEnter employee ID: ").strip()
                employee = department.find_employee_by_id(employee_id)
                
                if employee:
                    print(f"\nEmployee Details:")
                    print("-" * 20)
                    employee.display_details()
                else:
                    print(f"Employee with ID {employee_id} not found")
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '7':
            # Remove employee from department
            company.display_departments()
            if not company.departments:
                print("No departments available.")
                continue
            
            dept_name = input("\nEnter department name: ").strip()
            department = company.find_department_by_name(dept_name)
            
            if department:
                if not department.employees:
                    print(f"No employees in {department.department_name} department")
                    continue
                
                department.display_all_employees()
                employee_id = input("\nEnter employee ID to remove: ").strip()
                department.remove_employee(employee_id)
            else:
                print(f"Department '{dept_name}' not found")
        
        elif choice == '8':
            # Company summary
            print(f"\nCompany Summary - {company_name}")
            print("=" * 50)
            
            total_employees = 0
            total_expenditure = 0
            
            for dept in company.departments:
                employee_count = dept.get_employee_count()
                dept_expenditure = dept.calculate_total_salary()
                
                print(f"{dept.department_name}: {employee_count} employees, KSh {dept_expenditure:,.2f}")
                total_employees += employee_count
                total_expenditure += dept_expenditure
            
            print(f"\nTotal employees: {total_employees}")
            print(f"Total company expenditure: KSh {total_expenditure:,.2f}")
            
            if total_employees > 0:
                average_salary = total_expenditure / total_employees
                print(f"Average salary across company: KSh {average_salary:,.2f}")
        
        elif choice == '9':
            print(f"Thank you for using the Employee Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()