"""Write a class called MovieTicket that inherits from the Ticket class of the previous problem. It
should have the following (in addition to all that it gets from the Ticket class):
• A string field called movie_name
• A constructor that sets movie_name as well as cost and time
• Override the __str__() method so that it returns a string of the form MovieTicket(<cost>, <time>, <name<),
where <cost>, <time>, and <name> are replaced with the values of the class’s fields.
• A method called afternoon_discount() that returns a discount of 10 (standing for 10%) if the
ticket time falls in the range from 12:00 to 17:59 and 0 otherwise.
Test the class by creating a MovieTicket item, printing it, and calling the afternoon_discount()
and is_evening_time() methods."""
class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time
    
    def is_evening_time(self):
        hour = int(self.time.split(':')[0])
        return hour >= 18  


class MovieTicket(Ticket):
    def __init__(self, movie_name, cost, time):
        super().__init__(cost, time)
        self.movie_name = movie_name
    
    def __str__(self):
        return f"MovieTicket({self.cost}, {self.time}, {self.movie_name})"
    
    def afternoon_discount(self):
  
        hour = int(self.time.split(':')[0])
        if 12 <= hour < 18:
            return 10  
        else:
            return 0
    
    def is_evening_time(self):
        return super().is_evening_time() 

if __name__ == "__main__":
    
    movie_ticket = MovieTicket("Avengers: Endgame", 15.50, "15:30")
    
    print(movie_ticket)
    
    discount = movie_ticket.afternoon_discount()
    print(f"Afternoon discount: {discount}%")
    
    is_evening = movie_ticket.is_evening_time()
    print(f"Is evening time: {is_evening}")
