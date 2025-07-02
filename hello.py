print('Hello Git')

print('版本3：又添加了新能')

import numpy as np
import cv2
from utils import preprocess_image, save_result
from config import CONFIG

class ImageProcessor:
    def __init__(self):
        self.config = CONFIG
        self.images = []
    
    def load_image(self, path):
        """加载图像"""
        try:
            img = cv2.imread(path)
            if img is None:
                raise ValueError(f"无法加载图像: {path}")
            return img
        except Exception as e:
            print(f"错误: {e}")
            return None
    
    def process_batch(self, image_paths):
        """批量处理图像"""
        results = []
        for path in image_paths:
            img = self.load_image(path)
            if img is not None:
                processed = preprocess_image(img)
                results.append(processed)
        return results
    
    def run(self):
        """主运行函数"""
        print("开始处理图像...")
        # TODO: 实现主逻辑
        pass

if __name__ == "__main__":
    processor = ImageProcessor()
    processor.run()