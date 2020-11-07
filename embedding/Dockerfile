FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN apt install libgl1-mesa-glx git --no-install-recommends -y
RUN pip install keras_applications flask flask-cors git+https://github.com/rcmalli/keras-vggface.git

ADD . .

RUN python ./build_vgg_cache.py

EXPOSE 8080

CMD ["flask", "run", "-p", "8080", "--host=0.0.0.0"]
