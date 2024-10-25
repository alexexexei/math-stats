import numpy as np
import matplotlib.pyplot as plt


# common separator between unrelated outputs
def print_separate():
    print('----------------')


n_list = [10, 100, 1000]  # list of sample sizes
m = 100  # number of samples for each n
theta = 0.5  # true value of the scaling parameter
delta = 0.1  # threshold for determining the difference
hat_theta2_dict = {n: [] for n in n_list} # dictionary (key-val) for storing estimates

# for each n generating m samples and calculating estimates
for n in n_list:
    for i in range(m):
        # generating a sample from a Laplace distribution with zero bias
        sample = np.random.laplace(loc=0, scale=theta, size=n)
        
        # calculating hat_theta^2 accroding to the derived formula
        hat_theta2 = (1 / (2 * n)) * np.sum(sample ** 2)
        hat_theta2_dict[n].append(hat_theta2)

# processing results
results = {}
for n in n_list:
    hat_theta2_arr = np.array(hat_theta2_dict[n])
    
    # difference between estimate and true value
    bias = hat_theta2_arr - theta**2
    
    # sample characteristics
    mean_bias = np.mean(bias)
    var_bias = np.var(bias)
    biased_count = np.sum(np.abs(bias) > delta) # Number of samples that exceed the threshold
    
    results[n] = {
        'mean_bias': mean_bias,
        'var_bias': var_bias,
        'biased_count': biased_count,
        'hat_theta2_arr': hat_theta2_arr
    }

# results output
print(f"m={m}")
for n in n_list:
    print_separate()
    print(f"n={n}")
    print(f"mean_bias: {results[n]['mean_bias']:.4f}")
    print(f"var_bias: {results[n]['var_bias']:.4f}")
    print(f"biased_count: {results[n]['biased_count']}")

# visualisation
plt.figure(figsize=(10, 5))

for n in n_list:
    plt.hist(results[n]['hat_theta2_arr'], 
             bins=np.int64(np.floor(1 + 3.322 * np.log10(n))), # Sturges' rule
             alpha=0.5, 
             label=f'n={n}')

plt.axvline(x=theta**2, color='red', linestyle='--', label=r'true value of $\theta^2$')
plt.title(r'Distribution of $\theta^2$ estimates for different sample sizes')
plt.xlabel(r'$\hat{\theta}^2$')
plt.ylabel('count')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.boxplot([results[n]['hat_theta2_arr'] for n in n_list], labels=n_list)
plt.title(r'Boxplot of $\theta^2$ estimates for different n')
plt.ylabel(r'$\hat{\theta}^2$')
plt.xlabel('sample size n')
plt.grid()
plt.show()
