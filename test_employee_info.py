import employee_info

def test_calculate_average_salary():
    # Calculate the expected average manually
    total_salary = sum(item["salary"] for item in employee_info.employee_data)
    expected_average = total_salary / len(employee_info.employee_data) if employee_info.employee_data else 0
    assert employee_info.calculate_average_salary() == expected_average

def test_get_employees_by_age_range():
    # Define a sample range and calculate expected results manually
    age_lower_limit = 25
    age_upper_limit = 35
    expected_employees = [
        item for item in employee_info.employee_data 
        if age_lower_limit < item["age"] < age_upper_limit
    ]
    assert employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit) == expected_employees

def test_get_employees_by_dept():
    # Test with department "Marketing"
    department = "Marketing"
    expected_employees = [
        item for item in employee_info.employee_data 
        if item["department"].lower() == department.lower()
    ]
    assert employee_info.get_employees_by_dept(department) == expected_employees
