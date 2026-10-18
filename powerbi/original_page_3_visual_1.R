# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset <- data.frame(undefined, undefined.1, undefined.2, undefined.3)
# dataset <- unique(dataset)

# Paste or type your script code here:
library(ggplot2)
library(dplyr)

# Load data from Power BI
df <- dataset

# Filter for two indicators you want to compare
df <- df %>%
  filter(`Series Name` %in% c(
    "Prevalence of HIV, total (% of population ages 15-49)",
    "Antiretroviral therapy coverage (% of people living with HIV)"
  )) %>%
  filter(!is.na(Value))

# Plot both over time by year for the selected country
ggplot(df, aes(x = Year, y = Value, color = `Series Name`, group = `Series Name`)) +
  geom_line(size = 1.2) +
  geom_point(size = 2) +
  facet_wrap(~ `Country Name`) +
  theme_minimal(base_size = 14) +
  labs(
    title = "HIV Prevalence vs ART Coverage Over Time",
    x = "Year",
    y = "Value (%)",
    color = "Indicator"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    legend.position = "bottom"
  )
