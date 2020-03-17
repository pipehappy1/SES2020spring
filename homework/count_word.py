def count_char(file):
       import os.path
       if os.path.isfile(file):
          with open(file,'r') as  opf:
            total =0
            for line in opf:
             for char in('#','\n'):
               line=line.replace(char," ")
               word=line.split()
               total +=len(word)
             return total
