import math

#my_list = [1/128,3/128,5/128,7/128,9/128,11/128,13/128,15/128,15/128,13/128,11/128,9/128,7/128,5/128,3/128,1/128]

my_list = [1/8,3/8,3/8,1/8]

my_other_list = [1/16,3/16,3/16,1/16,1/16,3/16,3/16,1/16]


entropy_A = 0
entropy_B = 0

for i in range(len(my_list)):
    entropy_A += my_list[i]*math.log2(1/my_list[i])

for i in range(len(my_other_list)):
    entropy_B += my_other_list[i]*math.log2(1/my_other_list[i])

print("Entropy X: {}".format(entropy_A))

print("Entropy Y: {}".format(entropy_B))
