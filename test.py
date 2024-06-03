#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-05-31 11:03
# describe：
from PIL import Image
from ultralytics import YOLO
import os, time

# Run inference
def _inference(input_path: str, output_path: str):
    results = model(input_path, conf=0.75)  # filter values with confidence level > 0.75
    # Show the results
    for r in results:
        im_array = r.plot(boxes=r.boxes)  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save(output_path)  # save image


# Run inference batch
def _test_batch(batch_dir: str):
    file_list = os.listdir(batch_dir)
    total_size = len(file_list)
    for i in range(total_size):
        filename = file_list[i]
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            try:
                input_path = os.path.join(batch_dir, filename).replace(os.sep, "/")
                output_path = os.path.join(output_dir, f"{filename.split('.')[0]}.jpg").replace(os.sep, "/")
                print(f"【{i+1}/{total_size}】 is running: {input_path} => {output_path}")
                start_date = time.time()
                _inference(input_path, output_path)
                _print_date_info("inference takes time", start_date)
            except Exception as e:
                pass


def _print_date_info(tag: str, start_date):
    elapsed_time = time.time() - start_date
    print(f"{tag}: {elapsed_time:.2f}s")


if __name__ == "__main__":
    # Load model
    start_date = time.time()
    model_path = "runs/detect/train/weights/last.pt"    # customize the trained model, you need to execute `python training py` to get it first
    # model_path = "result-weights/last.pt"     # with the demo model submitted by this branch, it can be run directly
    print(f"Load model: {model_path}")
    model = YOLO(model_path)
    _print_date_info(f"Load model: {model_path} success, time consuming", start_date)

    output_dir = ".cache/output"
    os.makedirs(output_dir, exist_ok=True)

    # inference one
    _inference("test.png", f"{output_dir}/test.png")

    # inference batch
    batch_dir = "datasets/data/val/images"
    _test_batch(batch_dir=batch_dir)
    
    print("all done")