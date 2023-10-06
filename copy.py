# coding=utf-8
####王DRO的選修3.14功課_複製檔案
####by:WHY/2023.3.13

filenames = input("請輸入欲拷貝之原始檔案及目標檔名：(用空白鍵隔開)：").split()
old, new = filenames[0],filenames[1]

def copy(old,new):
    fr_old = open(old, 'r', encoding="utf-8")
    fr_new = open(new,'w')
    for line in fr_old:
        fr_new.write(line)
    fr_old.close()
    fr_new.close()

copy(old, new)

