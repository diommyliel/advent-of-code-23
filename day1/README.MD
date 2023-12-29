# PART 1

Given a input file with lines of strings all containing letters and numbers, retrieve the sum of the two digit number formed by the first and the last digit in each lines.

If there's only one digit in the string, it will act both as the first and the last digit.

Answer is 53080

# PART 2

Same as above, but with spelled out digits (ex 'three') counting as digits 

Attention, must use rfind for the r pointer to handle the case where there's two occurences of the same digit (find returns the first occurence from the left; rfind the first occurence from the right)

Answer is 53268
