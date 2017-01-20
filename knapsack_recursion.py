w = 8
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]

max_val = 0

def knapsack(total_weight, total_value, cur_wt, cur_vt):
	global max_val
	if total_weight > w:
		return 
	total_weight += cur_wt
	total_value += cur_vt

	if total_value > max_val and total_weight <= w:
		max_val = total_value
		# print str(total_value)+" total_weight :"+ str(total_weight) + " current weight : "+ str(cur_wt)

	for j in range(len(wt)):
		knapsack(total_weight, total_value, wt[j],val[j])

for i in range(len(wt)):
	total_weight = 0
	total_value = 0
 	lst_weight = []
	knapsack(total_weight, total_value, wt[i],val[i] )

	
print max_val