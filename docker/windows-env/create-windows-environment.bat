CALL conda update --strict-channel-priority --yes -n base conda
CALL conda deactivate
CALL conda env remove -n pyn --yes
CALL conda create -n pyn -c conda-forge --strict-channel-priority --file "../../requirements.txt" --file "../../requirements-dev.txt" --file "../requirements-more.txt" --yes
CALL conda activate pyn
CALL python -m ipykernel install --user --name pyn --display-name "Python (pyn)"
CALL conda clean --all --yes
CALL conda env export > environment-windows.yml
CALL conda list
CALL jupyter kernelspec list
CALL python -c "import pynamical; print(pynamical.__version__)"
