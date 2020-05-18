import os.path
def count_char(fn):
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            for line in fh:
                total += len(line)
            return total


fn = "D:/chromium/SES2020spring-master/SES2020spring-master/unit2/readme.md"
fh = open(fn, "r").read()

if os.path.isfile(fn):
    char_num = count_char(fn)
    line_num = fh.count("\n")
    words_num = len(fh.split())
    print('文件地址:{}\n字符共{}个\n行：{}\n单词共{}个'.format(fn, char_num, line_num, words_num))
else:
    print('路径错误')