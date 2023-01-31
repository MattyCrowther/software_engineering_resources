#The functools.reduce takes a rule and applies it to the 0th and 1st element of the list iterativley then does it again with result + 3rd element and so on.
from functools import reduce
import operator #Just a standard addition a+b == operator.add(a,b)
temp = reduce(operator.add,[1,2,3,4,5])
print(temp)

#Equivalent in normal
numbers = [1,2,3,4,5]
accumulator = operator.add(numbers[0],numbers[1])
for item in numbers[2:]:
	accumulator = operator.add(accumulator,item)

#---------------------------------------------------------------------------------------------

def mul(x,y):
	print('mul {} {}'.format(x,y))
	return x*y

reduction = reduce(mul,range(1,10))
print(reduction)

#---------------------------------------------------------------------------------------------
#EXTRA:: Combining map-reduce
#Uses map and reduce to create a way of finding how many times a word is present in a dictionary, uses map with the rule of count_words to produce a list of numbers and counts, then reduce using the 
#combine_counts function.

def count_words(doc):
	normalised_doc = ''.join(c.lower() if c.isalpha() else '' for c in doc)
	frequencies = {}
	for word in normalised_doc.split():
		frequencies[word] = frequencies.get(word,0)+1
	return frequencies

documents = ['Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry',
              's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ',
              'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' ,
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing ',
              'software like Aldus PageMaker including versions of Lorem Ipsum.']

counts = map(count_words,documents)

def combine_counts(d1,d2):
	d = d1.copy()
	for word,count in d2.items():
		d[word] = d.get(word,0) + count
	return d

total_counts = reduce(combine_counts,counts)
print(total_counts)