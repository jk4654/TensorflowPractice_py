from openpyxl import load_workbook
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random
load_wb = load_workbook('twothang\연도별 대한민국 학령인구수.xlsx', data_only=True)

load_ws = load_wb['Sheet1']

population_list = []
get_cells = load_ws['E2' : 'E63']
for row in get_cells:
    for cell in row:
        print(cell.value)
        population_list.append(cell.value)
print(population_list)

years = list(range(1960, 2022))

# a와 b, c를 랜덤한 값으로 초기화합니다.
# random.random()
a = tf.Variable(-1.75)
b = tf.Variable(6965.0)
c = tf.Variable(-6926000.0)

# 잔차의 제곱의 평균을 반환하는 함수입니다. 
def compute_loss(): 
  # 책의 본문(p, 83)은 아래처럼 되어 있지만, 에러가 날 것이다. 
  # y_pred = a*X**2 + b*X + c
  y_pred = a * years * years + b * years + c 
  loss = tf.reduce_mean((population_list - y_pred) ** 2)
  return loss

optimizer = tf.keras.optimizers.Adam(lr=10)

for i in range(600): 
  # 잔차의 제곱의 평균을 최소화합니다. 
    optimizer.minimize(compute_loss, var_list=[a, b, c])

    # if i % 100 == 99: 
    print(i, 'a:', a.numpy(), 'b:', b.numpy(), 'c:', c.numpy(), 'loss:', compute_loss().numpy())

line_x = np.arange(min(years), max(years), 0.01)
line_y = a * line_x * line_x + b * line_x + c

plt.scatter(years, population_list)
plt.plot(line_x,line_y,'r-')
plt.show()