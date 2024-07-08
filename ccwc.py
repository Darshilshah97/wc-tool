#!/usr/bin/env python3ccwc
import argparse
import os
import sys

def main():

    parser = argparse.ArgumentParser(description="a simple command line tool")

    parser.add_argument('filename', nargs='?', type=str, help='file name')
    parser.add_argument('-c', '--bytes', action='store_true', help='get bytes of the specified file')
    parser.add_argument('-l', '--lines', action='store_true', help='get number of lines present in file')
    parser.add_argument('-w', '--words', action='store_true', help='get number of words present in file')
    parser.add_argument('-m', '--characters', action='store_true', help='get number of characters present in file')
    
    
    args = parser.parse_args()
    print(args)
    
    if args.filename :
        providedFile = args.filename
        if not os.path.isfile(providedFile):
            print("File does not exist. Please provide valid filename")
            return
        
        f = open(providedFile,'r', encoding='utf8')
        opeartions(args,providedFile,f)
        f.close()

    else:

        if sys.stdin.isatty() is False:
            fileContent = sys.stdin.read()
            providedFile = 'temp.txt'
            f = open(providedFile,"a")
            f.write(fileContent)
            f.close()
            f = open(providedFile,'r', encoding='utf8')
            opeartions(args,providedFile,f)
            f.close()
            os.remove(providedFile)
        else:
            print("Please provide filename in the arguments!")
            return
    

def opeartions(args, providedFile, f):
    
    if args.bytes:
        print(f'{os.path.getsize(providedFile)} {providedFile}')
    
    if args.lines:
        
        count = 0

        for line in f:
            count+=1
        
        print(f'{count} {providedFile}')

    if args.words:
        # f = open(providedFile,'r', encoding='utf8')
        count = 0

        for line in f:
            count+=len(line.split())
        
        print(f'{count} {providedFile}')
    
    if args.characters:
        # f = open(providedFile,'r', encoding='utf8')
        count = 0

        for line in f:
            count+=len(line)
        
        print(f'{count} {providedFile}')
    
    if args.characters is False and args.words is False and args.bytes is False and args.lines is False:
        # f = open(providedFile,'r', encoding='utf8')
        lineCount = 0
        wordCount = 0
        characterCount = 0

        for line in f:
            lineCount+=1
            wordCount+=len(line.split())
            characterCount+=len(line)
        
        print(f'{lineCount} {wordCount} {characterCount} {providedFile}')
    
    if args.number is not None:
        print(f'The number you provided is {args.number}')

if __name__ == '__main__':
    main()