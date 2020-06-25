# Python-Geo-Data-Science-Template
Template para proyectos de GeoDataScience con Python

## Crear un proyecto a partir del template

Para crear un repositorio a partir de este template sólo necesitas seguir [estas](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) instrucciones de GitHub.

## Organización del repositorio

La organización del proyecto es como sigue

1. Cada proyecto debe estar en su propio repositorio
2. Scripts externos o librerías compiladas van en la carpeta `bin/`
3. Guarda los datos en la carpeta `data/`
4. La documentación y otros archivos de texto en la carpeta `doc/`
5. Todos los archivos relacionados con Docker en la carpeta `docker`
6. Los notebooks van en la carpeta `notebooks/`.
7. Los resultados y archivos intermedios en la carpeta `outputs/`.
8. El código fuente, clases, funciones, et. guárdalos en la carpeta `src/`.

## Librerías incluidas

* [Rasterio](https://rasterio.readthedocs.io/en/latest/)
* [Rasterstats](https://pythonhosted.org/rasterstats/)
* [Geopandas](https://geopandas.org/)
* [PySal](https://pysal.org/)
* [scikit-learn](https://scikit-learn.org/stable/)
* [scikit-image](https://scikit-image.org/)
* [Folium](https://python-visualization.github.io/folium/)
* [Seaborn](https://seaborn.pydata.org/)
* [Bokeh](https://bokeh.org/)
* [Holoviews](http://holoviews.org/)
* [GeoViews](https://geoviews.org/)
* [GeoPy](https://geopy.readthedocs.io/en/stable/)

Además de las dependencias básicas como [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/) y [matplotlib](https://matplotlib.org/).
 
## Instalación usando conda

**Nota:** Estas son las instrucciones usando Linux aunque deberían funcionar igual para Mac. Para levantar todo en windows busca la dicumentación de conda para esa plataforma.

En el archivo `environment.yml` están las dependencias básicas de un proyecto general de GeoDataScience con Python, si necesitas agregar más, ese es el lugar indicado. Para crear el entorno en una carpeta adentro del repositorio:

````bash
$ ENV_PREFIX=$PWD/env
$ conda env create --prefix $ENV_PREFIX --file environment.yml --force
````

Y para activarlo:

````bash
$ conda activate $ENV_PREFIX
````
En este caso el environment se crea en la carpeta `env` en la raiz del repositorio (tienes que crearla) y por default no se sube al repositorio.

Si quieres instalar y habilitar algunas extensiones de JupyterLab útiles para varios proyectos, ejecuta el script postBuild:

````bash
$ .postBuild.sh
````
También puedes sólo ejecutar el script `create-conda-env.sh` que ejecuta todos los comandos necesarios. Desde la raiz del repositorio;

````bash
$ ./bin/create-conda-env.sh
````

## Instalación usando Docker

Otra forma de levantar el repositorio y las dependencias es usando [Docker](https://www.docker.com/). Docker es un sistema de contenedores de software que permite reproducir fácilmente entornos de forma independiente de la plataforma.

Primero hay que [instalar Docker](https://docs.docker.com/engine/install/ubuntu/) y [docker-compose](https://docs.docker.com/compose/install/) y seguir los [pasos de post-instalación](https://docs.docker.com/engine/install/linux-postinstall/).


Ya con todo instalado, desde la carpeta `Docker` de este repositorio, la primera vez que se ejecute:

````bash
$ docker-compose up --build
````

Las siguientes veces no es necesario el flag `--build`

````bash
$ docker-compose up 
````
`docker-compose` va a levantar un `jupyter-lab` dentro del container. Puedes acceder a él desde `localhost:8080` en un browser. Pide un token que pudes copiar/pegar desde la terminal. En ese lab están disponibles todas las librerías.

Igual que si instalaras via conda, si necesitas agregar más dependencias de Python, lo puedes hacer en `environment.yml`
