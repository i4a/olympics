FROM continuumio/miniconda

WORKDIR /app

# Disable Intel optimizations (takes a lot of extra space).
RUN conda install nomkl

# Install scientific dependencies.
RUN conda install scikit-learn
RUN conda install pandas
RUN conda install scipy

# Support for requirements.txt files.
COPY . /app
RUN pip install -r /app/requirements.txt


ONBUILD ADD . /app/
