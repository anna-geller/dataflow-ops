FROM prefecthq/prefect:2-python3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
COPY setup.py .
COPY requirements.txt .
COPY dataflowops/ /opt/prefect/dataflowops/
COPY flows/ /opt/prefect/flows/
RUN pip install .
RUN prefect block register -m prefect_aws.ecs