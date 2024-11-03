import numpy as np
import scipy.stats as st


_lambda = 1
med = np.log(2) / _lambda
n = 25
alpha = 0.05
it = 1000

count = 0
for i in range(it):
    X = np.random.exponential(scale = 1 / _lambda, size=n)

    X_mean = np.mean(X)
    hat_m = np.log(2) * X_mean

    sigma = np.log(2) / (_lambda * np.sqrt(n))

    z = st.norm.ppf(1 - alpha / 2)

    lower_bound = hat_m - z * sigma
    upper_bound = hat_m + z * sigma

    print(f'{lower_bound:.4f}<={med:.4f}<={upper_bound:.4f}')

    if lower_bound <= med <= upper_bound:
        count += 1

print(f'covers_med_count={count}, ratio={count / it}')