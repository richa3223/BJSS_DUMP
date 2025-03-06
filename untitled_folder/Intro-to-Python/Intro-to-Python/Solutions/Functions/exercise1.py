
# Exercise 1 

# Question 1
def f_to_c(f):
    c = (5/9) * (f-32)
    print(f"{f}F is {round(c,1)}C")

# Question 2
def max_diff(num, num_list):
    diff = []
    for i in num_list:
        diff.append(abs(num - i))
    return diff.index(max(diff))

# Question 3
def mean_info(num_list):
    mean = sum(num_list)/len(num_list)
    index = max_diff(mean, num_list)
    maximum_diff = abs(mean - num_list[index])
    return {'mean' : mean, 'max diff index' : index, 'max diff' : maximum_diff}