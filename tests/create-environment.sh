#!/bin/bash
set -e
eval "$(conda shell.bash hook)"
conda deactivate
mamba env remove -n pynamical --yes
mamba clean --all --yes --quiet
mamba create -c conda-forge --strict-channel-priority -n pynamical --file "../docker/requirements.txt" --yes
eval "$(conda shell.bash hook)"
conda activate pynamical
pip uninstall pynamical --yes
pip install -e ../.
python -m ipykernel install --sys-prefix --name pynamical --display-name "Python (pynamical)"
mamba clean --all --yes --quiet
mamba env export -n pynamical > environment.yml
mamba list
jupyter kernelspec list
ipython -c "import pynamical; print('pynamical version', pynamical.__version__)"
