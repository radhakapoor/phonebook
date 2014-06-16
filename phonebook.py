import sys
import pickle

def main():
    if sys.argv[1] == 'create':
        create_phonebook()
    if sys.argv[2] == 'add':        
        add_phonebook(read_pb())
    if sys.argv[2] == 'lookup':
        lookup_name(read_pb())
    if sys.argv[2] == 'change':
        change_name(read_pb())
    if sys.argv[2] == 'remove':
        remove_name(read_pb())
    if sys.argv[2] == 'reverse-lookup':
        reverse_lookup(read_pb())

def create_phonebook():
    filename = sys.argv[2]
    pb = {}
    output = open(filename, 'wb')
    dump_pb(pb)

def read_pb(): 
    filename = 'hsphonebook.pb'
    pkl_file = open(filename, 'rb')    
    pb = pickle.load(pkl_file)
    pkl_file.close()
    print pb     
    return pb

def dump_pb(pb):
    filename = 'hsphonebook.pb'
    output = open(filename, 'wb')
    pickle.dump(pb, output)
    print "dump_pb is ", pb
    output.close()

def add_phonebook(pb): 
    name = sys.argv[3]
    number = sys.argv[4]        
    if name in pb:
        print "Duplicate! This name already exists in the phonebook!"
    else:    
        pb.update({name:number})
        dump_pb(pb)
    
def lookup_name(pb):
    name = sys.argv[3]    
    print pb       
    matches = [(k,v) for (k,v) in pb.iteritems() if name in k]
    for m in matches:
        print str(m[0]) + ' ' + str(m[1])   
    

def change_name(pb):
    name = sys.argv[3]
    number = sys.argv[4]      
    if name in pb:
        pb[name] = number
        dump_pb(pb)
    else:
        print "Error! This name is not in the phonebook"    


def remove_name(pb):
    name = sys.argv[3]       
    if name in pb:
        del pb[name]
        dump_pb(pb)
    else:
        print "Error! This name is not in the phonebook"      

    
def reverse_lookup(pb):
    reverse_lookup = sys.argv[3]      
    print pb       
    matches = [(k,v) for (k,v) in pb.iteritems() if sys.argv[3] in v]
    for m in matches:
        print str(m[0]) + ' ' + str(m[1])
    
 
main()