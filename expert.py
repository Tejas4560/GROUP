class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.performance_scores = {}

    def add_performance_score(self, criterion, score):
        self.performance_scores[criterion] = score

    def get_average_score(self):
        total_score = sum(self.performance_scores.values())
        return total_score / len(self.performance_scores)

class PerformanceEvaluationSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department):
        employee = Employee(name, department)
        self.employees.append(employee)

    def evaluate_employee_performance(self, employee_name, criterion, score):
        for employee in self.employees:
            if employee.name == employee_name:
                employee.add_performance_score(criterion, score)

    def get_employee_average_score(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                return employee.get_average_score()
        return None

# Example usage:

evaluation_system = PerformanceEvaluationSystem()

# Add employees
evaluation_system.add_employee("John Doe", "Sales")
evaluation_system.add_employee("Jane Smith", "Marketing")

# Evaluate performance
evaluation_system.evaluate_employee_performance("John Doe", "Quality of Work", 8)
evaluation_system.evaluate_employee_performance("John Doe", "Punctuality", 9)
evaluation_system.evaluate_employee_performance("Jane Smith", "Quality of Work", 7)
evaluation_system.evaluate_employee_performance("Jane Smith", "Punctuality", 8)

# Get average scores
print("John Doe's average performance score:", evaluation_system.get_employee_average_score("John Doe"))
print("Jane Smith's average performance score:", evaluation_system.get_employee_average_score("Jane Smith"))
