from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        """Hiển thị thông tin cơ bản của nhân viên"""
        print(f"Mã NV: {self.employee_id} | Tên: {self.name:<15} | ", end="")

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def get_role(self): 
        return "Full-time"
    
    def calculate_salary(self):
        """Tính theo lương cơ bản + thưởng"""
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def get_role(self): 
        return "Part-time"
    
    def calculate_salary(self):
        """Tính theo số giờ làm x lương theo giờ"""
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def get_role(self): 
        return "Intern"
    
    def calculate_salary(self):
        """Tính theo trợ cấp"""
        return self.allowance

employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]

def display_employees(employees) :
    if not employees :
        print("Danh sách trống!")
        return
    else :
        print("--- DANH SÁCH NHÂN VIÊN ---")
        for emp in employees :
            emp.display_info()
            role = emp.get_role()
            print(f"Loại: {role}")
        return
    
def display_salaries(employees) :
    if not employees :
        print("Danh sách trống!")
        return
    else :
        print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
        for emp in employees :
            emp.display_info()
            salary = emp.calculate_salary()
            print(f"Lương: {salary:,.0f}")
        return

while True :
    print("""
=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================
""")
    choice = input("Chọn chức năng (1-3): ").strip()
    if choice == '1':
        display_employees(employees)
    elif choice == '2':
        display_salaries(employees)
    elif choice == '3':
        print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
        break
    else :
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
