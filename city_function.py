def formatted_city_country(city, country, population = ''):
    '''this function returns a neatly formatted city and country'''
    
    if population:
        formatted_name = f'{city.title()}, {country.title()} - population: {population}'
    else:
        formatted_name = f'{city.title()}, {country.title()}'    
    return formatted_name