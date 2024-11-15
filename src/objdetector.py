import cv2
from picamera2 import Picamera2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

final_result = []
def main():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (640,480)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()
    base_options = python.BaseOptions(model_asset_path='efficientdet_lite0.tflite')
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                        score_threshold=0.25,max_results=1)
    detector = vision.ObjectDetector.create_from_options(options)
    global final_result

    while 1:
        image = picam2.capture_array()
        image = cv2.resize(image,(640,480))
        image = cv2.flip(image,-1)
        image = mp.Image(data=image,image_format=mp.ImageFormat.SRGB)
        detection_result = detector.detect(image)
        if(detection_result.detections):
            final_result = [detection_result.detections[0].categories[0].category_name,
                                    detection_result.detections[0].categories[0].score,
                                    [detection_result.detections[0].bounding_box.origin_x,
                                    detection_result.detections[0].bounding_box.origin_y,
                                    detection_result.detections[0].bounding_box.width,
                                    detection_result.detections[0].bounding_box.height]]
