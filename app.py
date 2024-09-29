from pathlib import Path
import PIL
import streamlit as st
import sqlite3
import settings
import helper

  # Setting page layout
st.set_page_config(
    page_title="NeuraScan 🕵🏽‍♀️",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("NeuraScan🕵🏽")

# Sidebar
st.sidebar.header("ML Model Config")

# Model Options
model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model_path = Path(settings.DETECTION_MODEL)
elif model_type == 'Segmentation':
    model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

# Sidebar options for Image, Video, Webcam, etc.
source_radio = st.sidebar.radio("Select Source", settings.SOURCES_LIST)

# Database setup
def setup_database():
    conn = sqlite3.connect('detected_frames.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detected_frames (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frame_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

setup_database()  # Call the function to set up the database

# Image source handling
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)

    # Display uploaded image or default images
    with col1:
        if source_img is None:
            default_image_path = str(settings.DEFAULT_IMAGE)
            default_image = PIL.Image.open(default_image_path)
            st.image(default_image, caption="Default Image",
                     use_column_width=True)
        else:
            uploaded_image = PIL.Image.open(source_img)
            st.image(uploaded_image, caption="Uploaded Image",
                     use_column_width=True)

    # Display detected image or default detected image
    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image, conf=confidence)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                            # Store the detected frame name in the database
                            conn = sqlite3.connect('detected_frames.db')
                            cursor = conn.cursor()
                            cursor.execute('INSERT INTO detected_frames (frame_name) VALUES (?)', (source_img.name,))
                            conn.commit()
                            conn.close()
                except Exception as ex:
                    st.write("No image is uploaded yet!")

# Video, Webcam, RTSP, and YouTube source handling
elif source_radio in [settings.VIDEO, settings.WEBCAM, settings.RTSP, settings.YOUTUBE]:
    if source_radio == settings.VIDEO:
        helper.play_stored_video(confidence, model)
    elif source_radio == settings.WEBCAM:
        helper.play_webcam(confidence, model)
    elif source_radio == settings.RTSP:
        helper.play_rtsp_stream(confidence, model)
    elif source_radio == settings.YOUTUBE:
        helper.play_youtube_video(confidence, model)

# Invalid source type
else:
    st.error("Please select a valid source type!")