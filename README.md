## 品牌logo的水印检测demo

本demo使用`labelImg`对`26`张样本图片的水印位置进行标注，[ultralytics-YOLO8](https://github.com/ultralytics/ultralytics)对水印位置进行模型训练&检测。

如果需要使用 [ultralytics-YOLO8](https://github.com/ultralytics/ultralytics) + [IOPaint](https://github.com/Sanster/IOPaint) 进行组合，自动移除yolo识别的目标水印，请点击[yolo8-plus-iopaint](https://github.com/Samge0/yolo8-plus-iopaint)仓库查看。


### 当前开发环境使用的关键依赖版本
```text
python==3.8.18
torch==2.3.0+cu118
torchvision==0.18.0+cu118
ultralytics==8.2.28

# labelImg is used to label the training data
labelImg==1.8.6
```


### 环境配置
- 【推荐】使用vscode的`Dev Containers`模式，参考[.devcontainer/README.md](.devcontainer/README.md)

- 【可选】其他虚拟环境方式
    - 【二选一】安装torch-cpu版
        ```shell
        pip install torch torchvision
        ```
    - 【二选一】安装torch-cuda版
        ```shell
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
        ```
    - 【必要】安装依赖
        ```shell
        pip install -r requirements.txt
        ```


### 训练
```shell
python train.py
```


### 推理
```shell
python test.py
```

### 自定义数据集进行训练：
- 安装`labelImg`
    ```shell
    pip install labelImg
    ```

- 启动`labelImg`
    ```shell
    labelImg
    ```

- 清理或备份旧的数据集，将需要训练的新数据图集放到[datasets/data/images](datasets/data/images)目录，参与训练的图片宽高最好一致，训练前需要在[train.py](train.py)中配置`imgsz`图片宽高信息
- 在`labelImg`打开[datasets/data/images](datasets/data/images)的图集进行标注，保存格式选择`YOLO`（建议点击`File -> YOLO`保存全局默认`YOLO`导出后，重新打开`labelImg`，可在后续保存标注时避免频繁切换导出格式）
- 标注完毕后，执行命令将[datasets/data/images](datasets/data/images)拆分为[datasets/data/train](datasets/data/train)、[datasets/data/test](datasets/data/test)、[datasets/data/val](datasets/data/val)
    ```shell
    cd datasets && python Process.py
    ```
- 按前面文档所示，执行`python train.py`进行训练，执行`python test.py`进行推理


### 相关截图
- labelImg标注界面
![labelImg](https://github.com/Samge0/yolo8-watermark-brand/assets/17336101/c8f9ac72-09f0-4bf7-93f5-e0aa0b20e7ef)

- 训练后的模型预测结果
![output-result](https://github.com/Samge0/yolo8-watermark-brand/assets/17336101/ccdccdc0-8683-499d-bd2b-27948a0fa4f3)