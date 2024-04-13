
from employee.salaryemployee import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия"""

    def __init__(self, kod, name, weekly_salary, commission):
        super().__init__(kod, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



