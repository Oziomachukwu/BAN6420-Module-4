# Load necessary libraries
library(ggplot2)
library(dplyr)  # For data manipulation

# Prompt the user for the directory path
directory_path <- readline(prompt = "Please enter the directory path: ")

# Set the working directory to the user-provided path
setwd(directory_path)

# Confirm the working directory has been set
cat("Working directory has been set to:", getwd(), "\n")

# Read the dataset
df <- read.csv("netflix_data_cleaned.csv", stringsAsFactors = FALSE)  # Read without factors


# Convert 'rating' to a factor
df$rating <- as.factor(df$rating)

# Create bar plot for ratings distribution
ggplot(df, aes(x = rating, fill = rating)) +
  geom_bar() +
  scale_fill_manual(values = c("#E50914","#E50910","#E50908","#E50904","#E50900","#E50920","#E50926","#E50932","#E50936","#E50940","#E50944","#E50948","#E50952","#E50956","#E50960")) +  #  red color scheme
  theme_minimal() +
  labs(title = "Distribution of Content Ratings on Netflix",
       x = "Rating", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels

