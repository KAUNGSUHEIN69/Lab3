import price_info

def test_total_cost_shopping():
    expected_total_cost = (
        price_info.price_list['apple']*price_info.quantity_list['apple']+
        price_info.price_list['orange']*price_info.quantity_list['orange']+
        price_info.price_list['watermelon']*price_info.quantity_list['watermelon']+
        price_info.price_list['pineapple']*price_info.quantity_list['pineapple']+
        price_info.price_list['pear']*price_info.quantity_list['pear']+
        price_info.price_list['papaya']*price_info.quantity_list['papaya']+
        price_info.price_list['pomegranate']*price_info.quantity_list['pomegranate']
    )
    assert price_info.total_cost_shopping()== expected_total_cost

def test_cost_of_fruits():
    assert price_info.cost_of_fruits('apple',10) == 10 * price_info.price_list['apple']
    assert price_info.cost_of_fruits('orange',5) == 5 * price_info.price_list['orange']



