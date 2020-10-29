#!/usr/bin/env python3
import random

platset1 = {3,4,6,8}
platset2 = {3,7,6}
print("Set1 => {}\nSet2 => {}\n".format(platset1,platset2))

print(platset1 == platset2)
print(platset1 > platset2)

# union of sets
print("Union =>", platset1 | platset2)

# Intersection
print("Intersection =>", platset1 & platset2)

# Difference
print("Difference => ", platset1 - platset2)

# Symmetric Difference
print("Symmetric Difference => ", platset1 ^ platset2)

# Add to set
platset1.add(95)
platset1.add(9)
print("Set1 => {}\nSet2 => {}\n".format(platset1,platset2))

# Remove
platset1.remove(3)
platset1.add(6)
print("Set1 => {}\nSet2 => {}\n".format(platset1,platset2))

print(random.randrange(1,7))
