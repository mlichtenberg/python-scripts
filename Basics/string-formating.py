num_true = 27
num_false = 39

# Print a formatted string that includes numbers represented as integers and floats
print("True cases {0} ({1:2.2f}%)".format(num_true, (num_true / (num_true + num_false)) * 100))
print("False cases {0} ({1:2.2f}%)".format(num_false, (num_false / (num_true + num_false)) * 100))