import os
from PIL import Image
import matplotlib.pyplot as plt
import  numpy as np
file_name='180502/labelwxw.txt'
image_path=r'D:\数据集\数据集\学生照片\4'
file=open(file_name)
labels=file.readlines()
for l in labels:
    label=l.split(' ')
    print(len(label))

    if(len(label)>=33):
        name=label[0]
        print(name)
        points=np.array(list(map(float,(label[1:-1]))))
        image=Image.open(os.path.join(image_path,name))
        print(points)
        new_points=points.reshape((-1,2))
        nx=new_points[:,0]
        ny=new_points[:,1]
        # print(len(nx))
        # x=[]
        # y=[]
        # for i in range(16):
        #     if(nx[i]>50 or ny[i]>100):
        #         x.append(nx[i])
        #         y.append(ny[i])


        # print(x[np.argmax(x)],y[np.argmax(y)])
        # plt.axis([x[np.argmin(x)],x[np.argmax(x)]+200,y[np.argmax(y)]+200,y[np.argmin(y)]])
    #plt.axes()
        plt.imshow(image)
        plt.plot(nx,ny,'r*')
        plt.show()
    else:
        continue



