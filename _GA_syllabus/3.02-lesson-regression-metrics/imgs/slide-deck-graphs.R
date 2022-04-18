library(tidyverse)

# Violation of L assumption
set.seed(123)
x <- seq(1, 1.5, length.out = 30)
y <- exp(x)
df <- data.frame(x = x, y = y)

plot(x, y)

m <- lm(y ~ x, data = df)
df$yhat <- predict(m, df)
df$e <- df$y - df$yhat

p1 <- ggplot(df, aes(x, y)) +
  geom_point(size = 0.5) + 
  geom_smooth(method = "lm", se = FALSE, color = "red", size = 0.5) +
  theme_bw() +
  labs(x = "", y = "") +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank()
  )

ggsave("l-violated.png", p1, dpi = 192,
       height = 4, width = 4, units = "in")

p2 <- ggplot(df, aes(yhat, e)) +
  geom_point(size = 0.5) +
  geom_hline(yintercept = 0, size = 0.5, color = "red") +
  theme_bw() +
  labs(x = "", y = "") +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank()
  )

ggsave("l-violated-resids.png", p2, dpi = 192,
       height = 4, width = 4, units = "in")

# Violation of E assumption
set.seed(125)
n <- 100
x <- seq(4, 6, length.out = n)
logy <- 2 + 0.7*x + rnorm(n, 0, 0.3)
y <- exp(logy)

df <- data.frame(x, y, logy)
plot(x, y)

m <- lm(y ~ x, data = df)
df$yhat <- predict(m, df)
df$e <- df$y - df$yhat

p3 <- ggplot(df, aes(x, y)) +
  geom_point(size = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "red", size = 0.5) +
  theme_bw() +
  labs(x = "", y = "") +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank()
  )
ggsave("e-violated.png", p3, dpi = 192,
       height = 4, width = 4, units = "in")

p4 <- ggplot(df, aes(yhat, e)) +
  geom_point(size = 0.5) +
  geom_hline(yintercept = 0, size = 0.5, color = "red") +
  theme_bw() +
  labs(x = "", y = "") +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank()
  )

ggsave("e-violated-resid.png", p4, dpi = 192,
       height = 4, width = 4, units = "in")

m2 <- lm(logy ~ x, data = df)
df$yhat2 <- predict(m2, df)
df$e2 <- df$yhat2 - df$logy

p5 <- ggplot(df, aes(yhat2, e2)) +
  geom_point(size = 0.5) +
  geom_hline(yintercept = 0, size = 0.5, color = "red") +
  theme_bw() +
  labs(x = "", y = "") +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank()
  )

ggsave("e-violated-resid-log.png", p5, dpi = 192,
       height = 4, width = 4, units = "in")
