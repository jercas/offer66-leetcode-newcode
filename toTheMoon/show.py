from keras.models import Sequential
from keras.layers import Dense, LSTM, Bidirectional, TimeDistributed, RepeatVector
time_steps = 50
features = 1
outputs = 5
# define model
model1 = Sequential()
model1.add(LSTM(20, return_sequences=True, input_shape=(time_steps, features)))
model1.add(LSTM(20, return_sequences=True))
model1.add(LSTM(20))
model1.add(Dense(outputs))
model1.compile(loss='mae' , optimizer='adam')
print(model1.summary())

# define model
model2 = Sequential()
model2.add(LSTM(50, return_sequences=True, input_shape=(time_steps, features)))
model2.add(Bidirectional(LSTM(50, return_sequences=True)))
model2.add(TimeDistributed(Dense(1)))
model2.add(Dense(1))
model2.compile(loss= 'binary_crossentropy' , optimizer= 'adam' , metrics=[ 'acc' ])
print(model2.summary())

# define model
model3 = Sequential()
model3.add(LSTM(75, input_shape=(time_steps, features)))
model3.add(RepeatVector(time_steps))
model3.add(LSTM(50, return_sequences=True))
model3.add(TimeDistributed(Dense(features, activation= 'sigmoid' )))
model3.add(Dense(1))
model3.compile(loss= 'categorical_crossentropy' , optimizer= 'adam' , metrics=[ 'accuracy' ])
print(model3.summary())

models = [model1, model2, model3]
for i, model in enumerate(models):
	json_string = model.to_json()
	json = 'model{0}.json'.format(i)
	with open(json, 'w') as of:
		of.write(json_string)