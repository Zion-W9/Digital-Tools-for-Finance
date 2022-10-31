library(readr)
library(ggplot2)
data = read.csv("C:/Users/Jillson/OneDrive/UZH/HS22/Digital Tools for Finance/Homework/Digital-Tools-for-Finance/homework/week2/coding environment/coding-environment-exercise.csv", header = TRUE)
Plot <- ggplot(data, aes(x = date, y = value, group = 1)) + geom_point() +
  geom_line()
Plot