countries = {'The Netherlands': {'capital': 'Amsterdam','population': 17283008,'continent': 'Europe',},
  'France': {
    'capital': 'Paris',
    'population': 67186638,
    'continent': 'Europe',
  },
  'USA': {
    'capital': 'Washington, D.C.',
    'population': 327167434,
    'continent': 'North America',
  }}

while True:
    What = input("What do you want to do?(exit, add, largest population, continent) -> ")
    if What == 'exit':
        break
    else:
        if What == 'add':
            country = input("Which country? -> ")
            capital = input("What is the capital? -> ")
            population = input("What is the population? -> ")
            continent = input("On which continent is it located? -> ")
            countries.update({str(country):{'capital':str(capital),
                                            'population':int(population),
                                            'continent':str(continent)}})
        elif What == 'continent':
             Whatc = input('What continent?   ')
             if Whatc == 'Europe':
                 for i in countries:
                     max(countries['population'].values())
                    
                     
                         
            
            
            
            
                            
