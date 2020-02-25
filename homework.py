import os.path


def count_char(fn):
    if os.path.isfile(fn):
        with open(fn,'r') as fh:
            total = 0
            for line in fh:
                total += len(line)
            return total

fn="C:/Users/wangx/Desktop/SES2020spring-master/unit2/readme.md"
fh= open(fn,"r").read()
       
if os.path.isfile(fn):
    number1=count_char(fn)
    line_num = fh.count("\n")
    words_num = len(fh.split())
    print('文件位置:{}\n共有{}个字符\n共有{}行\n共有{}个单词'.format(fn,number1,line_num,words_num))
else:
    print('文件不存在，请检查路径')








