#A list but only contain same class.
student.physics.marks <- c( 70L , 75L , 80L,  85L)
student.chemistry.marks <- c(60L, 70L, 85L, 70L)
student.marks <-rbind(student.physics.marks , student.chemistry.marks) #Row bind - Make matrix by params as rows.
student.marks
student.marks <-cbind(student.physics.marks , student.chemistry.marks) #Column bind - Make matix by params as column
student.marks
rownames(student.marks) <- c("Raj","Rahul","Priya","Poonam") #Set row names
student.marks
str(student.marks)
student.marks <- matrix(c( 70L , 75L , 80L,  85L, 60L, 70L, 85L, 70L),ncol=2,nrow=4) #Alt way of making matrix.
student.marks
student.marks <- matrix(c( 70L , 75L , 80L,  85L, 60L, 70L, 85L, 70L),ncol=4,nrow=2
                        ,byrow=TRUE)
student.marks

student.marks <-cbind(student.physics.marks , student.chemistry.marks) #Column bind - Make matix by params as column
rownames(student.marks) <- c("Raj","Rahul","Priya","Poonam") #Set row names
student.marks
#Subsetting: Extract element(s) from matrix
student.marks[,] #row number,column number
student.marks[2,2] 
student.marks[2,]
student.marks[,2]
student.marks[1:3,]
student.marks[c(1,3),]
student.marks[c(T,F,F,T),]

#summary
student.marks
rowSums(student.marks) #Row wise sum
colSums(student.marks) #Column wise sum
colMeans(student.marks) #Column wise mean
