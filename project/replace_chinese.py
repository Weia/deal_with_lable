# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 14:02
# @Author  : weic
# @FileName: replace_chinese.py
# @Software: PyCharm

import os
import re
path=r'D:\数据集\数据集\学生照片\1'


#修改文件名
def renameImageFile(path):
    files = os.listdir(path)
    count=0
    for ori_name in files:

        pattern=re.compile(u'[\u4e00-\u9fa5]+')
        words=pattern.findall(ori_name)
        if len(words):
            count+=1
            new_name=ori_name
            for i in range(len(words)):
                new_name=new_name.replace(words[i],'Image')
            os.rename(path+'\\'+ori_name,path+'\\'+new_name)
            #print('change')
    print('modify %d'%(count))

#修改label中的文件名
label_file = '180502/labelhzh.txt'
save_file_name = '180502/noclabelhzh.txt'

def renameLabelName(label_file,save_file_name):
    new_content = []
    count=0
    with open(label_file,'r') as f:

        content = f.readlines()
        for line in content:
            print(line)
            list_line = line.split(' ')
            name = list_line[0]
            pattern = re.compile(u'[\u4e00-\u9fa5]+')
            words = pattern.findall(name)
            if len(words):
                count+=1
                new_name = name
                for i in range(len(words)):
                    new_name = new_name.replace(words[i], 'Image')
                list_line[0] = new_name
            new_line = ' '.join(list_line)
            new_content.append(new_line)
        print('modify %d'%(count))
    with open(save_file_name, 'w') as f:
        f.writelines(new_content)

# renameLabelName(label_file,save_file_name)



