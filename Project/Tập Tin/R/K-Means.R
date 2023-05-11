library(stats)
library(dplyr)
library(ggplot2)
library(ggfortify)

data <- read.csv("E:/Data Mining/Project/ThoiQuenMuaSam.csv")

wssplot <- function(data, nc =15, seed = 1234)
{
  wss <- (nrow(data)-1)*sum(apply(data, 2, var))
  for (i in 2:nc){
    set.seed(seed)
    wss[i] <- sum(kmeans(data, centers = i)$withinss)}
  plot(1:nc, wss, type = "b", xlab = "Number of Clusters", 
       ylab = "within groups sum of squares")
}

wssplot(data)

KM = kmeans(data,5)

autoplot(KM,data, frame = TRUE, main = "K-Means Clustering")

KM$centers
