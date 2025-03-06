
# Exercise 2

# Question 1
multiply_tuple = lambda x : x[0] * x[1]

# Question 2
sub50 = lambda x : max(x-50,0)

# Question 3
str_manipulation = lambda s1, s2, s3 : " ".join([s1, s2, s3]).lower() if s1.lower().startswith('data') else "First string does not start with 'Data'"