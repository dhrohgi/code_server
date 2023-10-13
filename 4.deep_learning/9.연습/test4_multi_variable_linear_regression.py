import tensorflow as tf
import numpy as np

x_train = [[73, 80, 75], 
           [93, 88, 93], 
           [89, 91, 90], 
           [96, 98, 100],
           [73, 68, 70]]
y_train = [[152],
           [185],
           [180],
           [196],
           [142]]

tf.model = tf.keras.Sequential()

tf.model.add(tf.keras.layers.Dense(units=1, input_dim=3))
tf.model.add(tf.keras.layers.Activation('linear'))

tf.model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(learning_rate=1e-5))
tf.model.summary()
history = tf.model.fit(x_train, y_train, epochs=100)

y_predict = tf.model.predict(np.array([[72, 93, 90]]))
print(y_predict)
