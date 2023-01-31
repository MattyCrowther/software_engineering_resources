# Deploying to Production
install.packages("shiny")
# Load shiny
library(shiny)

# Create a UI
ui <- fluidPage("Hello World!")

# Create a server
server <- function(input, output) {}

# Create a shiny app
shinyApp(
  ui = ui,
  server = server)
