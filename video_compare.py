import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from pathlib import Path
from skimage.metrics import structural_similarity as ssim
from PIL import Image

# ---------- Helper: Save uploaded file to disk ----------
def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

# ---------- Extract frames from video ----------
def extract_frames(video_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_file)
    i = 1

    if not cap.isOpened():
        st.error(f"❌ Error opening video file: {video_file}")
        return []

    frames = []
    while True:
        ret, frame = cap.read()
        if ret:
            frame_path = os.path.join(output_folder, f"{i}.jpg")
            cv2.imwrite(frame_path, frame)
            frames.append(frame_path)
            i += 1
        else:
            break
    cap.release()
    return frames

# ---------- MSE ----------
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

# ---------- MSE + SSIM ----------
def compare_images(imageA, imageB):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return m, s

# ---------- Load image in grayscale ----------
def load_gray_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

# ---------- Streamlit App UI ----------
st.title("🎥 Video Frame Comparison using MSE & SSIM")

fake_video = st.file_uploader("📁 Upload FAKE video", type=["mp4", "avi", "mov"])
real_video = st.file_uploader("📁 Upload REAL video", type=["mp4", "avi", "mov"])

if fake_video and real_video:
    # Save videos to disk
    saved_fake_path = save_uploaded_file(fake_video, "uploaded_fake_video.mp4")
    saved_real_path = save_uploaded_file(real_video, "uploaded_real_video.mp4")

    # Extract frames
    fake_frames_dir = "temp_fake_frames"
    real_frames_dir = "temp_real_frames"

    st.info("🔄 Extracting frames from uploaded videos...")
    fake_frames = extract_frames(saved_fake_path, fake_frames_dir)
    real_frames = extract_frames(saved_real_path, real_frames_dir)

    if fake_frames and real_frames:
        st.success(f"✅ Extracted {len(fake_frames)} fake and {len(real_frames)} real frames")

        # Select frame index
        index = st.slider("🎯 Select Frame Index to Compare", 1, min(len(fake_frames), len(real_frames)))

        # Load and compare selected frames
        imageA = load_gray_image(fake_frames[index - 1])
        imageB = load_gray_image(real_frames[index - 1])

        m, s = compare_images(imageA, imageB)

        st.subheader(f"🔍 Comparison for Frame {index}")
        st.write(f"📊 **Mean Squared Error (MSE)**: `{m:.2f}`")
        st.write(f"📈 **Structural Similarity Index (SSIM)**: `{s:.2f}`")

        # Display side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(imageA, caption="🟥 Fake Video Frame", use_column_width=True, channels="GRAY")
        with col2:
            st.image(imageB, caption="🟩 Real Video Frame", use_column_width=True, channels="GRAY")

    else:
        st.warning("⚠️ Could not extract frames. Please check the uploaded videos.")

else:
    st.info("📌 Please upload both a FAKE and a REAL video.")
