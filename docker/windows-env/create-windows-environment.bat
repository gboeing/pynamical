CALL conda deactivate
CALL conda clean --all --yes
CALL conda config --set show_channel_urls true
CALL conda config --set channel_priority strict
CALL conda config --prepend channels conda-forge
CALL conda update conda -n base --yes
CALL conda env remove -n pyn --yes
CALL conda create -n pyn --file "../requirements.txt" --yes
CALL conda activate pyn
CALL python -m ipykernel install --user --name pyn --display-name "Python (pyn)"
CALL conda clean --all --yes
CALL conda env export > environment-windows.yml
CALL conda list
CALL jupyter kernelspec list
CALL python -c "import pynamical; print(pynamical.__version__)"
