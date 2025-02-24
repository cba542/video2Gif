import cv2
from PIL import Image

def video_to_gif(input_path, output_path, fps=15, scale=0.5, max_frames=100, frame_skip=1):
    cap = cv2.VideoCapture(input_path)
    frames = []
    count = 0
    total_frames = 0

    while cap.isOpened() and total_frames < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        # 跳帧处理
        if count % (frame_skip + 1) != 0:
            count += 1
            continue
        # 调整尺寸
        if scale:
            h, w = frame.shape[:2]
            new_size = (int(w * scale), int(h * scale))
            frame = cv2.resize(frame, new_size)
        # 颜色转换 BGR → RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        frames.append(img)
        total_frames += 1
        count += 1

    cap.release()

    # 保存为优化后的 GIF
    if frames:
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=int(1000 / fps),
            loop=0,
            optimize=True,
            disposal=2,
        )

videoPath = r"video.mp4"

video_to_gif(videoPath, "output.gif", fps=12, scale=0.5, max_frames=80, frame_skip=2)