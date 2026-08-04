library(languageserver)
library(tidyverse)
library(reticulate)

import("xhand")

#pegging for every round
p_pegs <- c(py$game.player_pegs)
c_pegs <- c(py$game.comp_pegs)
#hand score for every round
c_hands <- c(py$comp_handscs)
p_hands <- c(py$player_handscs)

player_data <- tibble(
  Pegging = p_pegs,
  Hand = p_hands
)

computer_data <- tibble(
  Pegging = c_pegs,
  Hand = c_hands
)

#Maxes and Means
mpeg <- select(game_data, Pegging) |>
  max()

avg_p <- pull(game_data, Pegging) |>
  mean()

mhand <- select(game_data, Hand) |>
  max()

avg_h <- pull(game_data, Hand) |>
  mean()

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
