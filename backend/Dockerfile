FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /backend

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app.py /backend
COPY ./.coveragerc /backend
COPY ./src /backend/src/
COPY ./tests /backend/tests/

# Set env variable
ENV FLASK_APP app.py

EXPOSE 5000

## Program to start
#ENTRYPOINT [ "flask" ]
## Arguments
#CMD ["run", "--host", "0.0.0.0"]

ENTRYPOINT ["sh", "-c", "pytest -s -v --cov --color=yes && flask run --host=0.0.0.0"]
# To make app run even if tests are failed
#ENTRYPOINT ["sh", "-c", "pytest -v --cov || true && flask run --host=0.0.0.0"]