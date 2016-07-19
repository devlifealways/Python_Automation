# __AUTHOR__  : ROUINEB Hamza
# __EMAIL__   : rouineb.business@gmail.com
# __PURPOSE__ : this script helps generate a new file with a given extension and and the same header
import sys, getopt
from datetime import datetime,date
import time


def usage():
    print ("This script makes it easier to generate a new file with the header already done")
    print ("To use it : python (version 2.X) ./"+ sys.argv[0] + " [OPTION] [ARGUMENT]")
    print ("OPTION:")
    print ("-"*len("OPTION"))
    print ("\t-p,--path".ljust(SPACE)+": The path where the file will be created !")
    print ("\t-a,--author".ljust(SPACE)+": The name of the user")
    print ("\t-e,--email".ljust(SPACE)+": The email of the creator")
    print ("\t-h,--help".ljust(SPACE)+": print the usage message")
    print ("\t-v,--verbose".ljust(SPACE)+": print some useful information")
    print ("ARGUMENT:")
    print ("-"*len("ARGUMENT"))
    print ("\tis the input value of each chosen option")

def make_file (Path="./generated.hrb",Author="Phoenix",Email="rouineb.business@gmail.com"):
    try:
        if len(Author) == 0:
            Author = 'Phoenix'
        if len(Email) == 0:
            Email='rouineb.business@gmail.com'
        Core = 'Flat is better than nested & Readability counts'

        NLINE = "\n"
        file = open(Path,"w+")
        file.write("# __AUTHOR__".ljust(SPACE)+":".ljust(3)+Author+NLINE)
        file.write("# __EMAIL__ ".ljust(SPACE)+":".ljust(3)+ Email+NLINE)
        file.write("# __CORE__".ljust(SPACE)+":".ljust(3)+Core+NLINE)
        file.write("# __DATE__".ljust(SPACE)+":".ljust(3)+datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H-%M-%S")+NLINE)
        file.write(NLINE)
        file.write("# __END__")
        file.close()
        if verbose :
            print ("The option that were user are  :")
            print ("Path    : "+path)
            if len(author) == 0:
                print ("Author  : Default(Phoenix)")
            else:
                print ("Author  : "+author)
            if len(email) == 0:
                print ("Email   : Default(rouineb.business@gmail.com)")
            else:
                print ("Email   : "+email)
    except Exception as ex:
        print (ex)


def remove_empty (author,email):
    if len(author) == 0:
        author = "ROUINEB Hamza"
    if len(email) == 0:
        email = "rouineb.business@gmail.com"

def launch () :
    global verbose
    global SPACE
    global path
    global email
    global author
    SPACE = 15
    path=''
    email=''
    author=''
    verbose = False
    try :
        opts,args =  getopt.getopt(sys.argv[1:],"p:e:a:hv",["path=","email=","author=","help","verbose"])
        for o,a in opts:
            if o in ("-h","--help"):
                usage()
                sys.exit()
            elif o in ("-e","--email"):
                email = a
            elif o in ("-p","--path") :
                path = a
            elif o in ("-a","--author"):
                author = a
            elif o in ("-v","--verbose"):
                verbose = True
            else:
                assert False,"Unhandled option"

        if path == '':
            assert False,"No Path was given !"

        remove_empty
        make_file(path,author,email)

        if verbose and len(args) :
            print ("Some arguments are not used at all")
            print (args)

    except Exception as err :
        print (str(err))
        sys.exit(2)

## launch zone:
launch()


#if __name__ == "__main__":
#    test()




# __ Bye __
