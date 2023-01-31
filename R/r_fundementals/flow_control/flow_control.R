#Simple if statement
IsGoodPerformanceByBatch <- function(test.marks) {
  average.marks <- mean(test.marks)
  performance.test <- average.marks >= 75
  print(paste("average marks :",average.marks, "performance.test :",performance.test))
  if(performance.test){
    print("Overall performance of the batch is brilliant")
  }
  print("performance test completed") 
}

IsGoodPerformanceByBatch(test.marks= c( 70L , 75L , 80L,  85L))
IsGoodPerformanceByBatch(test.marks= c( 50L , 55L , 60L,  70L))

#------------------------------------------------------------------------------------------------
#Simple if else statement
IsGoodPerformanceByBatchElse <- function(test.marks) {
  average.marks <- mean(test.marks)
  performance.test <- average.marks >= 75
  print(paste("average marks :",average.marks, "performance.test :",performance.test))
  if(performance.test){
    print("Overall performance of the batch is brilliant")
  }
  else{
    print("Overall performance of the batch is average")
  }
  print("performance test completed") 
}

IsGoodPerformanceByBatchElse(test.marks= c( 70L , 75L , 80L,  85L))
IsGoodPerformanceByBatchElse(test.marks= c( 50L , 60L , 60L,  70L))

#------------------------------------------------------------------------------------------------
#Multiple if-else statement
IsGoodPerformanceByBatchMultIf <- function(test.marks) {
  average.marks <- mean(test.marks)
  print(paste("average marks :",average.marks))
  if(average.marks >= 75) {
    print("Overall performance of the batch is brilliant")
  }
  else if(average.marks >= 60) {
    print("Overall performance of the batch is satisfactory")
  }
  else {
    print("Overall performance of the batch is below average")
  }
  print("performance test completed") 
}

IsGoodPerformanceByBatchMultIf(test.marks= c( 70L , 75L , 80L,  85L))
IsGoodPerformanceByBatchMultIf(test.marks= c( 50L , 60L , 60L,  70L))
IsGoodPerformanceByBatchMultIf(test.marks= c( 50L , 55L , 60L,  60L))

#-------------------------------------------------------------------------------------------------
#Switch statetemt
GetMarksSummary <- function(test.marks,summary.type) {
  result <- switch(summary.type,
                   "mean" = {
                     mean(test.marks)
                   },
                   "median" = {
                     median(test.marks)
                   },
                   "variance" = {
                     var(test.marks)
                   },
                   "Not Implemented"  
  )
  
  #result <- switch(summary.type,
  #                  "mean" = mean(test.marks),
  #                  "median" = median(test.marks), 
  #                  "variance" = var(test.marks),
  #                  "Not Implemented")
  result
}

GetMarksSummary(test.marks= c( 70L , 75L , 80L,  85L),"mean")
GetMarksSummary(test.marks= c( 70L , 75L , 80L,  85L),"median")
GetMarksSummary(test.marks= c( 70L , 75L , 80L,  85L),"variance")
GetMarksSummary(test.marks= c( 70L , 75L , 80L,  85L),"unknown")

#-------------------------------------------------------------------------------------------------
#Vectorized if
test.marks <- c( 70L , 75L , 80L, NA)
test.marks >= 75
ifelse(test.marks >= 75,c("Great","Bravo","Excellent","Congrats"),
       c("Keep it up","Not bad","Just missed","Jusk ok"))
ifelse(test.marks >= 75,"With distinction","Without distinction")
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
#While loop
WriteOnNoteBook <- function(total.page.count)
{
  count <- 0
  while(count < total.page.count){
    count <- count + 1
    print(paste("writing on page number",count))
  }
  print("Page finished")
}

WriteOnNoteBook(total.page.count = 10)

#-------------------------------------------------------------------------------------------------
#For loop
WriteOnNoteBook <- function(total.page.count)
{ 
  for(count in 1:total.page.count){
    print(paste("writing on page number",count))
  } 
  print("Page finished")  
}

WriteOnNoteBook(total.page.count = 10)

#-------------------------------------------------------------------------------------------------
#Applpy function
student.marks <- matrix(c( 70L, 75L, 72L, 80L, 50L,
                           80L, 85L, 60L, 72L, 88L,
                           60L, 70L, 87L, 55L, 90L,
                           85L, 70L, 74L, 86L, 78L ),ncol=5,nrow=4, byrow=TRUE)

rownames(student.marks) <- c("Raj","Rahul","Priya","Poonam")
colnames(student.marks) <- 
  c("Physics","Chemistry","Mathematics", "Biology","History")
student.marks
result <- vector("numeric",length=nrow(student.marks))

apply(student.marks,1,sum) #1 = want to work on rows (True/False value when talking about matrix, try adding 3 get error.)
apply(student.marks,1,max)
apply(student.marks,1,which.max) #Which column student has scored most on.
colnames(student.marks)[apply(student.marks,1,which.max)] #Subsetting but does same as above. (Same but shows name of subject)
apply(student.marks,2,mean) #Based on column
apply(student.marks,2,max)
rownames(student.marks)[apply(student.marks,2,which.max)]
apply(student.marks,1:2,function(x) x +2) #Adds two to each value