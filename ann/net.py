from math import sqrt, pi, sin
import random
import numpy
import matplotlib.pyplot as plt

neurons = 10
acceptable_error = .0001 #stops updating if the average squared error is less than this
max_iter = 100000 #stops updating if this number of iterations is reached
updates = 5 #number of times to calculate the average error (and write it to the console)

update_iter = max_iter / updates - 1

#the one-neuron function to predict sin(x) is: y = a * max(0, a1 * x + a2) + b
a = []
a1 = []
a2 = []
da = []
da1 = []
da2 = []
linear_combo = [] #this is a1 * x + a2
b = 0.0
db = 0.0

for i in range(neurons):
	a.append(random.uniform(-1, 1))
	a1.append(random.uniform(-1,1))
	a2.append(0.0)
	linear_combo.append(0.0)
	da.append(0.0)
	da1.append(0.0)
	da2.append(0.0)

avg_error = 0
current_error = 10

x = 1

#perhaps have the code increase the number of neurons if acceptable error isn't met
#in a future version of the code
while x < max_iter and current_error > acceptable_error:
	
	#get new input between -pi and pi
	input = random.uniform(-pi, pi)
	act = sin(input)
	predict = 0

	#update weights and predict sin(input) from the input
	for i in range(neurons):
		a[i] += da[i]
		a1[i] += da1[i]
		a2[i] += da2[i]
		linear_combo[i] = a1[i] * input + a2[i]
		if (linear_combo[i] > 0):
			predict += a[i] * linear_combo[i]
	b += db
	predict += b

	#calculate error, write avg error to console if needed	
	error = (act - predict) ** 2
	avg_error += error
	if (x % update_iter == 0):
		avg_error /= update_iter
		print("Avg squared error: ", avg_error)
		current_error = avg_error
		avg_error = 0
	
	#calculate weight changes
	step = .001
	sign = numpy.sign(act - predict)
	for i in range(neurons):
		if (linear_combo[i] > 0):
			da[i] = step * linear_combo[i] * sqrt(error) * sign	
			da1[i] = step * a[i] * input * sqrt(error) * sign
			da2[i] = step * a[i] * sqrt(error) * sign
	db = step * sqrt(error) * sign
	
	x += 1

#plot sin(x) against predictions for 100 values of x between -pi and pi
test = []
out = []
sine = []

for y in range (100):
	
	input = -pi + y * 2 * pi / 99
	test.append(input)
	sine.append(sin(input))

	output = 0
	for i in range(neurons):
		output += a[i] * max(0, a1[i] * input + a2[i])
	output += b
	out.append(output)

plt.plot(test, out, 'gs', test, sine)
plt.axis([-pi, pi, -1.5, 1.5])
plt.show()	
