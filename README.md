# 🎥 Video Frame Comparison App (MSE & SSIM)

This is a simple and interactive **Streamlit web app** for comparing frames from two video files — typically a **FAKE** and a **REAL** version — using two image similarity metrics:

- **MSE (Mean Squared Error)**
- **SSIM (Structural Similarity Index)**

---
## check here ()
## 🚀 Features

- Upload two video files (e.g., `.mp4`, `.avi`)
- Automatically extract frames from each video
- Compare the same frame index from both videos
- View similarity results (MSE & SSIM) and frame previews side-by-side
- All in a browser-based interface powered by [Streamlit](https://streamlit.io)

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

### requirements.txt includes:

- streamlit
- numpy
- opencv-python
- matplotlib
- scikit-image
- Pillow

### ▶️ How to Run
1. Clone or download the project files.

2. Save your app code as video_frame_compare.py

3. Then run the app with:

- streamlit run video_frame_compare.py
4. Upload your FAKE and REAL video files in the UI.

5. Use the slider to select a frame index and compare results.

### 🖼️ Output Example
- MSE gives a numerical difference between frames (lower is better).

- SSIM gives a similarity score (closer to 1 is more similar).
* MSE: 1523.77
* SSIM: 0.63

### To-Do (Ideas)
 - Auto-compare all frames & plot SSIM over time

 - Face detection on each frame (e.g., MTCNN)

 - Export similarity results to CSV or PDF

 - Compare resized/normalized frames for robustness

##### 👤 Author
- Made with ❤️ using Streamlit and OpenCV

