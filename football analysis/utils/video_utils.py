
import cv2
INPUT_VIDEO_PATH = "/home/ahmed/football analysis/input_videos/08fd33_4.mp4"
OUTPUT_VIDEO_PATH = "/home/ahmed/football analysis/output_videos/output_video.avi"
def read_video(video_path):
    frames = []
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")
    
    print(f"Opened video file: {video_path}")
    print(f"Frame width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    print(f"Frame height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print(f"Frame count: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}")
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("No more frames to read or failed to read frame.")
                break
            frames.append(frame)
    finally:
        cap.release()
    
    return frames

    
def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        raise ValueError("The list of video frames is empty.")
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_height, frame_width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (frame_width, frame_height))
    
    # Write each frame to the video
    for frame in output_video_frames:
        out.write(frame)
    
    # Release the VideoWriter object
    out.release()
