from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    jeep_models = cars.get('Jeep',[])
    return ', '.join(jeep_models)


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    lst =[]
    for model_list in cars.values():
        lst.append(model_list[0])
    return lst
        


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    lst =[]
    for model_list in cars.values():
        for models in model_list:
            if grep.lower() in models.lower():
                lst.append(models)
    return sorted(lst)


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    sorted_cars = {}
    for manufacturer, models in cars.items():
        sorted_cars[manufacturer] = sorted(models)
    return sorted_cars