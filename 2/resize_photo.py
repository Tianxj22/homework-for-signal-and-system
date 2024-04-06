#————————对图片进行拉伸和收缩——————————#
import cv2
import numpy as np

def show_img(img, window_name: str, photo_name: str):
    '''显示图片并保存'''
    cv2.imshow(window_name, img)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    cv2.imwrite(f'/home/tianxj/myCode/homework/xinhaoyuxitong/2/graph/operated/{photo_name}_{window_name}.jpg', img)

def sigal_ope(img, photo_name):
    '''对单个图片进行操作的汇总'''
    # 对幅值进行变化
    show_img(img * 2, 'fuzhi_double', photo_name)
    show_img(img / 2, 'fuzhi_half', photo_name)

    # 拉伸和收缩
    wider_img = cv2.resize(img, None, fx=2, fy=1, interpolation=cv2.INTER_LINEAR)
    show_img(wider_img, 'x_double', photo_name)
    thiner_img = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_LINEAR)
    show_img(thiner_img, 'x_half', photo_name)

    # 平移
    height, width = img.shape[:2]
    tx, ty = width / 4, height / 4
    trans_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty]
    ], dtype=np.float32)
    tranlate_img = cv2.warpAffine(img, trans_matrix, dsize=[width, height])
    show_img(tranlate_img, 'pingyi', photo_name)

    # 翻转
    y_fanzhuan = img[::-1,:,:]
    show_img(y_fanzhuan, 'y_fanzhuan', photo_name)
    x_fanzhuan = img[:,::-1,:]
    show_img(x_fanzhuan, 'x_fanzhuan', photo_name)

    # 分割rgb通道
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    show_img(r, 'r', photo_name)
    show_img(g, 'g', photo_name)
    show_img(b, 'b', photo_name)

def double_ope(img1, img2):
    '''对两个图像的处理'''
    addup = cv2.add(img1, img2)
    multi = cv2.multiply(img1, img2)
    show_img(img1 + img2, 'add', 'double')
    show_img(img1 * img2, 'multiply', 'double')
    show_img(addup, 'add_limited', 'double')
    show_img(multi, 'multiply_limited', 'double')

def remove_behind(filename: str):
    '''移除扩展名'''
    pos = filename.find('.')
    return filename[0: pos]
    

photo_name_1 = 'badapple.jpg'
photo_name_2 = 'hhhh.jpeg'

#   读取图片
image1 = cv2.imread(f"/home/tianxj/myCode/homework/xinhaoyuxitong/2/graph/origin/{photo_name_1}")
image2 = cv2.imread(f"/home/tianxj/myCode/homework/xinhaoyuxitong/2/graph/origin/{photo_name_2}")
photo_name_1, photo_name_2 = remove_behind(photo_name_1), remove_behind(photo_name_2)
show_img(image1, 'origin', photo_name_1)
show_img(image2, 'origin', photo_name_2)

#   单个图片的操作
sigal_ope(image1, photo_name_1)
sigal_ope(image2, photo_name_2)

double_ope(image1, image2)

# 将图片尺寸进行修改
# height = 300
# width = 200
# resized_image = cv2.resize(image, [height, width], interpolation=cv2.INTER_LINEAR)

# cv2.imshow('resized', resized_image)
# cv2.waitKey(0)
# cv2.imwrite('/home/tianxj/myCode/homework/xinhaoyuxitong/2/graph/origin/hhhh.jpeg', resized_image)

cv2.destroyAllWindows()