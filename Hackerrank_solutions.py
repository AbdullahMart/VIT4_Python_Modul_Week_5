
#Questions 1:
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName,idNumber)
        self.scores= scores
        
        
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate (self):
        sum=0
        for score in scores:
            sum += score
        average =sum /len(scores)
        
        if average < 40:
            return "T"
        elif average <55:
            return "D"
        elif average <70:
            return "P"
        elif average < 80:
            return "A"
        elif average <90:
            return "E"
        else:
            return "O"
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

#Questions 2:
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
        
         
        
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
        
        
    def __mul__(self, no):
        r=self.real*no.real-self.imaginary*no.imaginary
        i=self.real*no.imaginary+self.imaginary*no.real
        return Complex(r,i)

    def __truediv__(self, no):
        d=no.real**2+no.imaginary**2
        n=self*Complex(no.real,-1*no.imaginary)
        return Complex(n.real/d,n.imaginary/d)

    def mod(self):
        d=self.real**2+self.imaginary**2
        return Complex(math.sqrt(d),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':