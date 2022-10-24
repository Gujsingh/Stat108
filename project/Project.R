library(tidyverse)

# potentially useful function: read_csv
house <- read_csv(here::here("data/", "house.csv"))
glimpse(house)

assesements <- read.table("data/school/school1.txt", sep='\t',
                          header=TRUE)
glimpse(assesements)
