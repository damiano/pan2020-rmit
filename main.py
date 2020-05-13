import os 
import sys, getopt
from pan.user_level.admin import admin

def main(args=None):
    
    inputfile = ''
    outputfile = ''
    if args is None:
        args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args,"hi:o:",["ifile=","ofile="])
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
    print("Input file:", inputfile)
    print("Output file:", outputfile)    
    ad=admin(inputfile,outputfile)        
    ad.start()
if __name__ == '__main__':
    main()
    
