# Write a Python function to count the number of vowels in a given string.
str ='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
vowel_count = 0
for i in str:
    if i == 'a' or i =='e' or i =='i' or i =='o' or i =='u':
        vowel_count += 1
print(vowel_count)
