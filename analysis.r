library(languageserver)
library(tidyverse)
library(dplyr)
cc_data <- read_csv("data.csv", show_col_types = FALSE)
?read_csv()
View(cc_data)

select(cc_data, Pegging) |>
    max() -> mpeg

select(cc_data, Hand) |>
    max() -> mhand

mpeg
mhand
