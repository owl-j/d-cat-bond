FROM continuumio/miniconda3

WORKDIR /cat-bond-server
COPY . .
RUN conda env create -f anaconda_env.yml

ENV PATH /opt/conda/envs/cat-bond-server/bin:$PATH
RUN /bin/bash -c "source activate cat-bond-server"

# This assumes this project is a web server
WORKDIR /cat-bond-server/src/server/svc/
CMD gunicorn -w 5 -b :7002 app:app
