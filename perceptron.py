import sys
import random

class Perceptron():

	# Initial Perceptron Variables
	def __init__(self, inputs):
		self.inputs = inputs
		self.learning_speed = 0.000008
		self.input_weights = []
		self.expected_value = self.inputs[0]
		self.bias = 1 # => Constant necessary for take a better decision 
		self.init_weight()
		
	# Initial weigths for all the inputs
	def init_weight(self):
		self.inputs.append(self.bias)
		for input in self.inputs:
			self.input_weights.append(random.random())

	# Modify the weights based on the weighted sumatory of the inputs
	def calculate_decision(self):
		decision = 0
		counter = 0
		for input in self.inputs:
			decision += input * self.input_weights[counter]
			counter += 1
		self.activate(decision)

	# Detect if the expected result was accomplished, if it happened I will reinforce the weights in order to start the learning process
	def activate(self, decision):
		print "Expected: "+str(self.expected_value)
		print "Get: "+str(decision)
		print "Move to the Light: "+str((decision > self.expected_value))
		if(decision > self.expected_value):
			print "Move to the Light"
			# If the decision is the expected, I will reinforce the weights based on the delta between the expected and the getted value, taking in consideration the learn speed variable
			delta_error = (decision - self.expected_value)
			counter = 0
			for x in range(len(self.input_weights)):
				self.input_weights[x] += self.inputs[counter] * delta_error * self.learning_speed
				counter += 1
		else:
			print "I am seeing Darkness! I don not want to move in that direction"
			print "Activate Rotation"
		self.expected_value = decision
		self.inputs[0] = self.inputs[1]

	# Simple Setter to modify inputs on the fly
	def set_inputs(self, inputs):
		self.inputs = inputs
		
# Training function for the Simple Neural System
def training():
	sensor_input = [0,0]
	perceptron = Perceptron(sensor_input)
	for i in range(100):
		sensor_input[1] += 10
		perceptron.set_inputs(sensor_input)
		perceptron.calculate_decision()
 	
# Main loop to detect the differences between the last light input value and the new one after that the robot moves to the light
def main():
	sensor_input = [0,0]
	perceptron = Perceptron(sensor_input)
	counter = 0
	while True:
		sensor_input[1] = int(raw_input("Read Input: "))
		perceptron.set_inputs(sensor_input)
 		perceptron.calculate_decision()

#training()
main()