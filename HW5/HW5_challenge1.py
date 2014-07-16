import arcpy

arcpy.env.workspace = "U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise06"

fclist = arcpy.ListFeatureClasses()


for each in fclist:
    details = arcpy.Describe("U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise06/" + each)
    name = details.name
    types = details.dataType
    print ("{} is a {} feature class".format(name, types))
    
