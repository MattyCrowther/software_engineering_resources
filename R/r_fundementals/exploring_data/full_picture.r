library(datasets) #Load the package
data(iris) #Load data

str(iris) #Structure/ overviews
head(iris) #first 6 values

mean(iris$Sepal.Length)
median(iris$Sepal.Length) #Median = middle value

range(iris$Sepal.Length) #min max value
diff(range(iris$Sepal.Length))

summary(iris$Sepal.Length)
summary(iris)

boxplot(iris$Sepal.Length)
boxplot(iris$Sepal.Length,horizontal = TRUE)
boxplot.stats(iris$Sepal.Length)
boxplot(iris[1:4])

hist(iris$Sepal.Length)
hist(iris$Sepal.Length,main = "Histogram of sepal length",xlab="Sepal Length")

var(iris$Sepal.Length) #Variance
sd(iris$Sepal.Length) #Std deviation

table(iris)
barplot(iris$Species) #All the same as dataset has equal elements
prop.table(table(iris$Species))
prop.table(table(iris$Species)) * 100

#Category wise
install.packages("psych")
library(psych)
describeBy(iris,group = iris$Species)
library(lattice)
histogram(~Sepal.Length|Species,
          data = iris,
          layout=c(1,3),
          col = "black")
boxplot(Sepal.Length~Species,
        data = iris)

