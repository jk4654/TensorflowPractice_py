import tensorflow as tf
키 = 179
신발 = 280
a = tf.Variable(0.1)
b = tf.Variable(0.2)

def 손실함수():
    예측값 = 키 * a + b
    return tf.square(280 - 예측값)


opt = tf.keras.optimizers.Adam(learning_rate=0.1)
for i in range(10):
    opt.minimize(손실함수, var_list=[a,b])
    print(a.numpy(), b.numpy())