FROM prefecthq/prefect:2.0b8-python3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
COPY prefect_dataops/ /opt/prefect/prefect_dataops/
COPY requirements.txt .
COPY setup.py .
RUN pip install .
