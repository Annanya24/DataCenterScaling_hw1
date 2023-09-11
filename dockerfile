FROM python:3.8

WORKDIR /lab01

COPY pipeline.py pipeline_c.py
RUN pip install pandas
RUN pip install datetime
RUN pip install argparse

COPY pipeline.py pipeline_c.py

ENTRYPOINT [ "bash" ]