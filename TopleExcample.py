'''
tupleExcample = ('Toey','Som','Rich')
print(tupleExcample)
tupleExcample2 = ('Bank','Kay')
tupleExcample3 = tupleExcample+tupleExcample2
print(tupleExcample3)
print(tupleExcample3[:2])
'''
tupleExcample = ('Toey','Som','Rich')
tupleExcample2 = ('Bank','Kay')
tupleExcample3 = tupleExcample+tupleExcample2
for x in tupleExcample3:
    print(x)
    print('Toey' in tupleExcample3)