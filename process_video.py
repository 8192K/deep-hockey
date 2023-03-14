from ultralytics import YOLO
import supervision as sv

def main():
    model = YOLO('./data/yolo/runs/detect/medium/weights/best.pt')

    box_annotator = sv.BoxAnnotator(
        thickness=1,
        text_thickness=1,
        text_scale=0.5
    )

    SOURCE_PATH = './data/vid/eck_ecn_excerpt.mp4'
    TARGET_PATH = './data/vid/eck_ecn_excerpt_annotated.mp4'

    video_info = sv.VideoInfo.from_video_path(SOURCE_PATH)

    with sv.VideoSink(TARGET_PATH, video_info) as sink:
        for result in model.track(source=SOURCE_PATH, show=False, stream=True):
            frame = result.orig_img
            detections = sv.Detections.from_yolov8(result)

            if result.boxes.id is not None:
                detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

            labels = [
                f"#{tracker_id} {confidence:0.2f}"
                for _, confidence, _, tracker_id in detections
            ]

            frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)

            sink.write_frame(frame)

if __name__ == '__main__':
    main()
