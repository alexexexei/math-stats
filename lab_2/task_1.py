import numpy as np
import scipy.stats as st


mu_1, mu_2 = 2, 1
tau = mu_1 - mu_2
sigma2_1, sigma2_2 = 1, 0.5
n_1, n_2 = 25, 25
alpha = 0.05
n = 10000

count = 0
for i in range(n):
    X_1 = np.random.normal(mu_1, sigma2_1, n_1)
    X_2 = np.random.normal(mu_2, sigma2_2, n_2)

    X_1_mean = np.mean(X_1)
    X_2_mean = np.mean(X_2)

    sigma = np.sqrt(sigma2_1 / n_1 + sigma2_2 / n_2)

    z = st.norm.ppf(1 - alpha / 2)

    lower_bound = (X_1_mean - X_2_mean) - z * sigma
    upper_bound = (X_1_mean - X_2_mean) + z * sigma
    
    print(f'{lower_bound:.4f}<={tau}<={upper_bound:.4f}')
    
    if lower_bound <= tau <= upper_bound:
        count += 1

print(f'covers_tau_count={count}, ratio={count / n}')
