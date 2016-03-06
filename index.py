# python math

import math # math module

perc = 1/3.0 # fraction/percentage of the macaw's weight that can be carried
coco_wt = 1450 # weight, in grams, of the coconut
macaw_wt = 900 # weight, in grams, of the macaw
macaw_limit = macaw_wt * perc # formula to calculate the macaw can carry in grams

num_macaw = coco_wt/macaw_limit # formula to calculate the number of macaws required to carry the coconut

print math.ceil(num_macaw) # module/method for rounding a number up
