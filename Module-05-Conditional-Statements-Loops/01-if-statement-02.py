# Simple if and if..else statements
# Better Example

movie1_tickets_available = 3
movie2_tickets_available = 5
movie3_tickets_available = 7

movie_selected = input('Which movie do you want to watch? ')
count = input('How many tickets do you want? ')

if movie_selected == "movie1" and int(count) <= movie1_tickets_available:
    print("Here are your tickets for the move - {}".format(movie_selected))
else:
    print("The requested number of tickets are not available!")

if movie_selected == "movie2" and int(count) <= movie2_tickets_available:
    print("Here are your tickets for the move - {}".format(movie_selected))
else:
    print("The requested number of tickets are not available!")

if movie_selected == "movie3" and int(count) <= movie3_tickets_available:
    print("Here are your tickets for the move - {}".format(movie_selected))
else:
    print("The requested number of tickets are not available!")



