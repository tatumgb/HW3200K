import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/gbtatu7896/Python/Exercise07/Results"
fc = "roads.shp"
 
arcpy.AddField_management(fc, "FERRY", "TEXT","","", "")

delimfield2 = arcpy.AddFieldDelimiters(fc, "FEATURE")
cursor = arcpy.da.UpdateCursor(fc,["FERRY"], delimfield2 + " = 'Ferry Crossing'")

for row in cursor:
    row[0] = 'YES'
    cursor.updateRow(row)
del cursor

cursor = arcpy.da.UpdateCursor(fc,["FERRY"], delimfield2 + " <> 'Ferry Crossing'")

for row in cursor:
    row[0] = 'NO'
    cursor.updateRow(row)
    
    
del row
del cursor

del fc
