#create course class
class Course:
    #class attributes
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    #define class function to return contact details
    def contact_details(self):
        return f"Please contact us by visiting", self.contact_website
    
    #define class function to return loctal details
    def print_location(self):
        return f"The location of the course is Woodstock, Cape town. "
        
#child class inherited from course class
class OOPCourse(Course):
    #contructor function
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
    
    #define class function to return trainer details    
    def trainer_details(self):
        return f"This course is about {self.description}, and the teacher is {self.trainer}."
    
    #define class function to return course ID number
    def show_course_id(self):
        return f"The ID  of this course is #12345."

#defin class object
course_1 = OOPCourse()

#print results
print("\n", course_1.contact_details(), "\n")
print(course_1.trainer_details(), "\n")
print(course_1.show_course_id())