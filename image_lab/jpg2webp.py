# coding: utf-8
# @date: 2020-01-02

"""
jpg 图片转 webp
"""


import os
import shutil
from PIL import Image


def get_file_size(file_path):
    return round(os.path.getsize(file_path) / 1000)


quality_list = [10, 30, 50, 75]

lossless = False

image_list = [
    # "/Users/xxx/1/1/1_1_0b22a814e0aa71ff.jpg",  # 黑白
    # "/Users/xxx/58/135/58_135_07db382a7cbd4544.jpg",  # 黑白
    # "/Users/xxx/80/7/80_7_77c41c9766070a1e.jpg",  # 黑白
    # "/Users/xxx/15/7/15_7_702d51e27f03215e.jpg",
    # "/Users/xxx/86/53/86_53_35866b6ab3fbb3f0.jpg",
    # "/Users/xxx/149/11/149_11_7bf6a579fddbfdfd.jpg"
    "/Users/xxx/19/79/19_79_8888173ca7b8baea.jpg"
]

output_path = "/Users/xxx/python_lab/webp/"

with open(output_path + "stat.txt", 'a') as fw:
    for image in image_list:
        compress_ratio_list = [] # 压缩率

        text_list = image.split("/")
        gid = text_list[6]
        jpg_filename = text_list[-1]
        if lossless:
            jpg_filename = jpg_filename.split(".")[0] + "_lossless." + jpg_filename.split('.')[1]
        webp_filename = jpg_filename.split(".")[0] + ".webp"

        webp_output_path = output_path + str(gid) + "/"
        if lossless:
            webp_output_path = webp_output_path + "lossless/"

        if not os.path.exists(webp_output_path):
            os.makedirs(webp_output_path)
        shutil.copyfile(image, webp_output_path + jpg_filename)
        origin_size = get_file_size(webp_output_path + jpg_filename)
        print("origin_size", origin_size)

        for quality in quality_list:
            im = Image.open(image)
            webp_image_path = webp_output_path + "{0}_{1}".format(quality, webp_filename)
            im.save(webp_image_path, 'webp', quality=quality, lossless=lossless)
            new_size = get_file_size(webp_image_path)
            print("new_size", new_size)
            compress_ratio = round((origin_size - new_size) / origin_size * 100, 2)
            print(compress_ratio)
            compress_ratio_list.append(compress_ratio)

        compress_ratio_list = [str(ratio) + "%" for ratio in compress_ratio_list]
        compress_ratio_list.insert(0, jpg_filename)
        result = ", ".join(compress_ratio_list)
        fw.write(result + '\n')

