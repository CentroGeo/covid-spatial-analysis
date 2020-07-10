# Análisis Espacial de la pandemia de COVID-19 en México

Este repositorio contiene el código para realizar algunos análisis espaciales exploratorios para entender la evolución espacio-temporal de la pandemia COVID-19 en México. La idea es utilizar algunas herramientas sencillas de visualización y análisis de datos geográficos para explorar los [datos abiertos](https://www.gob.mx/salud/documentos/datos-abiertos-152127) que publica la Dirección General de Epidemiología.


## Organización del repositorio

La organización del proyecto es como sigue

1. La carpeta `notebooks/` contiene los notebooks de Python con los análisis y sus explicaciones
2. En la carpeta `src/` está el código de las funciones auxiliares
3. La carpeta `data/` contiene los datos necesarios


El repositorio está creado a partir del siguiente template [Python-Geo-Data-Science-Template](https://github.com/CentroGeo/Python-Geo-Data-Science-Template). A continuación están las instrucciones para echar a andar el código

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

