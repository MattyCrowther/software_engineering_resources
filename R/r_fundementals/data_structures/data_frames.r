#Data frames fundementally is a list where each element is a vector or equal length.

student.names <- c("Raj","Rahul","Priya","Poonam")
student.weights <- c( 60.5, 72.5 , 45.2,  47.5)
student.genders <- factor(c("Male","Male","Female","Female"))
student.physics.marks <- c( 70L , 75L , 80L,  85L)
student.chemistry.marks <- c(60L, 70L, 85L, 70L)
#Create data frame
students <- data.frame(student.names,student.weights,student.genders,
                       student.physics.marks, student.chemistry.marks)
typeof(students)
students
str(students)

#Use stringAsFactors = FALSE , to avoid converstion of character vector to factor
students <- data.frame(student.names,student.weights,student.genders,
                       student.physics.marks, student.chemistry.marks, 
                       stringsAsFactors = FALSE)
str(students)
#Subsetting: Extract element(s) in data frame
students[1] #Single brackets [] return element of same type
typeof(students[1])  
students[[1]] #double brackets [[]] return the object in its own type
typeof(students[[1]])
students[["student.names"]] #double brackets [[]] return the object in its own type
typeof(students[["student.names"]])
students$student.names #$ return the object in its own type
typeof(students$student.names)
students[1:3] #Remeber 1 index not 0
students[c("student.physics.marks","student.chemistry.marks")]
students
students[1,2] #Row number, Column number
students[1:3,1:2]
students[c(1,2),c(1,3)] #Extract row 1,2 and column 1,3
students[,1] #All values in column 1
students[1,] #All values in row 1
students[c(T,F,T,F),] #Give me rows where true.
students[student.genders == "Male",]
students[student.physics.marks >= 75,]

