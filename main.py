from importlib import reload

FREECADPATH = 'C:/FreeCadBeta/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD


import Path
import Tests.PathTestUtils as PathTestUtils

from Path.Post.scripts import refactored_linuxcnc_post as postprocessor
from Path.Post.Processor import PostProcessor


from cnc_controller import cnc_controller
from linuxcnc_controller import linuxcnc_controller
from grbl_controller import grbl_controller
from masso_controller import masso_controller
from mach_controller import mach_controller

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


print("\n\n")

jobObjs=[]

# The attribute Fixtures is unique to Jobs
for obj in docObjs:
    if hasattr(obj, 'Fixtures'):
        if obj.TypeId == 'Path::FeaturePython':
#            if "Job" in obj.Label:
            jobObjs.append(obj)
    
print("jobObjs: ", jobObjs)

for aJob in jobObjs:
    print("aJob.Label: ", aJob.Label)
    print(type(aJob))
    print(dir(aJob))
    print("\n\n")
    print("--------------")
    print("\n\n")
    
    print("Attributes of a job:")
    
    print("Content: ", aJob.Content)
    print("CycleTime: ", aJob.CycleTime)
    print("Description: ", aJob.Description)
    print("Document: ", aJob.Document)
    print("ExpressionEngine: ", aJob.ExpressionEngine)
    print("Fixtures: ", aJob.Fixtures)
    print("FullName: ", aJob.FullName)
    print("GeometryTolerance: ", aJob.GeometryTolerance)
    print("Group: ", aJob.Group) 
    print("ID: ", aJob.ID)
    print("InList: ", aJob.InList)
    print("InListRecursive: ", aJob.InListRecursive)
    print("Label: ", aJob.Label)
    print("Label2: ", aJob.Label2)
    print("LastPostProcessDate: ", aJob.LastPostProcessDate)
    print("LastPostProcessOutput: ", aJob.LastPostProcessOutput)
    print("MemSize: ", aJob.MemSize)
    print("Model: ", aJob.Model)
    print("MustExecute: ", aJob.MustExecute)
    print("Name: ", aJob.Name)
    print("NoTouch: ", aJob.NoTouch)
    print("OldLabel: ", aJob.OldLabel)
    print("Operations: ", aJob.Operations)
    print(type(aJob.Operations))
    print("Operations as a class: ", aJob.Operations.__class__)
    print("Operations as a name: ", aJob.Operations.__class__.__name__)
    print("Operations as a bases: ", aJob.Operations.__class__.__bases__)
    print("Operations as a mro: ", aJob.Operations.__class__.__mro__)
    print("Operations as a dict ", aJob.Operations.__class__.__dict__)
    print("Operations as a module: ", aJob.Operations.__class__.__module__)

    
    # Assuming aJob.Operations is the object you're interested in
    methods = [method for method in dir(aJob.Operations) if callable(getattr(aJob.Operations, method)) and not method.startswith('__')]

    print("Available methods for aJob.Operations:")
    for method in methods:
        print("    ",method)

    # List attributes of aJob.Operations, excluding methods and magic methods
    attributes = [attr for attr in dir(aJob.Operations) if not callable(getattr(aJob.Operations, attr)) and not attr.startswith('__')]

    print("Available attributes for aJob.Operations:")
    for attr in attributes:
        print("    ", attr)


    lclList=aJob.Operations.OutList
    print("OutList: ", lclList)
    print("OutList size: ", lclList.__len__())

    if lclList.__len__() > 0:
        anOp=lclList[0];
        print("anOp: ", anOp)
        anOpattributes = [attr for attr in dir(aJob.Operations) if not callable(getattr(aJob.Operations, attr)) and not attr.startswith('__')]

        print("Available attributes for aJob.Operations:")
        for attr in anOpattributes:
            print("    ", attr)
        print("Name", anOp.Name)    



    parent=aJob.Operations.getParent()
    print("Parent: ", parent)

    print ("++++++++++++++++++++++++++++++++++++++++++")
    
    

    #try:
    #    iter(aJob.Operations)
    #    print("aJob.Operations is iterable.")
    #except TypeError:
    #    print("aJob.Operations is not iterable.")

    #lclOpList=aJob.Operations.
    #print("lclOpList: ", lclOpList)
    
    
    #cnt=0
    #for i in lclOpList:
    #    cnt+=1
    #    print("Operation[",cnt,"]=",i)
    
    
    
    print("OrderOutputBy: ", aJob.OrderOutputBy)
    print("OutList: ", aJob.OutList)
    print("OutListRecursive: ", aJob.OutListRecursive)
    print("Parents: ", aJob.Parents)
    print("Path: ", aJob.Path)
    print("Placement: ", aJob.Placement)
    print("PostProcessor: ", aJob.PostProcessor)
    print("PostProcessorArgs: ", aJob.PostProcessorArgs)
    print("PostProcessorOutputFile: ", aJob.PostProcessorOutputFile)
    print("PropertiesList: ", aJob.PropertiesList)
    print("Removing: ", aJob.Removing)
    print("SetupSheet: ", aJob.SetupSheet)
    print("SetupSheet: ", aJob.SetupSheet)
    print("SplitOutput: ", aJob.SplitOutput)
    print("State: ", aJob.State)
    print("Stock: ", aJob.Stock)
    print("Tools: ", aJob.Tools)
    print("Type: ", aJob.JobType)
    print("TypeId: ", aJob.TypeId)
    #print(": ", aJob.)

    print("\n\n")


    print("-----------------\n\n")




print("=========================================================================\n")
print("=========================================================================\n")


Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
Path.Log.trackModule(Path.Log.thisModule())



c = Path.Command("G0 X10 Y20 Z30")

print(c)


print("---------------Creating lcl_linux_post ----------------------------------")
lcl_linux_controller=linuxcnc_controller(PostProcessor)
lcl_linux_controller.print_values()
print("---------------Printing linuxcnc_post ----------------------------------")



print("\n\n\n")
print("---------------Creating lcl_grbl_post ----------------------------------")
lcl_grbl_controller=grbl_controller(PostProcessor)
lcl_grbl_controller.print_values()
print("---------------Printing lcl_grbl_post ----------------------------------")



print("\n\n\n")
print("---------------Creating lcl_masso_post ----------------------------------")
lcl_masso_controller=masso_controller(PostProcessor)
lcl_masso_controller.print_values()
print("---------------Printing lcl_masso_post ----------------------------------")



print("\n\n\n")
print("---------------Creating lcl_mach_post ----------------------------------")
lcl_mach_controller=mach_controller(PostProcessor)
lcl_mach_controller.print_values()
print("---------------Printing lcl_mach_post ----------------------------------")


print("=========================================================================\n")


CreateThisPost= 'grbl'
CreateThisPost= 'haas'
CreateThisPost= 'linuxcnc'
CreateThisPost= 'mach'
CreateThisPost= 'masso'

CreateThisPost=CreateThisPost.upper()

print("CreateThisPost: ", CreateThisPost)


if CreateThisPost == 'GRBL':
    lcl_post=grbl_controller(PostProcessor)
elif CreateThisPost == 'LINUXCNC':
    lcl_post=linuxcnc_controller(PostProcessor)
elif CreateThisPost == 'MACH':
    lcl_post=mach_controller(PostProcessor)
elif CreateThisPost == 'MASSO':
    lcl_post=masso_controller(PostProcessor)
else:
    print("Unknown Post Processor")
    exit()


            

