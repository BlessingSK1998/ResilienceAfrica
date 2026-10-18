# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset <- data.frame(undefined, undefined.1, undefined.2, undefined.3)
# dataset <- unique(dataset)

# Paste or type your script code here:# Load required libraries
# Load libraries
library(ggplot2)
library(dplyr)

# Use dataset from Power BI
df <- dataset

# Remove missing values and filter for selected indicator
df <- dplyr::filter(df, !is.na(Value))

# Plot time series: 1 indicator across all countries
ggplot(df, aes(x = Year, y = Value, color = `Country Name`, group = `Country Name`)) +
  geom_line(size = 1.2) +
  geom_point(size = 2) +
  theme_minimal(base_size = 14) +
  labs(
    title = unique(df$`Series Name`),
    x = "Year",
    y = "Value",
    color = "Country"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16),
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  )
