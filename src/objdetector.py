import argparse
import sys
import time

import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#from utils import visualize
from picamera2 import Picamera2


# COUNTER, FPS = 0, 0
# START_TIME = time.time()
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
detection_result_list = []
final_result = []
def run(model: str, max_results: int, score_threshold: float, 
        camera_id: int, width: int, height: int) -> None:
    global detection_result_list,final_result
    # row_size = 50  # pixels
    # left_margin = 24  
    # text_color = (0, 0, 0)  #
    # font_size = 1
    # font_thickness = 1
    # fps_avg_frame_count = 10

    #detection_frame = None
    detection_result_list = []

    def save_result(result: vision.ObjectDetectorResult, unused_output_image: mp.Image, timestamp_ms: int):
        # global FPS, COUNTER, START_TIME

        # if COUNTER % fps_avg_frame_count == 0:
        #     FPS = fps_avg_frame_count / (time.time() - START_TIME)
        #     START_TIME = time.time()

        detection_result_list.append(result)
        
        #COUNTER += 1

    base_options = python.BaseOptions(model_asset_path=model)
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                            running_mode=vision.RunningMode.LIVE_STREAM,
                                            max_results=max_results, score_threshold=score_threshold,
                                            result_callback=save_result)
    detector = vision.ObjectDetector.create_from_options(options)



    while (1):
        im= picam2.capture_array()  

        image=cv2.resize(im,(640,480))
        #image = cv2.flip(image, -1)


        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)


        detector.detect_async(mp_image, time.time_ns() // 1_000_000)


        # fps_text = 'FPS = {:.1f}'.format(FPS)
        # text_location = (left_margin, row_size)
        # current_frame = image
        # cv2.putText(current_frame, fps_text, text_location, cv2.FONT_HERSHEY_DUPLEX,
        #             font_size, text_color, font_thickness, cv2.LINE_AA)

        if detection_result_list:
            final_result.extend([detection_result_list[0].detections[0].categories[0].category_name,
                            detection_result_list[0].detections[0].categories[0].score,
                            [detection_result_list[0].detections[0].bounding_box.origin_x,
                             detection_result_list[0].detections[0].bounding_box.origin_y,
                             detection_result_list[0].detections[0].bounding_box.width,
                             detection_result_list[0].detections[0].bounding_box.height]])
            #print(detection_result_list)
            #current_frame = visualize(current_frame, detection_result_list[0])
            #detection_frame = current_frame
            time.sleep(0.2)
            detection_result_list.clear()
            final_result.clear()

        # if detection_frame is not None:
        #     cv2.imshow('object_detection', detection_frame)

        # if cv2.waitKey(1) == 27:
        #     break

    detector.close()
    #cap.release()
    #cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--model',
        help='Path of the object detection model.',
        required=False,
        default='detection_model.tflite')
    parser.add_argument(
        '--maxResults',
        help='Max number of detection results.',
        required=False,
        default=1)
    parser.add_argument(
        '--scoreThreshold',
        help='The score threshold of detection results.',
        required=False,
        type=float,
        default=0.25)
    parser.add_argument(
        '--cameraId', help='Id of camera.', required=False, type=int, default=0)
    parser.add_argument(
        '--frameWidth',
        help='Width of frame to capture from camera.',
        required=False,
        type=int,
        default=640)
    parser.add_argument(
        '--frameHeight',
        help='Height of frame to capture from camera.',
        required=False,
        type=int,
        default=480)
    args = parser.parse_args()

    run(args.model, int(args.maxResults),
        args.scoreThreshold, int(args.cameraId), args.frameWidth, args.frameHeight)


if __name__ == '__main__':
    main()