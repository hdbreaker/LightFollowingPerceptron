import random

class Perceptron():

	# Initial Perceptron Variables
	def __init__(self, inputs):
		self.inputs = inputs
		self.learning_speed = 0.02
		self.input_weights = []
		self.expected_value = inputs[0]
		self.init_weight()
		
	# Initial weigths for all the inputs
	def init_weight(self):
		for input in self.inputs:
			self.input_weights.append(random.random())

	# Modify the weights based on the weighted sumatory of the inputs
	def predict(self):
		predict_result = 0
		counter = 0
		for input in self.inputs:
			predict_result += input * self.input_weights[counter]
			counter += 1
		self.evaluate(predict_result)

	# Detect if the expected result was accomplished, if it happened I will reinforce the weights in order to start the learning process
	def evaluate(self, predict_result):
		if(predict_result >= self.expected_value):
			print "In the Light"
			# If the prediction is correct, I will reinforce the weights based on the delta between the expected and the getted value, taking in consideration the learn speed variable
			delta_error = (predict_result - self.expected_value)
			for weight in self.input_weights:
				weight = weight * delta_error * self.learning_speed
		else:
			print "In the Shadows!"

	# Simple Setter to modify inputs on the fly
	def set_inputs(self, inputs):
		self.inputs = inputs
		self.expected_value = inputs[0]

# Training function for the Simple Neural System
def training():
	sensor_input = [0,0]
	perceptron = Perceptron(sensor_input)
	for i in range(2000):
		if(i == 0):
			sensor_input[0] = 0
			sensor_input[1] = 0
		else:
			sensor_input[0] = sensor_input[1]
			sensor_input[1] = sensor_input[1]+10
		perceptron.set_inputs(sensor_input)
		perceptron.predict()
 	
# Main loop to detect the differences between the last light input value and the new one after that the robot moves to the light
def main():
	sensor_input = [0,0]
	perceptron = Perceptron(sensor_input)
	counter = 0
	while True:
		if(counter == 0):
			sensor_input[0] = int(raw_input("Input: "))
			sensor_input[1] = sensor_input[0]
		else:
			sensor_input[0] = sensor_input[1]
			sensor_input[1] = int(raw_input("New Input: "))
			perceptron.set_inputs(sensor_input)
 		perceptron.predict()
 		counter += 1

training()
main()