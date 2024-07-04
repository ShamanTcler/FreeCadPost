from importlib import reload
from inspect import getmembers, isfunction

FREECADPATH = 'C:/FreeCadBeta/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD


import Path

print("\n\nAvailable functions in PAth")
print(getmembers(Path, isfunction))
txt=dir(Path)
print("txt:",txt)
print("Done ....Available functions in PAth")

print ("::::::::::::::::::::::::::::::::")

import PathScripts
#from PathScripts import PathUtils as pu
print("\n\nAvailable functions in PAthScrits")
print(getmembers(Path, isfunction))
txt1=dir(PathScripts)
print("txt:",txt1)
print("Done ....Available functions in PAthScrits")

print ("::::::::::::::::::::::::::::::::")

import JobUtils
print("\n\nAvailable functions in JobUtils")
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
print("Doc Label:",doc.Label)

print("These are global app settings:")
print("\t- Available lib paths for tools",JobUtils._get_available_tool_library_paths())


# HARD CODED FOR NOW
toolDirs=JobUtils._get_available_tool_library_paths()
print("\t- toolDirs[0][2]", toolDirs[0][2])
toolList=JobUtils._read_library(toolDirs[0][2])
print ("\t- toolList: ")
for aTool in toolList:
    print("\t\t:",aTool)


print("\n\n()()()()()())()()()()()()\n\n")

docObjs=doc.Objects
#print(type(docObjs))


opArray=[]
toolArray=[]
jobArray=[]

print("Parsing out CAM objects:")
for obj in docObjs:

    match obj.TypeId:

        case "App::FeaturePython":
            pass      

        case "App::DocumentObjectGroup":
            pass

        case "App::Line":
            pass

        case "App::Origin":
            pass

        case "App::Plane":
            pass

        case "Part::FeaturePython":
            pass

        case "PartDesign::Body":
            pass

        case "PartDesign::Pad":
            pass

        case "PartDesign::Pocket":
            pass

        case "Sketcher::SketchObject":            
            pass

        case "Path::FeaturePython":
            #print("Processing Path::FeaturePython")
            typeAsString=str(type(obj.Proxy))
            #print("typeAsString: ", typeAsString)

            if "Path.Main.Job" in typeAsString:
                jobArray.append(obj)    

            if "Path.Tool" in typeAsString:
                toolArray.append(obj)

            if "Path.Op" in typeAsString:
                opArray.append(obj)

        case _:
            print("Don't know this object type",obj.TypeId)

print("\tjobArray size: ",len(jobArray))
print("\ttoolArray size: ",len(toolArray))
print("\topArray size: ",len(opArray))


if len(jobArray) > 0:
    print("\n\nPrinting JobArray[0]:")
    #print(dir(jobArray[0]))
    print("\tLabel:",jobArray[0].Label)
    print("\tFixtures:",jobArray[0].Fixtures)
    print("\tPostProcessor:",jobArray[0].PostProcessor)
    print("\tPostProcessorArgs:",jobArray[0].PostProcessorArgs)
    print("\tPostProcessorOutputFile:",jobArray[0].PostProcessorOutputFile)
    print("\tSplitOutput:",jobArray[0].SplitOutput)

if len(toolArray) > 0:
    print("\n\nPrinting ToolArray[0]:")
    #print(dir(toolArray[0]))
    print("\tLabel:",toolArray[0].Label)
    print("\tToolNumber:",toolArray[0].ToolNumber)
    print("\tSpindleSpeed:",toolArray[0].SpindleSpeed)
    print("\t:SpindleDir",toolArray[0].SpindleDir)
    print("\tHorizFeed:",toolArray[0].HorizFeed)
    print("\tVertFeed:",toolArray[0].VertFeed)
    
        
if len(opArray) > 0:
    print("\n\nPrinting OpArray[0]:")
    print("\tLabel:",opArray[0].Label)
    print(dir(opArray[0]))
    print("\tActive:",opArray[0].Active)
    print("\tState:",opArray[0].State)
    print("\tClearanceHeight:",opArray[0].ClearanceHeight)
    print("\tCycleTime:",opArray[0].CycleTime)
    print("\tDirection:",opArray[0].Direction)
    print("\tFinalDepth:",opArray[0].FinalDepth)
    print("\tParents:",opArray[0].Parents)
    print("\tCoolantMode:",opArray[0].CoolantMode)

    #print(dir(opArray[0].Parents))
    #print("\t:",opArray[0].)
    #print("\t:",opArray[0].)


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


            

