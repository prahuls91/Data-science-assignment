import sys
def add(a,b):
    print (int(a)+int (b))

def sub(a,b):
	print(int(a)-int (b))

def divide(a,b):
	print(int(a)/int(b))

def mult(a,b):
	print(a*b)
    
def main(args):
    add(args[0],args[1])

if __name__ == "__main__":
    args = sys.argv[1:]
    if len (args) < 2 :
        print ("Less than 2 args")
        sys.exit (1)
    main(args)