# Use the Python3.7.3 image
FROM python:3.7.3-stretch

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
#RUN apk --no-cache add postgresql-client

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt



# For Flask
EXPOSE 5000
CMD ["python", "run.py"] 

# For some other command
# CMD ["python", "app.py"]
