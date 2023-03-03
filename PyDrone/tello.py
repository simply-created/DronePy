from flask import Flask, Blueprint, render_template, Response
from djitellopy import Tello
from cv2 import VideoCapture, imencode


tello = Blueprint(__name__, 'tello')
cap = VideoCapture(0)


@tello.route('/')
def telloTest():
    return render_template('tello.html')


@tello.route('/connect')
def test0():
    print('connecting')
    dji = Tello()
    dji.connect()
    return "printed string 1 to console"


@tello.route('/takeOff')
def test1():
    print('takeOff')
    dji = Tello()
    dji.takeoff()
    return "printed string 2 to console"


@tello.route('/land')
def test2():
    print('land')
    dji = Tello()
    dji.land()
    return "printed string 3 to console"


def update_frames():
    # https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        else:
            ret, buffer = imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Updates each frame
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )


@tello.route('/stream')
def stream():
    print('stream')
    # dji = Tello()
    return Response(update_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
