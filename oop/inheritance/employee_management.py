#Employee little system, for showing the concept of inheritance

# Base class, works as an interface:
class Employee:
      def __init__(self, name, emp_id, salary):
          self._name = name
          self._id = emp_id
          self.salary = salary
      
      # Common method implemented for ervery type of employee and will be overwrited.
      def get_actual_work(sef):
          pass

      def get_rise(self, percentage):
          self.salary += self.salary * percentage / 100 


# Manager employee
class Manager(Employee):
      def __init__(self, name, emp_id, salary, team_size):
          super().__init__(name, emp_id, salary)
          self.team_size = team_size

      def get_actual_work(self):
          return f"{self.name} is managing a team of developers"
