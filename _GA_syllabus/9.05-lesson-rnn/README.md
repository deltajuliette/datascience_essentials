# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Recurrent Neural Networks

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Intro to RNNs | Slide Deck | [Link](./rnn.pdf)
| Coding Example | RNN walkthrough | [Link](./starter-code.ipynb)|

## Learning Objectives

*After this lesson, students will be able to:*

1. Preprocess sequence data for RNN modeling
2. Design, train and evaluate an RNN model
3. Create a model that predicts the price of Apple's (AAPL) stock

## Lesson Outline

> **Total Time: 90 mins**

I. **Intro to RNNs** (30 minutes total)
- What types of datasets are ideal for RNN models
- How `TimeseriesGenerator` prepares your sequence data for modeling
- Overview of RNN architecture
- The shortcomings of early RNN models
- How LSTM/GRU networks solve the problem of vanishing gradients

II. **RNN walkthrough** (60 minutes total)
- Load in AAPL stock prices + SEC filings
- Train/test split for time series data
- Use `TimeseriesGenerator` to prep our data for modeling
- Design a basic RNN network using GRU layers

## OPTIONAL: Resources for Practice and Learning

*For supplemental reading material on this topic, check out the following resources:*
- Andrew Ng's Coursera course on [Sequence Models](https://www.coursera.org/learn/nlp-sequence-models)
- Ava Soleimany's [video on RNNs](https://www.youtube.com/watch?v=SEnXr6v2ifU)
- [*The Unreasonable Effectiveness of Recurrent Neural Networks*](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- A good [explanation of RNNs](https://explained.ai/rnn/index.html)
- Blog on the [Vanishing Gradient Problem](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484)
- How LSTMs solve the [vanishing gradient problem](https://medium.com/datadriveninvestor/how-do-lstm-networks-solve-the-problem-of-vanishing-gradients-a6784971a577)
- A blog on the [basics of RNNs](https://medium.com/towards-artificial-intelligence/whirlwind-tour-of-rnns-a11effb7808f) 
