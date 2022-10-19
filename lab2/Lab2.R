library(tidyverse)

# potentially useful function: read_csv
sweaters <- read_csv(here::here("data/use_this_data", "holiday_sweaters-2020-12-15-clean.csv")) %>% 
  filter(hs_tf == "Yes") %>% 
  # potentially useful function: separate colors column into rows
  separate_rows(colors, sep = c(", ")) %>% 
  group_by(colors) %>% 
  summarize(sum = length(colors))

ggplot(sweaters, aes(x = colors, y = sum)) +
  geom_col(aes(color = colors, fill = colors)) +
  geom_point(size = 10) + 
  theme(plot.background = element_rect(fill = "lightyellow"))+
  geom_vline(xintercept = 1)+
  geom_vline(xintercept = 2)+
  geom_vline(xintercept = 3)+
  geom_vline(xintercept = 4)+
  geom_vline(xintercept = 5)+
  geom_vline(xintercept = 6)+
  geom_text(label=rownames(sweaters), nudge_x = 0.40, nudge_y=50, size = 20, color = "Blue") + 
  labs(title = "Colors with lines",
           subtitle = "(black-pink)",
           caption = "Colors here or there",
           tag = "Color tags",
           x = "Many different colors ",
           y = "How many colors are there???",
           colour = "Colors"
           + theme_gray(base_size = 14))

ggsave(here::here("figures", "sample-plot.jpg"), width = 7, height = 4, dpi = 150)


