"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    # Opening the file
    open_file = open(file)

    # Adding a new Restaurant rating
    new_rest = input('Restaurant: ').strip().title()
    while True:
        try:
            rest_rating = int(input('Rating: '))
        except ValueError:
            continue    
        if type(rest_rating) == int and 1 <= rest_rating <= 5:
            break

    # Adding the restaurants to a dictionary 
    restaurant_ratings = {new_rest: rest_rating}
    for line in open_file:
        line = line.strip()
        restaurants = line.split(":")
        restaurant_ratings[restaurants[0]] = restaurants[1]

    # Sorting the dictionary     
    sorted_restaurants = sorted(restaurant_ratings.items())

    # Printing all the restaurants
    for rest, rating in sorted_restaurants:
        print(f"{rest} is rated {rating}")
            
    
    

get_ratings("scores.txt")
