FROM python:3.11.0rc2-alpine3.16
WORKDIR /TDE3
COPY . .
RUN python test/docker_test/docker_test.py
EXPOSE 3000
CMD ["python", "src/main.py"]