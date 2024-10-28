import Lab2.bmi as bmi 

def test_bmi_normal_weight():
    height = 1.75  
    weight = 70.0  
    result = bmi.calculate_bmi(height, weight)
    assert result == 0, "Expected Normal Weight category (0)"

def test_bmi_over_weight():
    height = 1.75  
    weight = 80.0  
    result = bmi.calculate_bmi(height, weight)
    assert result == 1, "Expected Overweight category (1)"

def test_bmi_under_weight():
    height = 1.75  
    weight = 50.0  
    result = bmi.calculate_bmi(height, weight)
    assert result == -1, "Expected Underweight category (-1)"