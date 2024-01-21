# DAY 3

## Part 1

### Python (first approach)

since there's the same amount of character in each line, we can add or substract the number of character in line to access the char right above or below 

careful though, EOF char counts as a character if you don't replace them

there are also the special cases of indices on the left or right end of each to take into account (the indices right below the one on the left end of a line would be the one on th right end of the preceding line, thus not being adjacent)

The approach considered was to gather  in a set (to be accessible in constant time) all the indices that were adajcent to a symbol.
Then gather all the numbers in the input and test if at least one of their digit index is in the symbol adjacent set. If so then append the concerned number to a list, and finally sum all of the entries in said list.

I made an error on my first try. I combined all the numbers to be summed in a set, thus forbiding duplicate entries as a security, but nothing int the brief forbade number to be duplicates. 

answer is 540025

## Part 2

### Python (first approach)

The approach is similar to the first one but this time we have to gather only if the specific symbol is adjacent to two numbers. 

By gathering in adavance the indices of all the digits in the input, we can then test for values when gathering adjacent indices to the symbol instead of afterwards. A good way to do this efficiently is to use a dictionary (for constant search time on keys)with indices of digits (what will be accessed) as keys and the corresponding full number as val.

We can verify then that multiple adjacent indices are in the said dictionary, and if so gather the corresponding numbers, multiply them, and store the result in a list to be summed further down.

But it has to be consider that the multiple digit adjacent may be coming from the same number. At first, I considered verifying that the values of the number were different, but then it may have ended up in a similar case to the preceding error.

I decided to store a generated id as well as the value in the numbers dict, thus using this id to verify that the multiple digit adjacent where indeed coming from distinct numbers.

careful to only multiply if there's two adajacent numbers.

Answer is 84584891