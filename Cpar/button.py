

import pandas as pd
import matplotlib.pyplot as plt
import random

peoples_df = pd.read_csv('D:/pima.csv', encoding='utf-8', header=None, sep=',')
peoples_df
print('Len:', len(peoples_df))
# Xem thông tin dataframe vừa đọc được
peoples_df.info()
# Xem kích thước của dataframe
print('Shape:', peoples_df.shape)