#!/usr/bin/python                                                                                                                                                                  

"""                                                                                                                                                                                
Implementation of comm command.                                                                                                                                                    
"""
import random, sys
from optparse import OptionParser


def main():
    version_msg = "%prog 2.0"                                                                                                                                                      
    usage_msg = "%prog [-123u] FILE1 FILE2"                                                                                                                                       
    parser = OptionParser(version=version_msg, usage=usage_msg)  
    parser.add_option("-u", action="store_true", dest="un", default=0)
    parser.add_option("-1", action="store_true", dest="one", default=0)
    parser.add_option("-2", action="store_true", dest="two", default=0)
    parser.add_option("-3", action="store_true", dest="three", default=0)
    options, args = parser.parse_args(sys.argv[1:])
    
    if len(args)!=2:
        parser.error("Wrong number of operands")
    
    file1=args[0]
    file2=args[1]
    lines1 = []
    lines2 =[]
    if file2=="-":
        lines1=sys.stdin.readlines()

        try:
            f2 = open (file1, 'r')
            lines2 = f2.readlines()
            f2.close()
        except:
            parser.error("Invalid file")

    else:
        try:
            f1 = open (file1, 'r')
            f2 = open (file2, 'r')
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            f1.close()
            f2.close()
        except:
            parser.error("Invalid file")
        
        
    un=options.un
    one=options.one
    two=options.two
    three=options.three

    
    sp="        "
 
    n1 = len(lines1)
    n2 = len(lines2)
    col1 = []
    col2 = []
    col3 = []
    n=0
    if un==0:
        col3=[i for i in lines1 if i in lines2]
        for i in col3:
            if i in lines2:
                lines2.remove(i)
        for i in col3:
            if i in lines1:
                lines1.remove(i)
        t=sorted(lines1+col3+lines2)

        col1=lines1
        col2=lines2
        for i in t:
            if i in col1 and one!=1:
                sys.stdout.write(i)
            
            if i in col2 and one!=1 and two!=1:
                sys.stdout.write(sp+i)
            elif i in col2 and one==1 and two!=1:
                sys.stdout.write(i)

            if i in col3 and one!=1 and two!=1 and three!=1:
                sys.stdout.write(sp+sp+i)
            elif i in col3 and one==1 and two!=1 and three!=1:
                sys.stdout.write(sp+i)
            elif i in col3 and one!=1 and two==1 and three!=1:
                sys.stdout.write(sp+i)
            elif i in col3 and one==1 and two==1 and three!=1:
                sys.stdout.write(i)

    if un==1:
        col3=[i for i in lines1 if i in lines2]
        for i in col3:
            if i in lines2:
                lines2.remove(i)
        for i in lines1:
            if i in col3 and one!=1 and two!=1 and three!=1:
                sys.stdout.write(sp+sp+i)
            elif i in col3 and one==1 and two!=1 and three!=1:
                sys.stdout.write(sp+i)
            elif i in col3 and one!=1 and two==1 and three!=1:
                sys.stdout.write(sp+i)
            elif i in col3 and one==1 and two==1 and three!=1:
                sys.stdout.write(i)
            elif i not in col3 and one!=1:
                sys.stdout.write(i)
        for i in lines2:
            if one!=1 and two!=1:
                sys.stdout.write(sp+i)
            elif one==1 and two!=1:
                sys.stdout.write(i)
                                                                                                                                                                                                                                                                                                                    
if __name__ == "__main__":
    main()




