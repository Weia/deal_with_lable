#生成label，如果是不合规图片手动去修改flag+1
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pylab import *
from PIL import Image
import os
import csv
#获取图片名
img_path=r'E:\视频资料\sample\front'
names=os.listdir(img_path)

#获取上次处理的步数
flag_path='./flag.txt'
flag_file=open(flag_path)
flag=flag_file.read()
step=int(flag)
    #step=int(f[0])
flag_file.close()

labels=[]#生成的label集合



try:
    for name in names[step:]:
        step += 1
        label=[]
        label.append(name)
        img=array(Image.open(os.path.join(img_path,name)))
        plt.imshow(img)
        x=ginput(16,timeout=-1)
        for m in x:
            label.append(m[0])
            label.append(m[1])
        labels.append(label)
finally:
    # 将labels写入文件
    save_path = './label.csv'
    file = open(save_path, 'a',newline='')
    csv_writer = csv.writer(file)
    for l in labels:
        csv_writer.writerow(l)
    file.close()

    save_flag = open(flag_path, 'w')
    save_flag.write(str(step))
    save_flag.close()


