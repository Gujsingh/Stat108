library(tidyverse)

sweaters <- read_csv(here::here("data/use_this_data", "holiday_sweaters-2020-12-15-clean.csv")) %>% 
  filter(hs_tf == "Yes") %>% 
  # potentially useful function: separate colors column into rows
  separate_rows(colors, sep = c(", ")) %>% 
  group_by(sweater) %>% 
  mutate(sum = length(colors)) %>% 
  rownames_to_column("values")

ggplot(sweaters, aes(x = sweater, y = sum)) +
  geom_point(aes(color = colors)) +
  labs(x = "Entry", 
       y = "Total number of colors") +
  facet_wrap(~sparkly) +
  theme(strip.background = element_rect(fill = "blue"),
        plot.background = element_rect(fill = "pink"),
        legend.background = element_rect(fill = "orange"))

ggsave(here::here("figures/an-plot.jpg"), width = 7, height = 4, dpi = 150)
