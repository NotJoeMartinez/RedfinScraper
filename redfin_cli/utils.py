import pandas as pd

def get_cities_by_state(data_path, state):
    """
    Get all cities in a state
    """
    data = pd.read_csv(data_path)

    cities = data[data['state'] == state]['primary_city'].unique()

    res = []
    for city in cities.tolist():
        res.append((city, state))
    
    print(len(res))
    return res
