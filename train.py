#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-05-31 11:03
# describe：
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# 配置训练参数 https://docs.ultralytics.com/zh/modes/train/#train-settings
train_config = {
    "data": "data-brand.yaml",  # 训练数据配置信息
    "epochs": 50,               # 训练批次
    "imgsz": 288,               # 指定输入图像的大小。合理配置 imgsz 参数可以显著影响模型的性能和准确性，默认值为640，这里的288是因为参与训练的图片尺寸(260, 160)与32倍数最接近的就是288
    "device": 0,                # cuda的设备号
    "workers": 0,               # 增加数据加载的工作线程数，提高数据加载速度
    "batch": 6,                 # 训练批次，-1为动态调整

    "hsv_h": 0.0,               # 禁用色调调整。注：因为这里水印比较淡，不禁用的话可能因色值变化导致水印消失，影响模型效果
    "hsv_s": 0.0,               # 禁用饱和度调整。注：因为这里水印比较淡，不禁用的话可能因色值变化导致水印消失，影响模型效果
    "hsv_v": 0.0,               # 禁用亮度调整。注：因为这里水印比较淡，不禁用的话可能因色值变化导致水印消失，影响模型效果
    # "degrees": 0.0,               # 禁用旋转
    # "translate": 0.1,             # 启用平移，但幅度较小
    # "scale": 0.0,                 # 禁用缩放
    # "shear": 0.0,                 # 禁用剪切
    # "perspective": 0.0,           # 禁用透视变换
    # "flipud": 0.0,                # 禁用上下翻转
    # "fliplr": 0.5,                # 保持左右翻转的默认值
    # "mosaic": 0.0,                # 禁用马赛克
    # "mixup": 0.0,                 # 禁用混合图像
    # "copy_paste": 0.0,            # 禁用复制粘贴
    # "auto_augment": "",           # 禁用自动增强策略
    # "erasing": 0.0,               # 禁用随机擦除
    # "crop_fraction": 1.0,         # 保持裁剪比例
}
model.train(**train_config)
