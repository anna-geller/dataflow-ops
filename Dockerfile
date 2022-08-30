FROM prefecthq/prefect:2.2-python3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
COPY setup.py .
COPY requirements.txt .
COPY dataflowops/ /opt/prefect/dataflowops/
RUN pip install .
