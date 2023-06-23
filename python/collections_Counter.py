from collections import Counter

a = "aaabbbbacccc" #this works on any other iterable

my_counter = Counter(a) #this returns a dictionary with the word frequency
print(my_counter)

print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1)[0][0]) #can pass parameter to the number of elements we need,rest is the indexing
