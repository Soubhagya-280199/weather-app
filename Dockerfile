FROM python:3.10
ADD weather_app.py .
CMD ["python", "./weather_app.py"]


RUN pip install requests


#new is my image name 