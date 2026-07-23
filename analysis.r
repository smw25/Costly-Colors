library(languageserver)
library(tidyverse)
cc_data <- read_csv("data.csv", show_col_types = FALSE)
#find a way to make it so if the game ends before hand play,
#the -hand values become just NA
?read_csv()
print(cc_data)

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

round <- c("Pegging", "Hand")
avgs <- c(avg_p, avg_h)
maxs <- c(mpeg, mhand)

analyzed <- tibble(
  Rounds = round,
  Average = avgs,
  Maximum = maxs
)

print(analyzed)

write_csv(analyzed, "analyzed.csv")
