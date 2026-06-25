library(languageserver)
library(tidyverse)
cc_data <- read_csv("data.csv", show_col_types = FALSE)
?read_csv()
View(cc_data)

#Maxes and Means
mpeg <- select(cc_data, Pegging) |>
  max()

avg_p <- pull(cc_data, Pegging) |>
  mean()

mhand <- select(cc_data, Hand) |>
  max()

avg_h <- pull(cc_data, Hand) |>
  mean()

mpeg
avg_p
mhand
avg_h

.libPaths()

R.version.string
Sys.which("R")
find.package("languageserver")
require(languageserver)
