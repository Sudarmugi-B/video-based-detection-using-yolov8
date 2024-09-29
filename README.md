# Video-Based Detection using YOLOv8

This project implements video-based object detection using YOLOv8 and a **Streamlit** interface, allowing users to upload videos and visualize detection results in real-time.

## Features

- **YOLOv8-Based Detection**: Leverages YOLOv8 for efficient and accurate object detection in videos.
- **Streamlit Interface**: Simple and interactive interface built with Streamlit for video uploads and result display.
- **Real-Time Dashboard**: Visualize detection results, including object bounding boxes, directly on the Streamlit dashboard.
- **Database Support**: Save detected frames and user activity to a local SQLite database.

## Project Structure

```bash
├── app.py                # Main Streamlit application file
├── createdb.py           # Script to create the initial database
├── dashboard.py          # Dashboard functionality for displaying video detection
├── helper.py             # Helper functions for video processing
├── login1.py             # User login functionality
├── settings.py           # Configuration and settings for the app
├── setup_database.py     # Initializes and sets up the database
├── detected_frames.db    # Database storing video detection results
├── user_credentials.db   # Database storing user credentials
├── weights/              # YOLOv8 model weights and configuration files
├── videos/               # Directory for storing user-uploaded videos
├── images/               # Directory for storing example images
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Sudarmugi-B/video-based-detection-using-yolov8.git
   cd video-based-detection-using-yolov8
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**: Initialize the database to store user credentials and detected video frames:

   ```bash
   python setup_database.py
   ```

## Usage

1. **Run the Application**: Start the Streamlit application using:

   ```bash
   streamlit run app.py
   ```

2. **Access the Application**: Once the app is running, it will automatically open in your web browser. If not, open the provided local URL (usually `http://localhost:8501/`).

3. **Upload and Detect**:
   * Use the interface to upload your video.
   * The system will process the video using YOLOv8 and display the detection results in real-time.

## YOLOv8 Model

The project uses pre-trained YOLOv8 weights stored in the `weights/` directory. You can update the weights or download newer versions if required from Ultralytics YOLOv8.

## Requirements

Ensure you have all the dependencies by running:

```bash
pip install -r requirements.txt
```

Key libraries include:
* **Streamlit**: For building the web application interface.
* **YOLOv8**: Object detection model.
* **SQLite**: Database for storing detection results and user credentials.

## Example

Here's an example of how object detection looks on an uploaded video:

!([images/yolov8_detection_example.jpg](https://github.com/Sudarmugi-B/video-based-detection-using-yolov8/blob/main/assets/home.png))

*Note: Replace 'images/yolov8_detection_example.jpg' with the path to your actual detection example image.*

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue on GitHub.
