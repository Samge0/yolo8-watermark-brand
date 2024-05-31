## 品牌logo的水印检测demo

使用`labelImg`对水印位置进行标注，[ultralytics-YOLO8](https://github.com/ultralytics/ultralytics)对水印位置进行模型训练&检测。


### 当前开发环境使用的关键依赖版本
```text
python==3.8.18
torch==2.1.1+cu118
torchvision==0.16.1+cu118
ultralytics==8.2.26
labelImg==1.8.6
```


### 安装依赖
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

- 清理或备份旧的数据集，将需要训练的新数据图集放到[datasets/data/images](datasets/data/images)目录
- 在`labelImg`打开[datasets/data/images](datasets/data/images)的图集进行标注，保存格式选择`YOLO`（建议点击`File>YOLO`保存全局的默认`YOLO`导出再重新打开`labelImg`，可减少后续保存标注时频繁切换导出格式）
- 标注完毕后，执行命令将[datasets/data/images](datasets/data/images)拆分为[datasets/data/train](datasets/data/train)、[datasets/data/test](datasets/data/test)、[datasets/data/val](datasets/data/val)
    ```shell
    cd datasets && python Process.py
    ```
- 按前面文档所示，执行`python train.py`进行训练，执行`python test.py`进行推理