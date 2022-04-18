import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

def plot_beta_binomial(a, b, n_trials, n_successes, n_steps = 100):
    plt.figure(figsize = (12,8))
    
    xs = np.linspace(0, 1, n_steps)
    
    ## Calculating prior, likelihood, and posterior.
    prior = beta(a, b).pdf(xs)
    likelihood = binom(n_trials, xs).pmf(k=n_successes)
    posterior = prior * likelihood
    
    ## Plotting colored lines here to show prior mode, the maximum likelihood value, and posterior mode.
    plt.vlines([(a - 1) / (a + b - 2), n_successes / n_trials, (a + n_successes - 1) / (a + b + n_trials - 2)],
               ymin = 0,
               ymax = max(max(prior),max(likelihood), max(posterior)), # height of dotted lines
               linestyles = 'dashed',
               colors = ['tab:orange', 'tab:green', 'tab:blue'])
    plt.yticks([])
    
    ## Plotting prior, likelihood, and posterior.
    plt.title("Prior, Likelihood, and Posterior Modes", fontsize = 18)
    plt.xlabel("Values of $p$", fontsize = 16)
    plt.plot(xs, prior, c = 'tab:orange', label="Prior")
    plt.plot(xs, likelihood, c = 'tab:green', label="Likelihood")
    plt.plot(xs, posterior, c = 'tab:blue', label='Posterior')
    plt.legend(loc = 2, fontsize=14);
