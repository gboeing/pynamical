FROM jupyter/base-notebook
LABEL maintainer="Geoff Boeing <boeing@usc.edu>"
LABEL url="https://github.com/gboeing/pynamical"
LABEL description="Pynamical is a Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos."

COPY --chmod=0755 requirements.txt /tmp/

# install and configuration everything in one RUN to keep image tidy
RUN conda update --yes -c conda-forge --strict-channel-priority -n base conda mamba && \
    mamba install --update-all --force-reinstall --yes -c conda-forge --strict-channel-priority --file /tmp/requirements.txt && \
    python -m ipykernel install --sys-prefix --name pynamical --display-name "Python (pynamical)" && \
    rm -f -r -v /opt/conda/share/jupyter/kernels/python3 && \
    conda clean --all --yes --quiet && \
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
