import netCDF4

stn = '067'
yeardate = '2011'

# CDIP Archived Dataset URL
# santaMonica028 = 'http://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/' + stn + 'p1/' + stn + 'p1_historic.nc'

santaMonica028_archive = "https://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/028p1/028p1_historic.nc"
sanPedroSouth213_archive = "https://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/213p1/213p1_historic.nc"
longBeachChannel215_archive = "https://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/215p1/215p1_historic.nc"


santaMonica_archiveData = netCDF4.Dataset(santaMonica028_archive)
sanPedroSouth_archiveData = netCDF4.Dataset(sanPedroSouth213_archive)
longBeachChannel_archiveData = netCDF4.Dataset(longBeachChannel215_archive)


print("List of variables")
# print(nc.variables)


# print metadata -> test data access
print(santaMonica_archiveData.metadata_link)
print(sanPedroSouth_archiveData.metadata_link)
print(longBeachChannel_archiveData.metadata_link)





