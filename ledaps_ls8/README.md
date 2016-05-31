# LEDAPS
docker commands to preprocess landsat 8 oli-tirs data and obtain surface reflectances

We need to download the auxiliary files described in: https://github.com/USGS-EROS/espa-surface-reflectance/tree/master/not-validated-prototype-l8_sr

Auxiliary files: http://espa.cr.usgs.gov/downloads/auxiliaries/l8sr_auxiliary/l8sr_auxiliary.tar.gz

We also have to download 4 files CMG and CMA MODIS products for both terra and aqua from the servers:

	* ladssci.nascom.nasa.gov
	* ladsweb.nascom.nasa.gov

you will need a user and password for the first one.

After building the image with the Dockerfile of this repo:


```
$docker build -t ledaps/ledaps_ls8:v1 .

```

you can combine the 4 files in a *hdf_fused* file. For example, if you have in the path "/auxiliary_files" the auxiliary files then, after creating the /LADS/2015 directory:

```
$docker run --rm -v /auxiliary_files:/opt/ledaps ledaps/ledaps_ls8:v1 combine_l8_aux_data \
--terra_cmg=MOD09CMG.A2015015.006.2015295113251.hdf --terra_cma=MOD09CMA.A2015015.006.2015295113500.hdf \
--aqua_cmg=MYD09CMG.A2015015.006.2015295105858.hdf --aqua_cma=MYD09CMA.A2015015.006.2015295105858.hdf \
--output_dir=/opt/ledaps/LADS/2015/
```

And for obtaining the surface reflectances you can use the following command:

```
$docker run --rm -v /auxiliary_files:/opt/ledaps -v /data_landsat:/data $(pwd):/results \
ledaps/ledaps_ls8:v1 /results/shell_script /data/LC80210482015015LGN00
```

where we have assumed that /data_landsat have the downloaded oli-tirs data of landsat 8 and in the working directory we want the results and have the shell_script

