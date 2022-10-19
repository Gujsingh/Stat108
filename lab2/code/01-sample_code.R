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
  scale_fill_manual(values = c("mediumorchid1", "lightyellow3", "salmon3", "salmon2", "slateblue4", "yellowgreen", "lawngreen", "tan", "ivory", "khaki2", "chocolate", "blue1", "darkkhaki", "forestgreen", "firebrick3", "goldenrod1", "grey0", "lightblue1", "honeydew2", "olivedrab", "ghostwhite")) +
  geom_errorbar(aes(ymin = sum - 2, ymax = sum + 3)) +
  annotate("text", x = 14, y = 51, label = "This is the \n highest bar!", size = 2) +
  theme_dark() +
  labs(x = "X-axis",
       y = "Y-axis",
       title = "The most beautiful plot ever")

ggsave(here::here("figures", "sample-plot.jpg"), width = 7, height = 4, dpi = 150)


