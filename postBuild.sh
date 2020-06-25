#!/bin/bash

jupyter labextension install --no-build @pyviz/jupyterlab_pyviz
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet
jupyter labextension install @jupyterlab/toc
# jupyter serverextension enable jupyterlab_sql --py --sys-prefix
jupyter lab build