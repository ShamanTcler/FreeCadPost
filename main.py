from importlib import reload
from inspect import getmembers, isfunction

FREECADPATH = 'C:/FreeCadBeta/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD


import Path

print("Available functions in PAth")
print(getmembers(Path, isfunction))
txt=dir(Path)
print("txt:",txt)
print("Done ....Available functions in PAth")

print ("::::::::::::::::::::::::::::::::")

import PathScripts
#from PathScripts import PathUtils as pu
print("Available functions in PAthScrits")
print(getmembers(Path, isfunction))
txt1=dir(PathScripts)
print("txt:",txt1)
print("Done ....Available functions in PAthScrits")

print ("::::::::::::::::::::::::::::::::")

import JobUtils
print("Available functions in JobUtils")
print(getmembers(JobUtils, isfunction))
txt2=dir(JobUtils)
print("txt:",txt2)
print("Done ....Available functions in JobUtils")

print ("::::::::::::::::::::::::::::::::")

import Tests.PathTestUtils as PathTestUtils


#from PathScripts import PathPost


from Path.Post.scripts import refactored_linuxcnc_post as postprocessor
from Path.Post.Processor import PostProcessor


from cnc_controller import cnc_controller
from linuxcnc_controller import linuxcnc_controller
from grbl_controller import grbl_controller
from masso_controller import masso_controller
from mach_controller import mach_controller

class post_it(PostProcessor):
    pass


print("======================Starting Code ===================================================\n")
#doc = FreeCAD.newDocument()

filepath = "test1.FCStd"
doc=FreeCAD.open(filepath)

print(type(doc))
print(doc.Label)


print("Available lib paths for tools")
toolDirs=JobUtils._get_available_tool_library_paths()
print(toolDirs)

# HARD CODED FOR NOW
print("toolDirs[0][2]", toolDirs[0][2])
toolList=JobUtils._read_library(toolDirs[0][2])
print(toolList)

print("Available FreeCAD.ActiveDocument")
print(dir(FreeCAD.ActiveDocument))


print("Jobs")
newJob = FreeCAD.ActiveDocument.getObject("Job")
print(type(newJob))
print(newJob.Label)


print("Operations")
p = FreeCAD.ActiveDocument.getObject("Operations")
print(type(p))

print("dressups")
p = FreeCAD.ActiveDocument.getObject("DressupTag")
print(type(p))



# poster=Path.Post.CommandPathPost()

print("()()()()()())()()()()()()")

docObjs=doc.Objects
print(type(docObjs))

for obj in docObjs:
    print("Object Name: ", obj.Name, "  | Object Label: ", obj.Label," | Object Type: ", obj.TypeId )
# print("Object Name: ", obj.Name , "Object Label: ", obj.Label, "Object Type: ", obj.TypeId, "Object SubType: ", obj.SubTypeId)

print("()-()-()-()-()-()-()-()-()-()-()-()")

for obj in docObjs:
    if obj.TypeId == 'Path::FeaturePython':
        print("Object Name: ", obj.Name, "  | Object Label: ", obj.Label," | Object Type: ", obj.TypeId )


opArray=[]
toolArray=[]
jobArray=[]

for obj in docObjs:
    if obj.TypeId == 'Path::FeaturePython':
        if "PROFILE" in obj.Name.upper() or "POCKET" in obj.Name.upper() or \
            "DRILL" in obj.Name.upper() or "FACE" in obj.Name.upper() or \
            "CONTOUR" in obj.Name.upper() or "THREAD" in obj.Name.upper() or \
            "ENGRAVE" in obj.Name.upper() or "DEBURR" in obj.Name.upper():
            opArray.append(obj)

        if "TC__" in obj.Name.upper():
            toolArray.append(obj)
        
        if "JOB" in obj.Name.upper():
            jobArray.append(obj)
            
print("\n\n")
print("opArray size: ", len(opArray))
for op in opArray:
    print("op.Name: ", op.Name, " | op.Label: ", op.Label, " | op.TypeId: ", op.TypeId)
    print(dir(op))
    if hasattr(op, 'Label'):
        print("\tLabel: ", op.Label)
    if hasattr(op, 'FullName'):
        print("\tFullName: ", op.FullName)
    if hasattr(op, 'Active'):
        print("\tActive: ", op.Active)
    if hasattr(op, 'Direction'):
        print("\tDirection: ", op.Direction)
    else:
        print("\tDirection: None")
    if hasattr(op, 'CoolantMode'):
        print("\tCoolantMode: ", op.CoolantMode) 
    if hasattr(op, 'CycleTime'):
        print("\tCycleTime: ", op.CycleTime)
    if hasattr(op, 'Description'):  
        print("\tDescription: ", op.Description)
    if hasattr(op, 'Document'):
        print("\tDocument: ", op.Document)
    #if hasattr(op, 'ExpressionEngine'):
    #    print("\tExpressionEngine: ", op.ExpressionEngine)  
    if hasattr(op, 'GeometryTolerance'):
        print("\tGeometryTolerance: ", op.GeometryTolerance)
    if hasattr(op, 'Group'):
        print("\tGroup: ", op.Group)
    if hasattr(op, 'ToolController') :
        print("\tToolController: ", op.ToolController)
        print("\tdir ToolController: ", dir(op.ToolController))
        print("\tToolController.ToolNumber: ", op.ToolController.ToolNumber)
        print("\tToolController.Tool: ", op.ToolController.Tool)

    if hasattr(op, 'Path'):
        print("\tPath: ", op.Path)
        #print("dir:", dir(op.Path))
        for cmd in op.Path.Commands:
            print("\t\tCommands:", cmd)

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
                  #print("\tPath cnt: ", op.Path.count)
        #for aMove in op.Path:
        #    print("\t\tPseudo Gcode: ", aMove)  

    if hasattr(op, 'Content'):
        print("\tContent: ", op.Content)


print("\n\n")
print("toolArray size: ",len(toolArray)) 
for tool in toolArray:
    print("tool.Name: ", tool.Name, " | tool.Label: ", tool.Label, " | tool.TypeId: ", tool.TypeId)
    #print(dir(tool))
    print("tool:",tool.ToolNumber)
    #  " | ", tool.Name, " | ", tool.Label, " | ", tool.TypeId))

print("\n\n")
print("jobArray size: ",len(jobArray))  
for job in jobArray:
    print("job.Name: ", job.Name, " | job.Label: ", job.Label, " | job.TypeId: ", job.TypeId)



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
    

    # print("Content: ", aJob.Content) gives a list of printable objects

    print("Attributes of a job:")
    print("   Label: ", aJob.Label)
    print("   Description: ", aJob.Description)
    print("   Document: ", aJob.Document)
    print("   Output filename:",aJob.PostProcessorOutputFile)
    print("   State: ", aJob.State)

    print("   PostProcessor: ", aJob.PostProcessor)
    print("   PostProcessor Args: ", aJob.PostProcessorArgs)

    print("   CycleTime: ", aJob.CycleTime)
    print("   Fixtures: ", aJob.Fixtures)
    #print("   Job Type: ", aJob.)
    print("\n")

    print("   SetUp Sheet:")
    #print("       : ", aJob.SetupSheet.)
    print("       FullName: ", aJob.SetupSheet.FullName)
    print("       ClearanceHeightExpression: ", aJob.SetupSheet.ClearanceHeightExpression)
    print("       ClearanceHeightOffset: ", aJob.SetupSheet.ClearanceHeightOffset)
    # printing contents lets you know what is in the entire list
    #print("       Content: ", aJob.SetupSheet.Content)
    print("       CoolantMode: ", aJob.SetupSheet.CoolantMode)
    print("       CoolantModes: ", aJob.SetupSheet.CoolantModes)
    print("       ExpressionEngine: ", aJob.SetupSheet.ExpressionEngine)
    #print("       Document: ", aJob.SetupSheet.Document)
    print("       FinalDepthExpression: ", aJob.SetupSheet.FinalDepthExpression)    
    print("\n")


    print("    Tools used:")
    for tc in aJob.Tools.Group:
        print("       tc: ", tc.ToolNumber, " name: ", tc.FullName)

    print("\n")



    print("   Operations:")
    
    print("       InList: ")
    #print("           Content: ", aJob.Operations.InList.Content)
    #print("           Content: ", aJob.Operations.InList.Group)
          
    #lclList=aJob.Operations.InList
    
    
    print("          List size: ", aJob.Operations.InList.__len__())
    for opListItem in aJob.Operations.InList:
        print("           opListItem: ", opListItem.Name, " | ", opListItem.Label, " | ", opListItem.TypeId,  " | ", opListItem.FullName)
        print(dir(opListItem))
        print(dir(opListItem.Operations))
        print("name:", opListItem.Operations.Name)

    print("\n")     

    print("       OutList: ")
    print("          List size: ", aJob.Operations.OutList.__len__())
    for opListItem in aJob.Operations.OutList:
        print("           opListItem: ", opListItem.Name, " | ", opListItem.Label, " | ", opListItem.TypeId,  " | ", opListItem.FullName)


    print("-----------------")

    #exit()

    type(aJob.Content)
    print("Content: ", aJob.Content)

    print("============================")

    print("CycleTime: ", aJob.CycleTime)
    print("Description: ", aJob.Description)
    print("Document: ", aJob.Document)
    print("ExpressionEngine: ", aJob.ExpressionEngine)

    
    print("FullName: ", aJob.FullName)
    print("GeometryTolerance: ", aJob.GeometryTolerance)
    print("Group: ", aJob.Group) 
    print("ID: ", aJob.ID)
    print("InList: ", aJob.InList)
    print("InListRecursive: ", aJob.InListRecursive)
    
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


    print("dir operation:",dir(aJob.Operations))
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
    print("aJob.OperationsOutList: ", lclList)
    print("aJob.OperationsOutList size: ", lclList.__len__())

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

    print ("++++++++++++++++++++++++++++++++++++++++++====================")
    #print("aJob.Operations.Content:", aJob.Operations.Content)
    print("aJob.Operations.inlist:", aJob.Operations.InList)
    print ("|||||||||||||||||||||||||")
    print("aJob.Operations.outlist:", aJob.Operations.OutList)
    print ("++++++++++++++++++++++++++++++++++++++++++====================")
    #try:
    #    iter(aJob.Operations)
    #    print("aJob.Operations is iterable.")
    #except TypeError:
    #    print("aJob.Operations is not iterable.")

   
    
    
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

    SetupSheetDir=dir(aJob.SetupSheet)
    print("SetupSheetDir: ", SetupSheetDir)

    #ret=aJob.SetupSheet.name
    #type(ret)
    #print("    output path", ret)
    
    print("SetupSheet: ", aJob.SetupSheet)
    print("SplitOutput: ", aJob.SplitOutput)
    print("State: ", aJob.State)
    print("Stock: ", aJob.Stock)
    print("Tools: ", aJob.Tools)
    print("Type: ", aJob.JobType)
    print("TypeId: ", aJob.TypeId)
    #print(": ", aJob.)

    print("\n\n")


    print()

    print("-----------------\n\n")




print("=========================================================================\n")
print("=========================================================================\n")



#exit()

print("============================Starting PATH stuff =============================================\n")

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


            

