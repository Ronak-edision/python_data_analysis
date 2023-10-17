class Student():
    
    
    def __init__(self,  DoB, studentName, courseDuration, tuitionFee):
        self.__DoB=DoB
        self.__studentName=studentName
        self.__courseDuration=courseDuration
        self.__tuitionFee=tuitionFee

        self.__enrollmentID=0
        self.__courseName=''
        self.__dateOfEnrollment=''

    #getter methods
    def getEnrollmentID(self):
        return self.__enrollmentID
    
    def getDoB(self):
       return self.__DoB
    
    def getCourseName(self):
       return self.__courseName
    
    def getStudentName(self):
       return self.__studentName
    
    def getDateOfEnrollment(self):
       return self.__dateOfEnrollment
    
    def getCourseDuration(self):
       return self.__courseDuration
    
    def getTuitionFee(self):
       return self.__tuitionFee
    
    #setter methods

    def setEnrollmentID(self, EnrollmentID):
       self.__enrollmentID=EnrollmentID

    def setDoB(self, DoBirth):
       self.__DoB=DoBirth
    
    def setCourseName(self,CourseName):
        self.__courseName=CourseName
    
    def setStudentName(self,StudentName):
        self.__studentName=StudentName
    
    def setDateOfEnrollment(self,DateOfEnrollment):
        self.__dateOfEnrollment=DateOfEnrollment
    
    def setCourseDuartion(self,CourseDuration):
        self.__courseDuration=CourseDuration
    
    def setTuitionFee(self,TuitionFee):
        self.__tuitionFee=TuitionFee

    def display(self):
        print("Student Information:")
        

        print(f"Enrollment ID: {self.getEnrollmentID()}")
        #print(f"Enrollment ID: {self.__enrollmentID}")

        print(f"Date of Birth: {self.getDoB()}")
        print(f"Student Name: {self.getStudentName()}")

        if self.getCourseName():
            print(f"Course Name: {self.getCourseName()}")
        else:
            print("Course Name: Not available")

        if self.getDateOfEnrollment():
            print(f"Date of Enrollment: {self.getDateOfEnrollment()}")
        else:
            print("Date of Enrollment: Not available")

        if self.getCourseDuration():
            print(f"Course Duration: {self.getCourseDuration()} months")
        else:
            print("Course Duration: Not available")

        if self.getTuitionFee():
            print(f"Tuition Fee: ${self.getTuitionFee()}")
        else:
            print("Tuition Fee: Not available")

        if self.getCourseDuration() and self.getDateOfEnrollment():
            years_enrolled = int(self.getCourseDuration()) / 12
            print(f"Years Enrolled: {years_enrolled:.2f}")
        else:
            print("Years Enrolled: Not available")


student= Student("1990","John Doe",24,5000)
"""student.setCourseName("AI")
student.setEnrollmentID(1234)
student.setDateOfEnrollment("2023")"""
student.setEnrollmentID(111)
student.display()

class Regular(Student):
    def __init__(self, enrollmentID, DoB, studentName, courseDuration, tuitionFee, courseName, dateOfEnrollment,numOfModules,numOfCreditHours,daysPresent ):
        
        # Call the superclass (Student) constructor with four parameters
        super().__init__( DoB, studentName, courseDuration, tuitionFee)

        # Call the parent class mutator methods with the corresponding parameters
        self.setEnrollmentID(enrollmentID)
        self.setCourseName(courseName)
        self.setDateOfEnrollment(dateOfEnrollment)

        # Assign number of modules, number of credit hours, and days present with the parameter values
        self.__numOfModules= numOfModules
        self.__numOfCreditHours= numOfCreditHours
        self.__daysPresent=daysPresent

        self.__isGrantedScholarship= False

    def getNumOfModules(self):
        return self.__numOfModules
    
    def getNumOfCreditHour(self):
        return self.__numOfCreditHours
    
    def getDaysPresent(self):
        return self.__daysPresent
    
    def getIsGrantedScholarship(self):
        return self.__isGrantedScholarship
    
    def presentPercentage(self, daysPresent):
        percentage= (( daysPresent)/(self.getCourseDuration()*30))*100
        if(percentage>=80 and percentage<=100):
            self.__isGrantedScholarship=True
            return "A"
        
        elif 60 <= percentage < 80:
            return "B"
        elif 40 <= percentage < 60:
            return "C"
        elif 20 <= percentage < 40:
            return "D"
        else:
            return "E"
        
    def grantCertificate(self,courseName, enrollmentId , dateofEnrollement):
        if self.getIsGrantedScholarship():
            print("Scholarship has been granted")

    def display(self):
        super().display()# calls display from student class
        print("the numOfModules is"+str(self.getNumOfModules()))
        print("the num of credit hour is"+str(self.getNumOfCreditHour()))
        print("the days present is"+str(self.getDaysPresent()))


"""regular1= Regular( 321, "2003", "studentName", 4, 129090, "AI", "2023",6,3,120 )
regular1.presentPercentage(120)
regular1.grantCertificate("AI",123,"2023")
#
# regular1.display()"""

class Dropout(Student):
    def __init__(self,dateOfBirth,studentName, courseDuration, tuitionFee, numOfRemainingModules,numOfMonthsAttended , dateOfDropout):
        super().__init__(dateOfBirth,studentName, courseDuration, tuitionFee)

        self.__numOfRemainingModules=numOfRemainingModules
        self.__numOfMonthsAttended=numOfMonthsAttended
        self.__dateOfDropout=dateOfDropout
        self.__remainingAmount=0
        self.__hasPaid=False

        # Call the parent class mutator methods for enrollment id, course name, and date of enrollment
        self.set_enrollment_id(0)  # Enrollment ID is initialized to 0 for dropouts
        self.set_course_name("")    # Course name is initialized to an empty string for dropouts
        self.set_date_of_enrollment("")  # Date of enrollment is initialized to an empty string for dropouts

    # Accessor methods for the attributes
    def get_num_of_remaining_modules(self):
        return self.__numOfRemainingModules

    def get_num_of_months_attended(self):
        return self.__numOfMonthsAttended

    def get_date_of_dropout(self):
        return self.__dateOfDropout

    def get_remaining_amount(self):
        return self.__remainingAmount

    def get_has_paid(self):
        return self.__hasPaid
    
    def billsPayable(self,courseDuration,numOfMonthsAttened):
        amount=(self.getCourseDuration-self.__numOfMonthsAttended)*self.getTuitionFee
        if amount==0:
            self.__hasPaid=True
    def removeStudent(self):
        if self.hasPaid:
            # Clear student information
            self.setDoB('')
            self.setCourseName('')
            self.setStudentName('')
            self.setDateOfEnrollment('')
            self.setCourseDuration(0)
            self.setTuitionFee(0)
            self.dateOfDropout = ''
            self.numOfRemainingModules = 0
            self.numOfMonthsAttended = 0
            self.remainingAmount = 0
            self.setEnrollmentID(0)

            # Display message
            print("Student information removed.")
        else:
            print("All bills not cleared.")




