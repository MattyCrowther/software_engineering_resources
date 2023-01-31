#Set working directory
getwd() #get working directory
setwd("D:/Work/general/R/")

#-------------------------------------------------------------------------------------------------
#CSV
file <- file.path("course_files/9-r-programming-fund-m9-exercise-files/data","01Sample.csv")
my.data <- read.csv(file)
str(my.data)
my.data

#-------------------------------------------------------------------------------------------------
#Tabular importation (Generic way of importing data into tabular format)
file <- file.path("../r_fundementals/course_files/9-r-programming-fund-m9-exercise-files/data","02Sample.txt")
my.data <- read.table(file,
                      header=TRUE,  #Contains header      
                      skip=1, #Skip 1 line
                      colClasses=c("character","factor","numeric","integer","integer"))
str(my.data)
my.data
#-------------------------------------------------------------------------------------------------
#URL
url <- "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
local <- file.path("course_files/9-r-programming-fund-m9-exercise-files/data","03DownloadedFile.data")
download.file(url,local)
my.data <- read.table(local,sep=",")
str(my.data)
#Use RCurl package for advanced scenarios 

#-------------------------------------------------------------------------------------------------
#XML
file <- file.path("course_files/9-r-programming-fund-m9-exercise-files/data","04Sample.xml")
install.packages("XML")
library(XML)
my.data <- xmlToDataFrame(file,
                          colClasses=c("character","integer","integer"),
                          stringsAsFactors=FALSE)
str(my.data)

#-------------------------------------------------------------------------------------------------
#Excel
file <- file.path("course_files/9-r-programming-fund-m9-exercise-files/data","05Sample.xlsx")
install.packages("XLConnect")
library(XLConnect)
my.data <- readWorksheetFromFile(file,
                                 sheet=1,
                                 startRow=2)
str(my.data)
my.data <- transform(my.data, 
                     student.gender = as.factor(student.gender),
                     student.physics.marks = as.integer(student.physics.marks),
                     student.chemistry.marks = as.integer(student.chemistry.marks))                     
str(my.data)
#Other packages : xlsReadWrite, xlsx , gdata 

#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
#Import built in datasets (Data sets which are built into packages)
library(datasets)
data(package="datasets")
data(iris)
str(iris)

#-------------------------------------------------------------------------------------------------
#Import from databases
install.packages("RODBC")
library(RODBC)
connect <- odbcConnect("mysqlconnection")
my.data <- sqlQuery(connect, "SELECT * FROM test.classroom")
my.data
