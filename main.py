import os 
import sys, getopt
from user_level.admin import admin

def main(argv):
    
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('args needed')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-i, -o')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    ad=admin(inputfile,outputfile)        
    ad.start()
if __name__ == '__main__':
    main(sys.argv[1:])
    