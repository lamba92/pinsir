import tensorflow as tf
import logging

from flask_cors import CORS

from detector_app import DetectorApp

try:
    tf.config.set_visible_devices([], 'GPU')
    visible_devices = tf.config.get_visible_devices()
    for device in visible_devices:
        assert device.device_type != 'GPU'
except:
    pass

app = DetectorApp(__name__)
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG

if __name__ == '__main__':
    app.run(host="localhost", port=8080)
