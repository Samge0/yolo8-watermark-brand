#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-05-31 11:03
# describe：
import os
import random
import shutil

def split_dataset(data_dir,train_val_test_dir, train_ratio, val_ratio, test_ratio):
    # 创建目标文件夹
    train_dir = os.path.join(train_val_test_dir, 'train')
    val_dir = os.path.join(train_val_test_dir, 'val')
    test_dir = os.path.join(train_val_test_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # 获取数据集中的所有文件
    files = os.listdir(data_dir)

    # 过滤掉非图片文件
    image_files = [f for f in files if f.endswith('.png')]
    # 随机打乱文件列表
    random.shuffle(image_files)

    # 计算切分数据集的索引
    num_files = len(image_files)
    num_train = int(num_files * train_ratio)
    num_val = int(num_files * val_ratio)
    num_test = num_files - num_train - num_val

    # 分离训练集
    train_files = image_files[:num_train]
    for file in train_files:
        src_image_path = os.path.join(data_dir, file)
        src_label_path = os.path.join(data_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        dst_image_path = os.path.join(train_dir, file)
        dst_label_path = os.path.join(train_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        shutil.copy(src_image_path, dst_image_path)
        shutil.copy(src_label_path, dst_label_path)

    # 分离验证集
    val_files = image_files[num_train:num_train+num_val]
    for file in val_files:
        src_image_path = os.path.join(data_dir, file)
        src_label_path = os.path.join(data_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        dst_image_path = os.path.join(val_dir, file)
        dst_label_path = os.path.join(val_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        shutil.copy(src_image_path, dst_image_path)
        shutil.copy(src_label_path, dst_label_path)

    # 分离测试集
    test_files = image_files[num_train+num_val:]
    for file in test_files:
        src_image_path = os.path.join(data_dir, file)
        src_label_path = os.path.join(data_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        dst_image_path = os.path.join(test_dir, file)
        dst_label_path = os.path.join(test_dir, file.replace('.png', '.txt').replace('.png', '.txt'))
        shutil.copy(src_image_path, dst_image_path)
        shutil.copy(src_label_path, dst_label_path)

    print("数据集分离完成！")
    print(f"训练集数量：{len(train_files)}")
    print(f"验证集数量：{len(val_files)}")
    print(f"测试集数量：{len(test_files)}")

def move_files(data_dir):
    # 创建目标文件夹
    images_dir = os.path.join(data_dir, 'images')
    labels_dir = os.path.join(data_dir, 'labels')
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)

    # 获取数据集中的所有文件
    files = os.listdir(data_dir)

    # 移动PNG文件到images文件夹
    png_files = [f for f in files if f.endswith('.png')]
    for file in png_files:
        src_path = os.path.join(data_dir, file)
        dst_path = os.path.join(images_dir, file)
        shutil.move(src_path, dst_path)

    # 移动TXT文件到labels文件夹
    txt_files = [f for f in files if f.endswith('.txt')]
    for file in txt_files:
        src_path = os.path.join(data_dir, file)
        dst_path = os.path.join(labels_dir, file)
        shutil.move(src_path, dst_path)

    print(f"{data_dir}文件移动完成！")
    print(f"总共移动了 {len(png_files)} 个png文件到images文件夹")
    print(f"总共移动了 {len(txt_files)} 个TXT文件到labels文件夹")


# 设置数据集路径和切分比例
data_dir = './data/images'      # 图片和标签路径
train_val_test_dir= './data'    # 目标文件夹
train_ratio = 0.7               # 训练集比例
val_ratio = 0.2                 # 验证集比例
test_ratio = 0.1                # 测试集比例

# 调用函数分离数据集
split_dataset(data_dir, train_val_test_dir,train_ratio, val_ratio, test_ratio)
# 调用函数移动文件
move_files(os.path.join(train_val_test_dir, 'train'))
move_files(os.path.join(train_val_test_dir, 'val'))
move_files(os.path.join(train_val_test_dir, 'test'))

