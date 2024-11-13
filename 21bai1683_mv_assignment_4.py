# -*- coding: utf-8 -*-
"""21BAI1683 MV Assignment 4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1irwRwwV9hlx4DFG1RkJ3yXnukYaf7tP2
"""

import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

video_path = "/content/MV Assignment 4 recording.mp4"
frames = []
for frame in iio.imiter(video_path):
    frames.append(np.array(frame))

motion_threshold = 10000
event_frames = []
timestamps = []
fps = 24

def frame_difference(prev_frame, curr_frame):
    diff_frame = np.abs(prev_frame.astype(np.int16) - curr_frame.astype(np.int16))
    return np.sum(diff_frame)

for i in range(1, len(frames)):
    prev_frame = frames[i - 1]
    curr_frame = frames[i]

    motion_intensity = frame_difference(prev_frame, curr_frame)

    if motion_intensity > motion_threshold:
        event_frames.append(curr_frame)
        timestamps.append(i / fps)

print("Events detected at the following timestamps (seconds):")
print(timestamps)

for i, event_frame in enumerate(event_frames):
    plt.figure()
    plt.imshow(event_frame)
    plt.title(f"Event at {timestamps[i]:.2f} seconds")
    plt.axis('off')
plt.show()