sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
 ## Change the sentence into dictionary with each word as the key and the length of the word as the value ##

result = {word:len(word) for word in sentence.split()}


print(result)

