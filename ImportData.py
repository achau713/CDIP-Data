import netCDF4

stn = '100'
startdate = "04/01/2012" # MM/DD/YYYY
enddate = "04/30/2012"


# CDIP Archived Dataset URL
data_url = 'http://thredds.cdip.ucsd.edu/thredds/dodsC/cdip/archive/' + stn + 'p1/' + stn + 'p1_historic.nc'

test_archived_data = netCDF4.Dataset(data_url)

print(test_archived_data)

