FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN pip install Pillow mtcnn grpcio
RUN apt install libgl1-mesa-glx --no-install-recommends -y

ADD . .
ENV TF_FORCE_GPU_ALLOW_GROWTH=1
ENV PORT=50051
EXPOSE 50051

CMD python app.py
