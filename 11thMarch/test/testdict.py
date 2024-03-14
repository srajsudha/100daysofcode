from nested_data_structure import get_all_jeeps, get_first_model_each_manufacturer, get_all_matching_models, sort_car_models

def test_get_all_jeeps():
    Expected_value = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    assert Expected_value ==get_all_jeeps()
    assert type(get_all_jeeps())==str

def test_first_model():
    Expected_value =['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert Expected_value == get_first_model_each_manufacturer()

def test_all_matching_models():
    expected = ['Trailblazer', 'Trailhawk']
    assert expected == get_all_matching_models()

def test_sort_car_models():
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    actual = sort_car_models()
    assert actual == expected