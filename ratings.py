"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    # Opening the file
    open_file = open(file)
    restaurant_ratings = {}
    # Giving user 3 choices
    while True:
        choice = int(input('What would you like to do?\n[1] - See all the ratings\n[2] - Add a new restaurant and rating it\n[3] - Quit '))
        
        # Exiting the function
        if choice == 3:
            return "Goodbye"
        # Adding a new Restaurant rating
        if choice == 2:
            new_rest = input('Restaurant: ').strip().title()
            while True:
                try:
                    rest_rating = int(input('Rating: '))
                except ValueError:
                    continue    
                if type(rest_rating) == int and 1 <= rest_rating <= 5:
                    restaurant_ratings = {new_rest: rest_rating}
                    break

        # Adding the restaurants to a dictionary 
        if len(restaurant_ratings) == 0:
            restaurant_ratings = {}
        if choice == 1:
            for line in open_file:
                line = line.strip()
                restaurants = line.split(":")
                restaurant_ratings[restaurants[0]] = restaurants[1]

            # Sorting the dictionary     
            sorted_restaurants = sorted(restaurant_ratings.items())

            # Printing all the restaurants and its ratings
            for rest, rating in sorted_restaurants:
                print(f"{rest} is rated {rating}")
                    
            
        

get_ratings("scores.txt")
