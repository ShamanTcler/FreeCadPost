from importlib import reload

FREECADPATH = 'C:/FreeCadBeta/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD


import Path
import Tests.PathTestUtils as PathTestUtils

from Path.Post.scripts import refactored_linuxcnc_post as postprocessor
from Path.Post.Processor import PostProcessor


from base_class_post import base_post
from linuxcnc_class_post import linuxcnc_post
from grbl_class_post import grbl_post
from masso_class_post import masso_post
from mach_class_post import mach_post

class post_it(PostProcessor):
    pass


#doc = FreeCAD.newDocument()

filepath = "test1.FCStd"
doc=FreeCAD.open(filepath)

print(type(doc))
print(doc.Label)

docObjs=doc.Objects
print(type(docObjs))

for obj in docObjs:
    print("Object Name: ", obj.Name, "  | Object Label: ", obj.Label," | Object Type: ", obj.TypeId )
# print("Object Name: ", obj.Name , "Object Label: ", obj.Label, "Object Type: ", obj.TypeId, "Object SubType: ", obj.SubTypeId)

for obj in docObjs:
    if obj.TypeId == 'Path::Feature':
        print("Object Name: ", obj.Name, "  | Object Label: ", obj.Label," | Object Type: ", obj.TypeId )
        print("Object Name: ", obj.Name , "Object Label: ", obj.Label, "Object Type: ", obj.TypeId, "Object SubType: ", obj.SubTypeId)

jobObjs=[]
for obj in docObjs:
    if hasattr(obj, 'TypeId'):
        if obj.TypeId == 'Path::FeaturePython':
            jobObjs.append(obj)
    
print("jobObjs: ", jobObjs)

for aJob in jobObjs:
    print("aJob.Label: ", aJob.Label)


exit()

Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
Path.Log.trackModule(Path.Log.thisModule())



c = Path.Command("G0 X10 Y20 Z30")

print(c)


print("---------------Creating lcl_linux_post ----------------------------------")
lcl_linux_post=linuxcnc_post(PostProcessor)
print("---------------Printing linuxcnc_post ----------------------------------")
print(lcl_linux_post)
print(lcl_linux_post.Values)

print("\n\n\n")
print("---------------Creating lcl_grbl_post ----------------------------------")
lcl_grbl_post=grbl_post(PostProcessor)
print("---------------Printing lcl_grbl_post ----------------------------------")
print(lcl_grbl_post)
print(lcl_grbl_post.Values)

print("\n\n\n")
print("---------------Creating lcl_masso_post ----------------------------------")
lcl_masso_post=masso_post(PostProcessor)
print("---------------Printing lcl_masso_post ----------------------------------")
print(lcl_masso_post)
print(lcl_masso_post.Values)


print("\n\n\n")
print("---------------Creating lcl_mach_post ----------------------------------")
lcl_mach_post=mach_post(PostProcessor)
print("---------------Printing lcl_mach_post ----------------------------------")
print(lcl_mach_post)
print(lcl_mach_post.Values)

print("=========================================================================\n")


CreateThisPost= 'grbl'
CreateThisPost= 'haas'
CreateThisPost= 'linuxcnc'
CreateThisPost= 'mach'
CreateThisPost= 'masso'

CreateThisPost=CreateThisPost.upper()

print("CreateThisPost: ", CreateThisPost)


if CreateThisPost == 'GRBL':
    lcl_post=grbl_post(PostProcessor)
elif CreateThisPost == 'HAAS':
    lcl_post=haas_post(PostProcessor)
elif CreateThisPost == 'LINUXCNC':
    lcl_post=linuxcnc_post(PostProcessor)
elif CreateThisPost == 'MACH':
    lcl_post=mach_post(PostProcessor)
elif CreateThisPost == 'MASSO':
    lcl_post=masso_post(PostProcessor)
else:
    print("Unknown Post Processor")
    exit()


            

