FROM python:3.9-slim

WORKDIR /PAD_2025_1_2

COPY pruebadocker.py .

CMD [ "python","pruebadocker.py"]
