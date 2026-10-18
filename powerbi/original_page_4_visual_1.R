# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset <- data.frame(undefined, undefined.1, undefined.2)
# dataset <- unique(dataset)

# Paste or type your script code here:
library(ggplot2)

ggplot(dataset, aes(x = Year, group = Country)) +
  geom_line(aes(y = `GDP growth (annual %)`, color = Country), linetype = "solid") +
  geom_line(aes(y = `GDP per capita growth (annual %)`, color = Country), linetype = "dashed") +
  labs(
    x = "Year",
    y = "GDP Value (%)",
    color = "Country",
    title = "GDP Growth and GDP per Capita Growth"
  ) +
  theme_minimal()

