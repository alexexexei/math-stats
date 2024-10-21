import numpy as np
import matplotlib.pyplot as plt

# Параметры
sample_sizes = [10, 50, 100]  # массив объемов выборки
m = 100  # количество выборок для каждого n
b = 0.5  # истинное значение параметра b
threshold = 0.1  # порог для определения отличия

# Для хранения оценок
estimates = {n: [] for n in sample_sizes}

for n in sample_sizes:
    for _ in range(m):
        # Генерация выборки из распределения Лапласа с нулевым сдвигом
        sample = np.random.laplace(loc=0, scale=b, size=n)
        
        # Вычисление оценки b^2
        estimate_b_squared = (1 / (2 * n)) * np.sum(sample ** 2)
        
        # Сохранение оценки
        estimates[n].append(estimate_b_squared)

# Обработка результатов
results = {}
for n in sample_sizes:
    estimates_array = np.array(estimates[n])
    
    # Разница между оценкой и истинным значением
    differences = estimates_array - b**2
    
    # Выборочные характеристики
    mean_difference = np.mean(differences)
    std_difference = np.std(differences)
    count_exceeds_threshold = np.sum(np.abs(differences) > threshold)
    
    results[n] = {
        'mean_difference': mean_difference,
        'std_difference': std_difference,
        'count_exceeds_threshold': count_exceeds_threshold,
        'estimates': estimates_array
    }

# Вывод результатов
for n in sample_sizes:
    print(f"\nОбъем выборки n={n}:")
    print(f"Средняя разница: {results[n]['mean_difference']:.4f}")
    print(f"Стандартное отклонение разницы: {results[n]['std_difference']:.4f}")
    print(f"Количество выборок, которые превышают порог: {results[n]['count_exceeds_threshold']}")

# Визуализация
plt.figure(figsize=(10, 5))

for n in sample_sizes:
    plt.hist(results[n]['estimates'], bins=20, alpha=0.5, label=f'n={n}')

plt.axvline(x=b**2, color='red', linestyle='--', label='Истинное значение b^2')
plt.title('Распределение оценок b^2 для разных объемов выборки')
plt.xlabel(r'$\hat{\theta}^2$')
plt.ylabel('Частота')
plt.legend()
plt.grid()
plt.show()
