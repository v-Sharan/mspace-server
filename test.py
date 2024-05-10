from flask import Flask, Response
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# RTSP stream URL
RTSP_URL = "rtsp://192.168.1.168:554/main"


def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )


@app.route("/")
def index():
    return "RTSP Stream Server"


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
