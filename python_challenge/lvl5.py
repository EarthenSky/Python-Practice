import pickle

# Create the obj.
fileObject = open("banner.p",'r')
_obj = pickle.load(fileObject)

print _obj

#      ----------------------------------------------
print "----------------------------------------------"
#      ----------------------------------------------

for _list in _obj:
    #print _list  #Coloumn

    line = ""
    for _tuple in _list:
        #print _tuple  #Line
        line += _tuple[0] * _tuple[1]

    print line

#This is so fucking awesome.
