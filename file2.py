with open('population.txt', 'r') as file:
   
    for line in file:
        
        country_name = parts[0]
        population = int(parts[1].strip())  
        
        if country_name.startswith('G') and population >= 500000:
            
            print(country_name)
