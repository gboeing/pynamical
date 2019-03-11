########################################################################
# Pynamical Dockerfile
# License: MIT, see full license in LICENSE.txt
# Web: https://github.com/gboeing/pynamical
#
# Build an image from the dockerfile:
# >>> docker build -t gboeing/pynamical .
#
# Push the built image to hub so others can pull/run it:
# >>> docker tag gboeing/pynamical gboeing/pynamical:v0.0.0
# >>> docker login
# >>> docker push gboeing/pynamical
#
# Run bash in this container and export final conda environment to a yml file:
# >>> docker run --rm -it -u 0 --name pynamical -v %cd%:/home/jovyan/work gboeing/pynamical /bin/bash
# >>> conda env export -n base > /home/jovyan/work/environment.yml
#
# Run jupyter lab in this container:
# >>> docker run --rm -it --name pynamical -p 8888:8888 -v %cd%:/home/jovyan/work gboeing/pynamical
#
# Stop/delete all local docker containers/images:
# >>> docker stop $(docker ps -aq)
# >>> docker rm $(docker ps -aq)
# >>> docker rmi $(docker images -q)
########################################################################

FROM jupyter/base-notebook
LABEL maintainer="Geoff Boeing <g.boeing@northeastern.edu>"

# symlink and permissions
USER root
RUN ln -s /opt/conda/bin/jupyter /usr/local/bin
USER $NB_UID

COPY "requirements-more.txt" /tmp/

# configure conda and install packages in one RUN to keep image tidy
RUN conda config --set show_channel_urls true && \
    conda config --prepend channels conda-forge && \
    conda update --strict-channel-priority --yes -n base conda && \
    conda install --strict-channel-priority --update-all --force-reinstall --yes --file /tmp/requirements-more.txt && \
    conda clean --all --yes && \
    conda info --all && \
    conda list

# launch notebook in the local working directory that we mount
WORKDIR /home/jovyan/work

# set default command to launch when container is run
CMD ["jupyter", "lab", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# to test, import pynamical and print its version
RUN python -c "import pynamical; print(pynamical.__version__)"
