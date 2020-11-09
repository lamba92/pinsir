FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN pip install Pillow flask mtcnn flask-cors
RUN apt install libgl1-mesa-glx --no-install-recommends -y

ADD . .

EXPOSE 80

CMD ["flask", "run", "-p", "80", "--host=0.0.0.0"]
