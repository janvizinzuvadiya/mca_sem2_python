# to zip the content

from zipfile import *
f = ZipFile('abc.zip','w',ZIP_DEFLATED) # zip_deflated : compresses the content/file and zips in folder
f.write('source_image.png')
f.write('destination_image.png')
f.close()