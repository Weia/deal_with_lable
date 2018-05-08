# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 2:09
# @Author  : weic
# @FileName: Main.py
# @Software: PyCharm

import os
import random
import numpy as np
import shutil

import replace_chinese
import gene_zero_label
import gene_mirror_label
def main():
    # files_path='180502'
    # files_name=os.listdir(files_path)



    #修改文件名
    # path = r'D:\数据集\数据集\学生照片'
    # for i in range(4,5):
    #     img_path=path+'\\'+str(i)
    #     replace_chinese.renameImageFile(img_path)

    #修改label名
    # for name in files_name:
    #
    #     replace_chinese.renameLabelName(os.path.join(files_path,name),
    #                              os.path.join(files_path,'noc'+name))

    #验证标记的图片都在文件夹中
    path = r'D:\数据集\数据集\学生照片\train'
    file_path=r'D:\标注文件\merge_all.txt'
    new_file=r'D:\标注文件\train_merge_all.txt'
    count=0

    img_path=path
    imgs_name=os.listdir(img_path)
    with open(new_file) as f:
        contents=f.readlines()
    print(len(contents))
    for content in contents:
        img_name=content.split(' ')[0]
        if img_name in imgs_name:
            count+=1
        else:
            contents.remove(content)
            print(img_name)
    print(len(contents))
    print(count)
    with open(new_file,'w') as f_new:
        f_new.writelines(contents)

    #变换zero_label
    # files_name=os.listdir('nochinese')
    # for file_name in files_name:
    #     label_path='nochinese'+'\\'+file_name
    #     save_path='zero_labels'+'\\'+'zero_'+file_name
    #     gene_zero_label.gene_zero(label_path,save_path)


    #做镜像变换
    # img_path=r'D:\数据集\数据集\学生照片\all'
    # label_path='zero_labels/zero_all.txt'
    # gene_mirror_label.mirror_label_Image(img_path,label_path)

    #产生测试集和训练集

    # label_path='mirror_label/zero_all_mirror.txt'
    # train_path='mirror_label/train.txt'
    # test_path='mirror_label/test.txt'
    # test=[]
    # train=[]
    # with open(label_path) as f_label:
    #     contents=f_label.readlines()
    #
    # index=np.random.randint(0,8246,2000)
    #
    #
    # test=[contents[i] for i in index[:]]
    # train=[contents[i] for i in range(8246) if i not in index[:]]
    #
    # with open(train_path,'w') as f_train:
    #     f_train.writelines(train)
    # with open(test_path,'w') as f_test:
    #     f_test.writelines(test)

    #将测试集的图片另存到其他文件夹
    # imgs_path=r'D:\数据集\数据集\学生照片\all'
    # save_path=r'D:\数据集\数据集\学生照片\test'
    # with open('mirror_label/test.txt') as f_test:
    #     contents=f_test.readlines()
    #     for line in contents:
    #         list_line=line.split(' ')
    #         img_Name=list_line[0]
    #         print(img_Name)
    #         old_path=imgs_path+'\\'+img_Name
    #         new_path=save_path+'\\'+img_Name
    #         try:
    #             shutil.move(old_path, new_path)
    #         except FileNotFoundError:
    #             continue


    pass










if __name__ == '__main__':
    main()
