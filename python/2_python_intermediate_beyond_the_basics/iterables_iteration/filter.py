#Filter does as the name suggests filters out elements from a collection given a rule.
positives = filter(lambda x: x>0,[1,-5,0,6,-2,8])
print(list(positives))
#If none is given removes all "falsey" type elements.
trues = filter(None,[0,1,False,True,[],[1,2,3],'','hello'])
print(list(trues))