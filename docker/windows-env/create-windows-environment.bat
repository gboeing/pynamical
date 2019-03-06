CALL conda update conda -n base --yes
CALL conda deactivate
CALL conda env remove -n pyn --yes
CALL conda create -n pyn -c conda-forge --strict-channel-priority --file "../../requirements.txt" --file "../../requirements-dev.txt" --file "requirements-more.txt" --yes
CALL conda activate pyn
CALL python -m ipykernel install --user
CALL conda clean --all --yes
CALL conda env export > environment-windows.yml
