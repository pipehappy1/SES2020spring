def word_count(fn):
    import os.path
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            for line in fh:
                total += len(line.split())
                return total
    else: 
        print('file not found')
word_count('C:\Users\lzl\Desktop\git102\SES2020spring\unit2\readme.md')