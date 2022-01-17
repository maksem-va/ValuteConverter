FROM python:3.9
RUN pip install requests
ADD main.py   /
CMD [ "python3", "-u", "main.py" ]