FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN mkdir /data
RUN mkdir -pv /code/data/local_pic
RUN mkdir -pv /code/data/logs
RUN mkdir -pv /code/data/user_pic
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install --upgrade pip
RUN pip install redis flask
RUN pip install Pillow
RUN pwd
RUN ls -alhrt
RUN ls -alhrt
CMD ["python", "pic.py"]