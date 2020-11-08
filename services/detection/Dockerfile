FROM tensorflow/tensorflow:2.4.0rc0-gpu

RUN pip install flask mtcnn flask-cors
RUN apt install libgl1-mesa-glx --no-install-recommends -y

ADD . .

EXPOSE 8080

CMD ["flask", "run", "-p", "8080", "--host=0.0.0.0"]
