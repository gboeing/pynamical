########################################################################
# Pynamical Dockerfile
# License: MIT, see full license in LICENSE.txt
# Web: https://github.com/gboeing/pynamical
#
# Build an image from the dockerfile:
# >>> docker build -t gboeing/pynamical .
#
# Push the built image to hub so others can pull/run it:
# >>> docker login
# >>> docker tag gboeing/pynamical gboeing/pynamical:v0.0.0
# >>> docker push -a gboeing/pynamical
#
# Run bash in this container and export final conda environment to a yml file:
# >>> docker run --rm -it -u 0 --name pynamical -v %cd%:/home/jovyan/work gboeing/pynamical /bin/bash
# >>> conda env export -n base > /home/jovyan/work/environment.yml
#
# Run jupyter lab in this container:
# >>> docker run --rm -it --name pynamical -p 8888:8888 -v %cd%:/home/jovyan/work gboeing/pynamical
# >>> docker run --rm -it --name pynamical -p 8888:8888 -v $PWD:/home/jovyan/work gboeing/pynamical
#
# Stop/delete all local docker containers/images:
# >>> docker stop $(docker ps -aq)
# >>> docker rm $(docker ps -aq)
# >>> docker rmi $(docker images -q)
########################################################################

FROM jupyter/base-notebook
LABEL maintainer="Geoff Boeing <boeing@usc.edu>"
LABEL url="https://github.com/gboeing/pynamical"
LABEL description="Pynamical is a Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos."

COPY requirements.txt /tmp/

# configure conda and install packages in one RUN to keep image tidy
RUN conda config --set show_channel_urls true && \
    conda config --set channel_priority strict && \
    conda config --prepend channels conda-forge && \
    conda update --yes -n base conda && \
    conda install --update-all --force-reinstall --yes --file /tmp/requirements.txt && \
    rm -f -r -v /opt/conda/share/jupyter/kernels/python3 && \
    python -m ipykernel install --sys-prefix --name pynamical --display-name "Python (pynamical)" && \
    conda clean --all --yes && \
    conda info --all && \
    conda list && \
    jupyter kernelspec list && \
    ipython -c "import pynamical; print('pynamical version', pynamical.__version__)"

# launch notebook in the local working directory that we mount
WORKDIR /home/jovyan/work

# set default command to launch when container is run
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# to test, import pynamical and print its version
RUN ipython -c "import pynamical; print(pynamical.__version__)"
