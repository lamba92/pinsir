FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN apt install libgl1-mesa-glx git --no-install-recommends -y
RUN pip install Pillow keras_applications grpcio git+https://github.com/rcmalli/keras-vggface.git

ENV TF_FORCE_GPU_ALLOW_GROWTH=1

ADD . .
ENV PORT=50051
EXPOSE 50051

CMD python app.py
