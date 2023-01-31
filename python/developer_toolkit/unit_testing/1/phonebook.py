import itertools as it
class Phonebook:
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
    
    def lookup(self, name):
        return self.entries[name]
        
    def is_consistent(self):
    	for x,y in it.combinations(list(self.entries.values()),2):
    		if y in x or x in y:
    			return False
    		else:
    			continue
    	return True

    def get_names(self):
    	return list(self.entries.keys())

    def get_numbers(self):
    	return list(self.entries.values())


def main():

if __name__ == "__main__":main()