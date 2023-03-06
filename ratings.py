"""Restaurant rating lister."""

"""Restaurant name and score"""
# put your code here
scores = {}

file = open('scores.txt')

for line in file:
    line = line.rstrip().split(":")  # OR line = line.split(":")
    scores[line[0]] = line[1]

#prompt user
print("Add the restaurant and rating")
restaurant = input("restaurant name: ")
rating = input("restaurant rating: ")

scores[restaurant] = rating #add user input to scores dict


sorted = sorted(scores) #list of keys in scores in abc order
for key_name in sorted: #loop through list of keynames and using those keynames to access value in scores
    print (f"{key_name}: {scores[key_name]}")
      
      



