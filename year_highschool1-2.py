from openpyxl import load_workbook
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random


#한글 폰트
from matplotlib import font_manager, rc
font_path = "C:/Users/박진규/AppData/Local/Microsoft/Windows/Fonts/Maplestory Bold.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#엑셀 파일 불러오기
load_wb = load_workbook('twothang\연도별 대한민국 학령인구수.xlsx', data_only=True)
load_ws = load_wb['Sheet1']

#인구수 리스트
population_list = []
get_cells = load_ws['E2' : 'E63']
for row in get_cells:
    for cell in row:
        print(cell.value)
        population_list.append(cell.value)
print(population_list)

years = list(range(1960, 2021))

# a와 b, c를 랜덤한 값으로 초기화합니다. 
# a = tf.Variable(random.random()) 이렇게 해야 하는데 막 랜덤으로 하면 값이 이상하게 나와서 수학적으로 게산해서 좀 맞춰줬음
a = tf.Variable(random.random()*0.001 -1.403)
b = tf.Variable(random.random()*0.001 + 5589.5)
c = tf.Variable(random.random()*1 - 5564393.8)

# 잔차의 제곱의 평균을 반환하는 함수입니다. 
def compute_loss(): 
  y_pred = a * years * years + b * years + c 
  loss = tf.reduce_mean((population_list - y_pred) ** 2)
  return loss

optimizer = tf.keras.optimizers.Adam(lr=0.01)

for i in range(600): 
  # 잔차의 제곱의 평균을 최소화합니다. 
    optimizer.minimize(compute_loss, var_list=[a,b,c])

    # if i % 100 == 99: 
    print(i, 'a:', a.numpy(), 'b:', b.numpy(), 'c:', c.numpy(),  'loss:', compute_loss().numpy())
    if i == 599:
        def f(x):
            return a.numpy()*x*x + b.numpy()*x + c.numpy()

print(f(2030))
line_x = np.arange(min(years), max(years), 0.01)
line_y = a * line_x * line_x + b * line_x+ c

plt.scatter(years, population_list, label='data')
plt.plot(line_x,line_y,'r-', label='polynomial')
plt.xlabel("연도")
plt.ylabel("고등학생 수 (천 명)")
plt.legend()
plt.show()