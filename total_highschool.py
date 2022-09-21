from openpyxl import load_workbook
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random

load_wb = load_workbook('twothang\연도별 대한민국 학령인구수.xlsx', data_only=True)

#한글 폰트
from matplotlib import font_manager, rc
font_path = "C:/Users/박진규/AppData/Local/Microsoft/Windows/Fonts/Maplestory Bold.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

load_ws = load_wb['Sheet1']

population_list = []
get_cells = load_ws['E2' : 'E62']
for row in get_cells:
    for cell in row:
        print(cell.value)
        population_list.append(cell.value)
print(population_list)

years = list(range(1960, 2021))


total_population_list = [25012374, 25765673, 26513030, 27261747, 27984155, 28704674, 29435571, 30130983, 30838302, 31544266, 32240827, 
32882704, 33505406, 34103149, 34692266, 35280725, 35848523, 36411795, 36969185, 37534236, 38123775, 38723248, 39326352, 39910403, 40405956, 40805744, 41213674, 41621690, 42031247, 42449038, 42869283, 43295704, 43747962, 44194628, 44641540, 45092991, 45524681, 45953580, 46286503, 46616677, 47008111, 47370164, 47644736, 47892330, 48082519, 48184561, 48438292, 48683638, 49054708, 49307835, 49554112, 49936638, 50199853, 50428893, 50746659, 51014947, 51217803, 51361911, 51606633, 51709098, 51780579]
print(total_population_list)
plt.scatter(total_population_list, population_list,  label='data')

plt.xlabel("총 인구수")
plt.ylabel("고등학생 수 (천 명)")
plt.legend()
plt.show()




# a와 b, c를 랜덤한 값으로 초기화합니다.
# # random.random()
# a = tf.Variable(random.random()*0.001 -1.403)
# b = tf.Variable(random.random()*0.001 + 5589.5)
# c = tf.Variable(random.random()*1 - 5564393.8)

# # 잔차의 제곱의 평균을 반환하는 함수입니다. 
# def compute_loss(): 
#   # 책의 본문(p, 83)은 아래처럼 되어 있지만, 에러가 날 것이다. 
#   # y_pred = a*X**2 + b*X + c
#   y_pred = a * years * years + b * years + c 
#   loss = tf.reduce_mean((population_list - y_pred) ** 2)
#   return loss

# optimizer = tf.keras.optimizers.Adam(lr=0.01)

# for i in range(600): 
#   # 잔차의 제곱의 평균을 최소화합니다. 
#     optimizer.minimize(compute_loss, var_list=[a,b,c])

#     # if i % 100 == 99: 
#     print(i, 'a:', a.numpy(), 'b:', b.numpy(), 'c:', c.numpy(),  'loss:', compute_loss().numpy())
#     if i == 599:
#         def f(x):
#             return a.numpy()*x*x + b.numpy()*x + c.numpy()
# print(f(2030))
# line_x = np.arange(min(years), max(years), 0.01)
# line_y = a * line_x * line_x + b * line_x+ c

# import matplotlib.pyplot as plt