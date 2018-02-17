FROM python:3.5
# create a directory and change working directory
WORKDIR /src
# copy requirements file to the working directory
ADD src/requirements.txt requirements.txt
# install packages in the requirements file
RUN pip install -r requirements.txt
# Set the timezone
RUN echo "Asia/Tokyo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
# copy project directory
ADD src /src
# expose 8000 port on the container
EXPOSE 5000
CMD ["python", "rolling-update.py"]
