import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# common separator between unrelated outputs
def print_separate():
    print('----------------')


# calculating the main values
def calculate_print_values(df: pd.Series, name: str):
    mean = df.mean()
    print(f'mean_{name}={mean}')

    var = df.var()
    print(f'var_{name}={var}')

    median = df.median()
    print(f'median_{name}={median}')

    quantile_2d5 = df.quantile(q=2/5)
    print(f'quantile_2/5_{name}={quantile_2d5}')


# plotting basic graphs
def show_graphs(df: pd.Series, name='sample'):
    # the resulting axis will be labeled 0, 1, …, n - 1
    # (not saving original indexes)
    sorted = df.sort_values(ignore_index=True)

    # normalize for proportions (probabilities) instead of freqs
    # sorting by DataFrame column values (not by freqs)
    idx_prob = sorted.value_counts(normalize=True, sort=False)

    # parsing x & y then cumsum for distribution function
    plt.plot(idx_prob.index, idx_prob.values.cumsum())
    plt.title(f'Empirical distribution function of {name}')
    plt.xlabel('battery_power')
    plt.ylabel('probability')
    plt.grid()
    plt.gcf().set_size_inches(10, 5)
    plt.show()

    # Sturges' rule
    n = np.int64(1 + np.floor(3.322 * np.log10(df.shape[0])))
    plt.hist(df, bins=n)
    plt.title(f'Histogram of {name}')
    plt.xlabel('battery_power')
    plt.ylabel('count')
    plt.grid()
    plt.gcf().set_size_inches(10, 5)
    plt.show()

    plt.boxplot(df)
    plt.title(f'Boxplot of {name}')
    plt.ylabel('battery_power')
    plt.grid()
    plt.gcf().set_size_inches(10, 5)
    plt.show()


# reading the table
url='https://drive.google.com/file/d/1O4rFr9xg9aFmkjx4-hl_XOc5O9q65_EW\
    /view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

# how many models can you insert 2 SIM cards into?
dual_sim_count = df['dual_sim'].sum()
print(f'dual_sim_count={dual_sim_count}')

# how many models support 3-G?
three_g_count = df['three_g'].sum()
print(f'three_g_count={three_g_count}')

# what is the highest number of cores a processor has?
max_cores = df['n_cores'].max()
print(f'max_cores={max_cores}')

print_separate()

# the entire sample
all_battery = df['battery_power']
calculate_print_values(all_battery, name='all_battery')

print_separate()

# selection with the condition of wifi availability
wifi_table = df[df['wifi']==1]
wifi_battery = wifi_table['battery_power']
calculate_print_values(wifi_battery, name='wifi_battery')

print_separate()

# selection with the condition of wifi unavailability
nowifi_table = df[df['wifi']==0]
no_wifi_battery = nowifi_table['battery_power']
calculate_print_values(no_wifi_battery, name='no_wifi_battery')

show_graphs(all_battery, name='all_battery')
show_graphs(wifi_battery, name='wifi_battery')
show_graphs(no_wifi_battery, name='no_wifi_battery')
