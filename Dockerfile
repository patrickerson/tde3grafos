FROM python:3.11.0rc2-alpine3.16
WORKDIR /TDE3
COPY . .
RUN python test/docker_test.py
RUN python -m pip install -r requirements.txt
RUN python src/preprocessing.py
EXPOSE 3000
CMD ["python", "src/main.py"]