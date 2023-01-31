GetTotalMarks <- function(quiz.marks, viva.marks, assignment.marks = 5L,...) {
  
  total.marks <- quiz.marks + viva.marks + assignment.marks + sum(...) 
  total.marks
}
#--------------------------------------------------------------------------------------
#Basic Function
student.physics.quiz.marks <- c(70L, 75L, 80L, 85L)
student.physics.viva.marks <- c(7L, 5L, 8L, 6L)
student.physics.total.marks <- GetTotalMarks(student.physics.quiz.marks,
                                             student.physics.viva.marks)
student.physics.total.marks

student.chemistry.quiz.marks <- c(60L, 70L, 85L, 70L)
student.chemistry.viva.marks <- c(8L, 4L, 7L, 9L)
student.chemistry.total.marks <- GetTotalMarks(student.chemistry.quiz.marks,
                                               student.chemistry.viva.marks)
student.chemistry.total.marks
#--------------------------------------------------------------------------------------
#Default value 
GetTotalMarks(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L))
GetTotalMarks(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L), 
              assignment.marks = c(2L, 1L, 3L, 4L))
#--------------------------------------------------------------------------------------
#Optional Arguments.
GetTotalMarks(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L), 
              assignment.marks = c(2L, 1L, 3L, 4L), creativity.marks = 2)
GetTotalMarks(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L), 
              assignment.marks = c(2L, 1L, 3L, 4L), creativity.marks = 2,
              attendence.marks = 3)
#--------------------------------------------------------------------------------------
#Lazy evaluation - extra.marks is only used when it is first called so this code is acceptible.
GetTotalMarksWithLazyEval <- function(quiz.marks, viva.marks, extra.marks = average.viva.marks) {  
  average.viva.marks <- mean(viva.marks)
  total.marks <- quiz.marks + viva.marks + extra.marks
  total.marks
}

GetTotalMarksWithLazyEval(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L))
#--------------------------------------------------------------------------------------
#Multiple Return Values - Cannot actually return two values but can create named list and return.
GetMarksSummaryMultipleReturns <- function(quiz.marks, viva.marks) {  
  total.marks <- quiz.marks + viva.marks 
  avg.marks <- mean(total.marks)
  return(list(total = total.marks,average = avg.marks))
}

GetMarksSummaryMultipleReturns(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L))
#--------------------------------------------------------------------------------------
#Functions as objects - Functions are first class objects.
GetTotalMarksFAO <- function(quiz.marks,viva.marks){
  total.marks <- quiz.marks + viva.marks
  total.marks
}
#01 Look into them
GetTotalMarksFAO #return function itself
formals(GetTotalMarksFAO) #Access args
body(GetTotalMarksFAO) #access body

#02Assign them
MyGetTotalMarksFAO <- GetTotalMarksFAO
MyGetTotalMarksFAO

#03 Use them as args to another func
#Pass func as arg in do.call func (do.call is just another way of calling something.)
do.call(GetTotalMarksFAO,list(quiz.marks = c(07L,75L,80L,85L),viva.marks = c(07L,75L,80L,85L)))
#--------------------------------------------------------------------------------------
#Using anonymous function
do.call(function(quiz.marks, viva.marks) {
  quiz.marks + viva.marks 
},list(quiz.marks = c(70L, 75L, 80L, 85L), viva.marks = c(7L, 5L, 8L, 6L)))

