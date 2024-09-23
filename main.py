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

print("\n\n\nThese are global app settings:")
print("\t- Available lib paths for tools",JobUtils._get_available_tool_library_paths())


# HARD CODED FOR NOW
toolDirs=JobUtils._get_available_tool_library_paths()
print("\t- toolDirs[0][2]", toolDirs[0][2])
toolList=JobUtils._read_library(toolDirs[0][2])

print("\n")
print ("\t- toolList: ")
for aTool in toolList:
    print("\t\t:",aTool)


print("Done with tools\n\n\n\n")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Walking the CAM details\n")

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
    lclCnt=0
    

    while lclCnt < len(jobArray):
        
        
        print("\n\nPrinting JobArray[",lclCnt,"]:")
        print(dir(jobArray[lclCnt]))
        # Content has ALL the data
        # print("\tContent:",jobArray[lclCnt].Content)
        print("\tLabel:",jobArray[lclCnt].Label)
        print("\tFixtures:",jobArray[lclCnt].Fixtures)
        print("\tPostProcessor:",jobArray[lclCnt].PostProcessor)
        print("\tPostProcessorArgs:",jobArray[lclCnt].PostProcessorArgs)
        print("\tPostProcessorOutputFile:",jobArray[lclCnt].PostProcessorOutputFile)
        print("\tSplitOutput:",jobArray[lclCnt].SplitOutput)
        print("\tStock:",jobArray[lclCnt].Stock)

        print("\tCycleTime:",jobArray[lclCnt].CycleTime)
        print("\tDescription:",jobArray[lclCnt].Description)

        #print("\tGroup:",jobArray[lclCnt].Group)
        print("\n")
        for elem in jobArray[lclCnt].Group:
            print("\t\tGroup:",elem)

        print("\tOperations:",jobArray[lclCnt].Operations)
 
        jobArray[lclCnt].dumpContent()

        
        Ops=jobArray[lclCnt].Operations
        opCnt=0
        opTotCnt=len(jobArray[lclCnt].Operations.Group)

        for op in jobArray[lclCnt].Operations.Group:
            opCnt=opCnt+1
            print("\t\tOp:",opCnt," of ",opTotCnt)
            print("\t\t\tDir Op:",dir(op))      
            #print("\n")
            print("\t\t\tLabel:",op.Label)
            print("\t\t\tActive:",op.Active)
            print("\t\t\tBase:",op.Base)
            print("\t\t\tClearanceHeight:",op.ClearanceHeight)
            print("\t\t\tCoolantMode:",op.CoolantMode)
            print("\t\t\tCycleTime:",op.CycleTime)
            

            
            #print("\n")
            print("\t\t\tTool Controller:")
            print("\t\t\t\t Dir ToolController :",dir(op.ToolController))
            print("\t\t\t\t Label:",op.ToolController.Label)
            print("\t\t\t\t Name:",op.ToolController.Name)
            print("\t\t\t\t FullName:",op.ToolController.FullName)
            print("\t\t\t\t ToolNumber:",op.ToolController.ToolNumber)
            print("\t\t\t\t SpindleSpeed:",op.ToolController.SpindleSpeed)
            print("\t\t\t\t SpindleDir:",op.ToolController.SpindleDir)
            print("\t\t\t\t HorizFeed:",op.ToolController.HorizFeed)
            print("\t\t\t\t VertFeed:",op.ToolController.VertFeed)
            print("\n")

            
            print("\t\t\tPath:")
            print("\t\t\t\tDir Op Path:",dir(op.Path))

            
            print("\t\t\t\t BoundBox:",op.Path.BoundBox)
            print("\t\t\t\t Center:",op.Path.Center)
            print("\t\t\t\t Length:",op.Path.Length)
            print("\t\t\t\t Module:",op.Path.Module)
            print("\t\t\t\t GCode Commands:")
            for lclCmd in op.Path.Commands:
                print("\t\t\t\t\t\t Commands:",lclCmd.toGCode())
            print("\n")

            
        
        
        lclCnt += 1
    

    print("Jobs are Done\n\n\n\n")
    exit

    print("Walking ALL the tools: (in all jobs)")
    lclCnt=0
    while lclCnt < len(toolArray):
        print("\tPrinting Tool[",lclCnt,"]:")
        #print(dir(toolArray[0]))
        print("\t\tLabel:",toolArray[lclCnt].Label)
        print("\t\tToolNumber:",toolArray[lclCnt].ToolNumber)
        print("\t\tSpindleSpeed:",toolArray[lclCnt].SpindleSpeed)
        print("\t\tSpindleDir:",toolArray[lclCnt].SpindleDir)
        print("\t\tHorizFeed:",toolArray[lclCnt].HorizFeed)
        print("\t\tVertFeed:",toolArray[lclCnt].VertFeed)
        lclCnt += 1
    


    print("\n\n")
    print("Walking ALL the operations: (in all jobs)")
    lclCnt=0
    while lclCnt <len(opArray):
        print("\tPrinting Op[",lclCnt,"]:")
        print("\t\tLabel:",opArray[lclCnt].Label)
        #print(dir(opArray[lclCnt]))
        print("\t\tActive:",opArray[lclCnt].Active)
        print("\t\tState:",opArray[lclCnt].State)
        print("\t\tClearanceHeight:",opArray[lclCnt].ClearanceHeight)
        print("\t\tCycleTime:",opArray[lclCnt].CycleTime)
        if hasattr(opArray[lclCnt] ,"Direction"):
            print("\t\tDirection:",opArray[lclCnt].Direction)
        else:
            print("\t\tDirection:Undefined")
        if hasattr(opArray[lclCnt] ,"FinalDepth"):
            print("\t\tFinalDepth:",opArray[lclCnt].FinalDepth)
        else:
            print("\t\tFinalDepth:Undefined")
        print("\t\tParents:",opArray[lclCnt].Parents)
        print("\t\tCoolantMode:",opArray[lclCnt].CoolantMode)
        lclCnt += 1



print("============================Starting PATH stuff =============================================\n")

#Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
#Path.Log.trackModule(Path.Log.thisModule())
#c = Path.Command("G0 X10 Y20 Z30")
#print(c)


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


            

