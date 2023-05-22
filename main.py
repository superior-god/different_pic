# -*- coding: utf-8 -*-
# @Time:    2023-05-22 09:23
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    main.py
# @Project: different_pic
# @Package: 
# @Ref:

from PIL import Image
from PIL import ImageChops

def compare_images(path_one, path_two, diff_save_location):#文件1的路径，文件2的路径，生成比较后不同的图片文件路径
  image_one = Image.open(path_one)
  image_two = Image.open(path_two)

  try:
    diff = ImageChops.difference(image_one, image_two)
    if diff.getbbox() is None:
    # 图片间没有任何不同则直接退出
      print("We are the same!")

    else:
      print(diff.getbbox())
      diff.save(diff_save_location)

  except ValueError as e:
    text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
        "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
        "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
        "image must match the size of the region.使用2纬的box避免上述问题")
    print("【{0}】{1}".format(e,text))

if __name__ == '__main__':
  compare_images('10.jpg','11.jpg','12.jpg')

