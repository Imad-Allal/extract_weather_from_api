FROM python:3.9
WORKDIR /app
COPY etl.py /app/etl.py
COPY extract.py /app/extract.py
COPY transform.py /app/transform.py
COPY display_map.py /app/display_map.py
COPY cities.json /app/cities.json
RUN pip cache purge
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update --fix-missing && apt-get install -y cron
COPY crontab /etc/cron.d/etl-cron
RUN chmod 0644 /etc/cron.d/etl-cron
RUN crontab /etc/cron.d/etl-cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

