# Documentation for LEDAPS Processing for Surface Reflectance in a Docker Environment

1 Introduction 2

2 Materials and Methods 2

2.1 Preliminary Research 2

2.2 Infrastructure 3

2.3 Requirements 4

3 Guides 6

3.1 Installation 6

3.2 Processing Guide 6

Author: Lars Schulz
([*lars.schulz@systemic.de)*](mailto:lars.schulz@systemic.de))

Document history:

16-10-27: Version v0

Introduction
============

Surface reflectance satellite data is available for many different
environmental analysis applications. The relatively high radiometric and
temporal resolution of LANDSAT missions and the fact, that it covers a
timespan of 35 years while being freely available makes it very relevant
in this respect.

Processing time series data from Landsat Missions for surface
reflectance is a complicated matter. There are only few options and they
are mostly geared towards developers. So while some preprocessed scenes
are available, for many old mission scenes, there is no such service
available.

1.  Materials and Methods
=====================

Preliminary Research
--------------------

#### The situation

##### Aquisition of data

Landsat mission data is collected decentralized via a number of ground stations around the globe. Some of these no longer operate, therefore it is difficult to acquire their data. Depending on the study area of interest it is necessary to contact the stations operators and possibly acquire the data. The USGS Landsat website maintains a list of all legacy operators[^1], so this might be worthwhile to contact them, if
the main repositories do not have the data. For our purpose, a study area in Cyprus, USGS and the ESA combined had a quite comprehensive list of scenes available, so it was not necessary to tap into legacy stations. We used the metadata available from USGS to plot data availability in R[^2].

###### Process varies with data provider

The actual acquisition process varies greatly among data providers, but for USGS and ESA there is reasonably documented software and online services to self-serve.

###### USGS does not provide all legacy scenes for TM, Thematic Mapper, ETM+, Enhanced Thematic Mapper Plus missions

###### Surface reflectance products from USGS

USGS provides readily processed scenes for surface reflectance and other higher-level products. Naturally only for the scenes they have. There is an ongoing project called Landsat Collection
(http://landsat.usgs.gov/landsatcollections.php) that might change this. However during the time of writing, scenes for the study area where not yet available, but it might be reevaluate for other projects.

###### No surface reflectance calculated for the ESA scenes

ESA provides L1T scenes as is, without preprocessed surface reflectance. For our study area, most of the scenes from the 80s where only available from ESA, so it was necessary to process them ourselves.

#### Weighing of options

There are a number of algorithms available for processing surface reflectance. Which one is necessary depends on the study question. There is a paper that compares the most common methods and helped greatly to clarify (<span style="font-variant:small-caps;">Schultz et al.</span> 2015).

##### DOS1: Dark Object Subtraction 1)(<span style="font-variant:small-caps;">Chavez</span> 1996)

DOS1 is the simplest of algorithms, that is pure image processing, without auxiliary data to complement.

##### ATCOR (<span style="font-variant:small-caps;">Richter</span> 2011)

ATCOR is a commercial product which utilizes auxiliary data to improve processing results. We evaluated it, and some papers suggest, that its results compare to LEDAPS. It also has a plugin for ERDAS Imagine (2015 and later), so it might be worth considering, if the software is available.

##### LEDAPS (<span style="font-variant:small-caps;">Schmidt et al.</span> 2013)

LEDAPS is the processing algorithm developed and used by USGS/ESPA. It employs auxiliary data and is used for the preprocessed scenes available from them.

#### The solution

We decided to go with the LEDAPS route. It was a good fit for our study area, because we could combine scenes from different providers into one time series. Otherwise there is a chance of more processing discrepancies stemming from the varying algorithms used. This could affect the time series analysis of pixels across algorithms.

Conceptional, we tried to transform the scenes into the USGS format andprocess with the tools they provide publicly. To make this process reusable, we settled on a virtualization environment that handles all dependencies and libraries, of which there are a lot. A detailed guide on this process is elaborated in chapter 3.

Infrastructure
--------------

#### Docker container with all required tools

We build on a Docker Image for geospatial analysis provided by the University of South Hampton (GEODATA)[^3] extended by the Comisión Nacional para el Conocimiento y Uso de la Biodiversidad (CONABIO)[^4] of Mexico. CONABIO had prepared a docker image, that we customized to our needs. To complement, we included the latest tools from USGS EROS[^5] github repository for formatting the data and the actual processing with the LEDAPS algorithm. Figure 1 provides an overview of the technological
stack used.

##### ![](media/image1.emf){width="6.263888888888889in" height="2.9305555555555554in"}Figure 1: Technological stack for processing

Requirements
------------

The actual processing takes place in a controlled environment, a
virtualized machine running linux. The only requirement for the host system is the docker framework that manages this environment[^6].

#### Requirements for host machine

##### Windows

Docker for Windows requires 64bit Windows 10 Pro, Enterprise and
Education (1511 November update, Build 10586 or later) and Microsoft Hyper-V. Please see What to know before you install for a full list of prerequisites

##### Mac

Docker for Mac requires macOS 10.10.3 Yosemite or newer running on a 2010 or newer Mac, with Intel’s hardware support for MMU virtualization. Please see What to know before you install for a full list of prerequisites.

##### Linux

Docker is supported on these Ubuntu operating systems:\
• Ubuntu Xenial 16.04 (LTS)\
• Ubuntu Trusty 14.04 (LTS)\
• Ubuntu Precise 12.04 (LTS)\
\
And many other Linux operating systems.[^7]

#### Data input requirements

##### Meta data

Before actual acquisition, we evaluated the metadata for the Landsat missions available from USGS.

##### Landsat Scenes

There are a number of options to acquire data from both USGS and ESA. For large number of scenes, it worked best to download from ESA via Online Dissemination service, since we only needed one row/path. We used a Plugin for Firefox[^8] to download all scenes from the ESA website.

###### ESA

ESA is offering:

Pre-defined cloud-free European Coverages of TM and ETM+ data acquired between 1990 and 1995 (TM) and between 1999 and 2003 (ETM+). Available after (Fast registration and direct download for LANDSAT.TM.SCPSCC). Newly processed orthocorrected Landsat 5 TM data from 1984 to 2011 and Landsat 7 ETM from 1999 to 2003. Products unique to ESA, not in USGS archives. Available over Europe (incl. Greenland) and West Africa (Fast registration and direct download for LANDSAT.TM.GTC and LANDSAT.ETM.GTC).

####### Online Dissemination

[*https://landsat-ds.eo.esa.int/app/protected/collections\_WRS.php*](https://landsat-ds.eo.esa.int/app/protected/collections_WRS.php)

###### USGS

####### EarthExplorer

[*http://earthexplorer.usgs.gov/*](http://earthexplorer.usgs.gov/)

####### File list ordering

[*http://earthexplorer.usgs.gov/filelist*](http://earthexplorer.usgs.gov/filelist)

####### ESPA - New Bulk Order

[*http://espa.cr.usgs.gov/ordering/new/*](http://espa.cr.usgs.gov/ordering/new/)

##### Auxiliary data

Auxiliary data is available from the USGS website at
```
http://edclpdsftp.cr.usgs.gov/downloads/auxiliaries/ledaps\_auxiliary/ledaps\_aux.1978-2014.tar.gz
```
The espa-surface-reflectance tool documentation provides instructions on how to update these, but for our purpose, this was not necessary.

###### http://edclpdsftp.cr.usgs.gov/downloads/auxiliaries/ledaps\_auxiliary/ledaps\_aux.1978-2014.tar.gz

###### https://github.com/USGS-EROS/espa-surface-reflectance/tree/master/ledaps

<span id="_Toc465327255" class="anchor"></span>

1.  Guides
======

Installation
------------

#### Docker App

##### Download from docker.com

```
*https://www.docker.com/products/overview*
```

#### Windows

##### Enable Hyper-V

Hyper-V is the vitualisation environment for Windows 10. There is good
documentation on the Internet on how to enable this on your machine.

##### Install Docker for Windows

[*https://www.docker.com/products/overview*](https://www.docker.com/products/overview)

Processing Guide
----------------

#### Running in a shell

All host systems have shell environments, that can be used to navigate
and execute commands and scripts. In Windows, this is the Powershell, on
a Mac or Linux machine it is often called terminal. Use these to run the
commands highlighted in this guide.

#### Download from Github

1.  Go to desired directory
```
cd \[PATH TO DIRECTORY\]
```
1.  Get repository
```
git clone https://github.com/meerestier/LEDAPS.git ledaps_process --config core.autocrlf=input
```
**Important:** The Readme.md file contains up-to-date details on how to
use the container and gives examples on how to construct the commands.

The script might be updated, so it is possible to pull the latest version from github. Make sure you are in the target directory and execute.
```
git pull
```
The script contains a readme file, that guides through the process.
Please always use the latest version of the script. Explaining the version control workflow is beyond the scope of this guide, but there are resources available online[^9].

#### Build Docker Container

The Dockerfile included in the downloaded directory contains all
directives to set up the virtual environment for processing.

The actual Docker Image needs to be downloaded from hub.docker.com. On initial execution, this will fetch all data online, so this may take a while.

Command:
```
docker build -t natriskchange/ledaps .
```
#### Run Docker Container

Building a Docker Image makes it available, but we need to run it (comparable to booting a machine).

Command on Linux Mac:
```
docker run -ti --rm \
-v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps\_aux.1978-2014:/opt/ledaps \
-v /Volumes/DATA_DRIVE/NatRiskChange/Data:/data \
-v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
natriskchange/ledaps /data /opt/ledaps
```

Command on Windows:
```
docker run -ti --rm -v F:/NatRiskChange/Auxiliary/ledaps\_aux.1978-2014:/opt/ledaps -v F:/NatRiskChange/Data:/data -v F:/NatRiskChange/Results:/results natriskchange/ledaps /data /opt/ledaps
```

**Explanation**: This command will run the container natriskchange/ledaps and link volumes with scenes (/data), auxiliary files (/ledaps_aux.1978-2014) and a volume for the results (/results) When the container runs, it prompts for the scene names that need to be in the data directory. So this should have the form LT41760361990224XXX03, the standard naming convention for landsat source data (more info: [http://landsat.usgs.gov/naming_conventions_scene_identifiers.php](http://landsat.usgs.gov/naming_conventions_scene_identifiers.php))

You can enter multiple names, separated by a space (see the scenelist.txt for an example) or just one scene to process. At the moment processing no more than 5 scenes at once is recommended until the script is further optimized.

Sources
=======

<span style="font-variant:small-caps;">Chavez, P.S.</span>, 1996: Image-based atmospheric corrections-revisited and improved. Photogrammetric engineering and remote sensing 62: 1025–1035.

<span style="font-variant:small-caps;">Richter, R.</span>, 2011: Atmospheric/Topographic from Satellite Imagery (ATCOR 2/3 User Guide, Version 8). DLR-German Aerospace Center, Wessling, Germany.

<span style="font-variant:small-caps;">Schmidt, G., Jenkerson, C., Masek, J., Vermote, E. & Gao, F.</span>, 2013: Landsat ecosystem disturbance adaptive processing system (LEDAPS) algorithm description, http://pubs.er.usgs.gov/publication/ofr20131057.

<span style="font-variant:small-caps;">Schultz, M., Verbesselt, J., Avitabile, V., Souza, C. & Herold, M.</span>, 2015: Error Sources in Deforestation Detection Using BFAST Monitor on Landsat Time Series Across Three Tropical Sites. .

####

[^1]: [*http://landsat.usgs.gov/Historical\_IGS.php*](http://landsat.usgs.gov/Historical_IGS.php)

[^2]: Script available at
    [*https://github.com/meerestier/Landsat-Metadaten-in-R*](https://github.com/meerestier/Landsat-Metadaten-in-R)

[^3]: [*http://www.geodata.soton.ac.uk/geodata*](http://www.geodata.soton.ac.uk/geodata)

[^4]: [*http://www.conabio.gob.mx*](http://www.conabio.gob.mx)

[^5]: [*http://eros.usgs.gov*](http://eros.usgs.gov)

[^6]: [*https://docs.docker.com/ucp/installation/system-requirements/*](https://docs.docker.com/ucp/installation/system-requirements/)

[^7]: Docker has a detailed guide at:
    [*https://docs.docker.com/engine/installation/*](https://docs.docker.com/engine/installation/)

[^8]: [*https://addons.mozilla.org/de/firefox/addon/downthemall*](https://addons.mozilla.org/de/firefox/addon/downthemall)

[^9]: [*https://help.github.com/articles/fetching-a-remote/*](https://help.github.com/articles/fetching-a-remote/)
