#create adult task
class Adult:
    #initialize the constructor
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
    
    #function to see if user can drive
    def can_drive(self):
        #return the information to user
        return f"{self.name} is {self.age} and they are old enough to drive."

#child class that inherits from adult class       
class Child(Adult):
    #get attributes of child from adult class
    def __init__(self, name, age, hair_color, eye_color):
        super().__init__(name, age, hair_color, eye_color)

    def can_drive(self):
        return f"{self.name} is {self.age} and they are too young to drive."
        
        
if __name__ == '__main__':
    
    while True:
        #try to prevent user from inputing incorrect types
        try:
            #initialize variables
            user_name = input("What is your name? ").lower()
            user_age = int(input("How old are you? "))
            hair_color = input("What color is your hair? ").lower()
            eye_color = input("What color are your eyes? ").lower()
            
            #check if user is 18 or over
            if user_age >= 18:
                #enter user arguments
                user = Adult(user_name, user_age, hair_color, eye_color)
            else:
                #else if user is under 18 return child function
                user = Child(user_name, user_age, hair_color, eye_color)
            #print the method
            print(user.can_drive())
            break
        except ValueError:
            print("You have not entered the correct information.")
            