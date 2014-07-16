import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise06/start.gdb"
arcpy.CreateFileGDB_management("U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise06", "analyze.gdb")
fclist = arcpy.ListFeatureClasses("", "polygon")
print fclist
for fc in fclist:
  fcdesc = arcpy.Describe(fc)
  arcpy.CopyFeatures_management(fc, "U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise06/analyze.gdb" + '/' + fcdesc.name)

