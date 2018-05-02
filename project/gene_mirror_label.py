from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
# images_path=r'E:\Project\p2\我们1'
# #labels_path='E:\Project\p2\zero_label.txt'
# names=os.listdir(images_path)
# for name in names:
#
#     image_path=os.path.join(images_path,name)
#     or_image=Image.open(image_path)
#     print(name)
#     (width,height)=or_image.size
#     print(width,height)
    # mirror_image=or_image.transpose(Image.FLIP_LEFT_RIGHT)
    # split_name=name.split('.')[0]
    # print(type(split_name))
    # mirror_image.save('mirror'+split_name+'.jpg')

images_path=r'D:\数据集\数据集\学生照片\1'
labels_path='180502zerolabel/caohewen_zero_label.txt'

# #镜像图片处理label
def mirror_label_Image(images_path,labels_path):
    file_label = open(labels_path, 'r+')
    lines = file_label.readlines()

    for line in lines:
        new_label = ''
        list_line = line.split(' ')
        img_name = list_line[0]
        new_label += ('mirror' + img_name)
        new_label += ' '
        img = Image.open(os.path.join(images_path, img_name))
        mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        mirror_img.save(os.path.join(images_path, 'mirror' + img_name))
        (width, height) = img.size
        print(width, height)
        img_label = np.array(list(map(float, list_line[1:-1])))
        re_img_label = img_label.reshape((-1, 2))
        for j in range(16):
            if re_img_label[j, 0] != 0.0 or re_img_label[j, 1] != 0.0:
                re_img_label[j, 0] = width - re_img_label[j, 0]
        for i in range(16):

            if i == 0 or i == 15:
                new_label += str(re_img_label[i, 0])
                new_label += ' '
                new_label += str(re_img_label[i, 1])
                new_label += ' '
            else:
                if i % 2 == 0:
                    new_label += str(re_img_label[i - 1, 0])
                    new_label += ' '
                    new_label += str(re_img_label[i - 1, 1])
                    new_label += ' '
                else:
                    new_label += str(re_img_label[i + 1, 0])
                    new_label += ' '
                    new_label += str(re_img_label[i + 1, 1])
                    new_label += ' '
        new_label.rstrip()
        file_label.write(new_label)
        file_label.write('\n')
    file_label.close()
    #验证变换
    # label=np.array(list(map(float,new_label.split(' ')[1:-1])))
    # re_label=label.reshape((-1,2))
    # x=re_label[:,0]
    # y=re_label[:,1]
    # plt.imshow(mirror_img)
    #plt.show()





#验证写入

# file_labels=open(labels_path)
# lines=file_labels.readlines()
#
# print(len(lines))
# for line in lines:
#     list_line=line.split(' ')
#     name=list_line[0]
#     if 'mirror' not in name:
#         continue
#     print(name)
#     img_label = np.array(list(map(float, list_line[1:-1])))
#     re_img_label=img_label.reshape(-1,2)
#     img=Image.open(os.path.join(images_path,name))
#     x=re_img_label[:,0]
#     y=re_img_label[:,1]
#     plt.imshow(img)
#     plt.plot(x,y,'r*')
#     plt.show()

