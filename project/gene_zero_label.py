# #读取label,将左上角标记的点转成0.0 0.0

#问题，左上角的标记不太统一，不足够小，有的转成0.0 0.0 失败
#或许读取图片，跟图片的宽度高度结合


import numpy as np
file_name='180502/chwnochineselabel.txt'
count=0
file=open(file_name,'r')
labels=file.readlines()
zero_labels=[]
for l in labels:
    label=l.split(' ')
    if len(label)==34:
        count+=1
        zero_label = ''
        zero_label += label[0]
        zero_label += ' '
        points = np.array(list(map(float, (label[1:-1]))))
        new_points = points.reshape((-1, 2))
        nx = new_points[:, 0]
        ny = new_points[:, 1]
        for i in range(16):
            if (nx[i] > 60 or ny[i] > 60):
                zero_label += str(nx[i])
                zero_label += ' '
                zero_label += str(ny[i])
                zero_label += ' '
            else:
                zero_label += str(0.0)
                zero_label += ' '
                zero_label += str(0.0)
                zero_label += ' '
        zero_labels.append(zero_label)

    else:
        continue


fil=open('./180502zerolabel/caohewen_zero_label.txt','w')
for zl in zero_labels:
    fil.write(str(zl))
    fil.write('\n')

print(count)
