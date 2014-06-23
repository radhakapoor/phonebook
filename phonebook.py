import sys
import pickle

filename = 'hsphonebook.pb'

def main():    
    if sys.argv[1] == 'create':
        create_phonebook(filename)
    elif sys.argv[2] == 'add':
        name = sys.argv[3]
        number = sys.argv[4]        
        add_phonebook(read_pb(filename), name, number)        
    elif sys.argv[2] == 'lookup':
        name = sys.argv[3]        
        lookup_name(read_pb(filename), name)
    elif sys.argv[2] == 'change':
        name = sys.argv[3]
        number = sys.argv[4] 
        change_name(read_pb(filename), name, number)
    elif sys.argv[2] == 'remove':
        name = sys.argv[3]        
        remove_name(read_pb(filename), name)
    elif sys.argv[2] == 'reverse-lookup':
        number = sys.argv[3]
        reverse_lookup(read_pb(filename), number)

def hello():
    return 1234 

def create_phonebook(filename):    
    pb = {}
    output = open(filename, 'wb')
    dump_pb(pb)

def read_pb(filename):    
    pkl_file = open(filename, 'rb')    
    pb = pickle.load(pkl_file)
    pkl_file.close()
    print pb     
    return pb

def dump_pb(pb):    
    output = open(filename, 'wb')
    pickle.dump(pb, output)
    print "dump_pb is ", pb
    output.close()
    return pb    

def add_phonebook(pb, name, number):             
    if name in pb:
        print "Duplicate! This name already exists in the phonebook!"
    else:    
        pb.update({name:number})
        dump_pb(pb)
        return pb 
    
def lookup_name(pb, name):        
    print pb       
    matches = [(pb_name, pb_number) for (pb_name, pb_number) in pb.iteritems() if name in pb_name]
    for m in matches:
        print str(m[0]) + ' ' + str(m[1])
        return str(m[0]) + ' ' + str(m[1])     
    

def change_name(pb, name, number):         
    if name in pb:
        pb[name] = number
        dump_pb(pb)
    else:
        print "Error! This name is not in the phonebook"    


def remove_name(pb, name):         
    if name in pb:
        del pb[name]
        dump_pb(pb)
    else:
        print "Error! This name is not in the phonebook"      

    
def reverse_lookup(pb, number):              
    print pb       
    matches = [(pb_name, pb_number) for (pb_name, pb_number) in pb.iteritems() if number in pb_number]
    for m in matches:
        print str(m[0]) + ' ' + str(m[1])
        return str(m[0]) + ' ' + str(m[1])      

  
if __name__ == '__main__':
    main()