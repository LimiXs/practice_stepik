import pandas as pd
import numpy as np
from IPython.display import display

# Создание таблицы данных
human_years = np.arange(0, 101, 5)
cat_years = human_years / 5

# Создание DataFrame
age_comparison = pd.DataFrame({
    'Годы жизни человека': human_years,
    'Годы жизни кошки': cat_years
})

# Вывод таблицы данных
# print(age_comparison)
display(age_comparison)
