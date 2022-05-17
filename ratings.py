"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    # Opening the file
    open_file = open(file)
    restaurant_ratings = {}
    # Giving user 3 choices
    while True:
        try:
            choice = int(input('What would you like to do?\n[1] - See all the ratings\n[2] - Add a new restaurant and rating it\n[3] - Quit\n[4] - Update restaurant rating: '))
        except ValueError:
            continue

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
                    restaurant_ratings[new_rest] = rest_rating
                    break

        # Adding the restaurants to a dictionary 
        if len(restaurant_ratings) == 0:
            restaurant_ratings = {}
        if choice == 1 or choice == 2 or choice == 4:
            for line in open_file:
                line = line.strip()
                restaurants = line.split(":")
                restaurant_ratings[restaurants[0]] = restaurants[1]

            # Sorting the dictionary     
            sorted_restaurants = sorted(restaurant_ratings.items())

            # Printing all the restaurants and its ratings
            if choice == 1:
                for rest, rating in sorted_restaurants:
                    print(f"{rest} is rated {rating}")

        # Updating restaurant rating
        if choice == 4:
            import random
            rest_keys = list(restaurant_ratings.keys())
            random_update = random.choice(rest_keys) 
            print(f'{random_update}')

            while True:
                try:
                    random_rating = int(input('Rating: '))
                except ValueError:
                    continue

                if type(random_rating) == int and 1 <= random_rating <= 5:
                    print(f'The restaurant {random_update} old rating was: {restaurant_ratings[random_update]}. The new rating is: {random_rating}')            
                    restaurant_ratings[random_update] = random_rating
                    break           
           
            
        

get_ratings("scores.txt")
