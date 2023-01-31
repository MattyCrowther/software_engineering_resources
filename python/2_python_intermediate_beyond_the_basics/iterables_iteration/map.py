#The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
#Can be equivlaent to set comprehension so take your pick (I think set sc is easier to understand)
#Bascially takes a rule and creates a list.
import itertools
size = ['small','medium','large']
colour = ['red','blue','green']
animal = ['dog','bird','cat']
def combine(quantity,size,colour,animal):
	return '{} {} {}'.format(quantity,size,colour,animal)

print(list(map(combine,itertools.count(),size,colour,animal)))