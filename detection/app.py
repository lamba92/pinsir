import tensorflow as tf
import logging

from detector_app import DetectorApp

try:
    tf.config.set_visible_devices([], 'GPU')
    visible_devices = tf.config.get_visible_devices()
    for device in visible_devices:
        assert device.device_type != 'GPU'
except:
    pass

app = DetectorApp(__name__)
logging.getLogger('flask_cors').level = logging.DEBUG
