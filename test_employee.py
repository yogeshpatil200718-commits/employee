from employee import Employee

def test_employee_name():
    emp = Employee("yogesh", 123, "bca", 100000)
    assert emp.name == "yogesh"