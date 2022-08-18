FROM prefecthq/prefect:2.1-python3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
COPY requirements.txt .
COPY setup.py .
RUN pip install .
