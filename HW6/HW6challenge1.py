import arcpy

arcpy.env.workspace = "u:/Shared/GIS/StuData/jpdees0754/Python/Data/Exercise06"

fclist = arcpy.ListFeatureClasses()


for each in fclist:
    details = arcpy.Describe("u:/Shared/GIS/StuData/jpdees0754/Python/Data/Exercise06/" + each)
    name = details.name
    types = details.dataType
    print ("{} is a {} feature class".format(name, types))
    


