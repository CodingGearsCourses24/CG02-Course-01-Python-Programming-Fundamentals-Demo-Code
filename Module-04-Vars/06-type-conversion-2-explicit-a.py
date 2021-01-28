# Type Conversion - Explicit
# A.K.A Type Casting,
# One Data Type --> To Another Data Type

var_integer = 24
var_float = "two"

#var_sum = var_float + var_integer
var_sum = float(var_float) + var_integer

print("var_integer Data Type : ", type(var_integer))
print("var_float Data Type : ", type(var_float))

print("The value of var_sum :", var_sum)
print("var_sum Data Type : ", type(var_sum))
