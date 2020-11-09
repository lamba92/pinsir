FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN apt install libgl1-mesa-glx git --no-install-recommends -y
RUN pip install Pillow keras_applications flask flask-cors git+https://github.com/rcmalli/keras-vggface.git

ADD . .

RUN python ./build_vgg_cache.py

EXPOSE 80

CMD ["flask", "run", "-p", "80", "--host=0.0.0.0"]
