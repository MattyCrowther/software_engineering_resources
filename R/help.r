#Help Examples
help(rnorm)
?rnorm

help.search("vector")  
??"vector"

example(rnorm) 

demo()
demo(package = .packages(all.available = TRUE))
demo(package = "graphics") #This is for package
demo(graphics) #This is for particular function

vignette() #Lists all vignettes in attached packages
vignette(package = packages(all.available = TRUE)) #List all vignettes in all installed packages
vignette(package = "parralel") #List all vignettes in parralel package
vignette('parralel',package = 'parralel') # Show vignette for parallel

RSiteSearch("arithmetic mean") #Search on http://search.r-project.org
RSiteSearch("{arithmetic mean}") #Exact search

install.packages("sos") #Install package
library(sos) # Load package
findFn("{arithmetic mean}") # Tabulates the results to see in easier to view format.
findFn("{arithmetic mean}",maxPages = 2)
???"{arithmetic mean}"(2) #Shortcut of above.