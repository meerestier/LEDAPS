FROM ubuntu:14.04

RUN apt-get update -y && \
	apt-get install -y \
	zlib1g zlib1g-dev libtiff5 libtiff5-dev \
	libgeotiff2 libgeotiff-dev libxml2 libxml2-dev \
	g++ gfortran bison byacc flex csh make \
	nano subversion git curl

ENV USERNAME=root
RUN mkdir /usr/local/hdf4
RUN chown $USERNAME /usr/local/hdf4

RUN cd /usr/local/hdf4 && curl http://www.hdfgroup.org/ftp/HDF/HDF_Current/src/hdf-4.2.11.tar.gz -O && tar -xzvf hdf-4.2.11.tar.gz
RUN cd /usr/local/hdf4/hdf-4.2.11 && ./configure && make check install && ldconfig

RUN mkdir /usr/local/hdf-eos
RUN chown $USERNAME /usr/local/hdf-eos
RUN cd /usr/local/hdf-eos && curl ftp://edhs1.gsfc.nasa.gov/edhs/hdfeos/latest_release/HDF-EOS2.19v1.00.tar.Z -O && tar -xzvf HDF-EOS2.19v1.00.tar.Z
RUN cd /usr/local/hdf-eos/hdfeos && ./configure -enable-install-include CC=/usr/local/hdf4/hdf-4.2.11/hdf4/bin/h4cc && make check install && ldconfig

ENV HDFEOS_GCTPINC="/usr/local/hdf-eos/hdfeos/hdfeos2/include"
ENV HDFEOS_GCTPLIB="/usr/local/hdf-eos/hdfeos/hdfeos2/lib"
ENV TIFFINC="/usr/include/x86_64-linux-gnu/"
ENV TIFFLIB="/usr/lib/x86_64-linux-gnu/"
ENV GEOTIFF_INC="/usr/include/geotiff/"
ENV GEOTIFF_LIB="/usr/lib/"
ENV HDFINC="/usr/local/hdf4/hdf-4.2.11/hdf4/include/"
ENV HDFLIB="/usr/local/hdf4/hdf-4.2.11/hdf4/lib/"
ENV HDFEOS_INC="/usr/local/hdf-eos/hdfeos/include/"
ENV HDFEOS_LIB="/usr/local/hdf-eos/hdfeos/hdfeos2/lib"
ENV JPEGINC="/usr/include/"
ENV JPEGLIB="/usr/lib/x86_64-linux-gnu/"
ENV XML2INC="/usr/include/libxml2/"
ENV XML2LIB="/usr/lib/x86_64-linux-gnu/"
ENV ZLIBINC="/usr/include/"
ENV ZLIBLIB="/usr/lib/x86_64-linux-gnu/"
ENV JBIGINC="/usr/include/"
ENV JBIGLIB="/usr/lib/x86_64-linux-gnu/"


RUN cd /usr/local/ && git clone https://github.com/USGS-EROS/espa-product-formatter.git espa-common
RUN mkdir -p /usr/local/espa-tools
ENV PREFIX="/usr/local/espa-tools/" #export PREFIX="path_to_directory_for_format_converter_build_data" probably "/usr/local/espa-common/src/raw_binary/format_conversion_libs"

RUN cd /usr/local/espa-tools && mkdir static_data && cd static_data && curl http://espa.cr.usgs.gov/downloads/auxiliaries/land_water_poly/land_no_buf.ply.gz -O && gunzip land_no_buf.ply.gz
ENV ESPA_LAND_MASS_POLYGON="$PREFIX/static_data/land_no_buf.ply"

RUN mkdir -p /usr/local/espa-tools/raw_binary
ENV ESPAINC="/usr/local/espa-tools/raw_binary/include"
ENV ESPALIB="/usr/local/espa-tools/raw_binary/lib"

RUN cd /usr/local/espa-common/src/raw_binary && make install && ldconfig


#Surface reflectances...

RUN cd /usr/local && mkdir espa-surface && git clone https://github.com/USGS-EROS/espa-surface-reflectance.git espa-surface/
ENV LEDAPS_AUX_DIR="/opt/ledaps"
ADD Makefile /usr/local/espa-surface/ledaps/ledapsSrc/src/lndsr/
RUN cd /usr/local/espa-surface/ledaps/ledapsSrc/src && make && make install

###
#ENV BIN="/usr/local/bin/ledapsSrc/bin"
#RUN svn checkout http://ledaps.googlecode.com/svn/releases/version_2.2.1/ /usr/local/bin
#RUN cd /usr/local/bin/ledapsSrc/src && make 
#RUN cd /usr/local/bin/ledapsSrc/src && make install && ldconfig
#RUN cd $BIN && chmod gou+x lndsrbm.ksh








