import tensorflow as tf
import numpy as np

# 입력 데이터
x_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float32)
y_train = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], dtype=np.float32)

# 가중치와 편향 초기화
w = tf.Variable(0.0)
b = tf.Variable(0.0)

# 선형 모델 정의
def linear_regression(x):
    return w * x + b

# 손실 함수 정의 (평균 제곱 오차)
def mean_square_error(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))

# 옵티마이저 정의 (경사 하강법)
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# 학습 함수 정의
def train_step(x, y):
    with tf.GradientTape() as tape:
        y_pred = linear_regression(x)
        loss = mean_square_error(y_pred, y)
    
    gradients = tape.gradient(loss, [w, b])
    optimizer.apply_gradients(zip(gradients, [w, b]))

# 학습
epochs = 100
for epoch in range(epochs):
    train_step(x_train, y_train)

# 결과 출력
print("가중치(w): {:.2f}".format(w.numpy()))
print("편향(b): {:.2f}".format(b.numpy()))