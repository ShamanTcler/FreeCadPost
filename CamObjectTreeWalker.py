import os
from importlib import reload
from inspect import getmembers, isfunction


print("\n\nStarting CamObjectTreeWalker.py\n\n")

print("\n======================Generic FreeCAD stuff ===================================================\n")


# This is the path FreeCAD directory, it is used to import the FreeCAD module
FREECADPATH = 'C:/FreeCadBeta/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD



import JobUtils
print("\n\nAvailable functions in JobUtils  Note: [] implies empty list\n")
print(getmembers(JobUtils, isfunction))
print("\nComplete contents of JobUtils\n")
txt=dir(JobUtils)
print("txt:",txt,"\n")
print("Done ....Available functions in JobUtils\n")

import Tests.PathTestUtils as PathTestUtils

print("\n\nAvailable functions in PathTestUtils   Note: [] implies empty list\n")
print(getmembers(PathTestUtils, isfunction))
print("\nComplete contents of PathTestUtils\n")
txt=dir(PathTestUtils)
print("txt:",txt,"\n")
print("Done ....Available functions in PathTestUtils\n")

print("\n======================Starting to work with A file ===================================================\n")

# This is the path to the file that we want to open
filepath = "test1.FCStd"

print("\nNow we are going to open the file:",filepath,"\n")
# Try to open the file
try:
    doc=FreeCAD.open(filepath)
except OSError as error : 
    print(error) 
    print("Unable to open the file exiting. Exit code:1\n")
    exit(1)


print("FreeCAD filename (the \"Label\"):",doc.Label)

print("\n\n\nThese are global app settings:")
print("\t- Available lib paths for tools:\n\t\t",JobUtils._get_available_tool_library_paths())
toolPaths=JobUtils._get_available_tool_library_paths()
for aPath in toolPaths:
    print("\t\t",aPath)
print("\n")

# HARD CODED FOR NOW
toolDirs=JobUtils._get_available_tool_library_paths()
print("\t- toolDirs[0][2]\n\t\t", toolDirs[0][2])
print("\n")

toolList=JobUtils._read_library(toolDirs[0][2])
print("\n")
print ("\t- toolList: ")
for aTool in toolList:
    print("\t\t:",aTool)
print("\n")

print("Done with tools\n\n\n\n")


print("======================Starting Object Walk ===================================================\n")


docObjs=doc.Objects
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

print("\nWalking the file based on JOBS\n\n\n\n")

if len(jobArray) > 0:
    lclCnt=0
    

    while lclCnt < len(jobArray):
        
        
        print("\n\nPrinting JobArray[",lclCnt,"]:")

        # If you want to see all the attributes of the jobArray
        #print(dir(jobArray[lclCnt]))

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
            
            # If you want to see all the attributes of the "op"
            #print("\t\t\tDir Op:",dir(op))      
            #print("\n")

            print("\t\t\tLabel:",op.Label)
            print("\t\t\tActive:",op.Active)
            print("\t\t\tBase:",op.Base)
            print("\t\t\tClearanceHeight:",op.ClearanceHeight)
            print("\t\t\tCoolantMode:",op.CoolantMode)
            print("\t\t\tCycleTime:",op.CycleTime)
            

            
            #print("\n")
            print("\t\t\tTool Controller:")
            # If you want to see all the attributes of the "op.ToolController"
            #print("\t\t\t\t Dir ToolController :",dir(op.ToolController))
            
            print("\t\t\t\t Name:",op.ToolController.Name)
            print("\t\t\t\t FullName:",op.ToolController.FullName)
            print("\t\t\t\t ToolNumber:",op.ToolController.ToolNumber)
            print("\t\t\t\t SpindleSpeed:",op.ToolController.SpindleSpeed)
            print("\t\t\t\t SpindleDir:",op.ToolController.SpindleDir)
            print("\t\t\t\t HorizFeed:",op.ToolController.HorizFeed)
            print("\t\t\t\t VertFeed:",op.ToolController.VertFeed)
            print("\n")

            
            print("\t\t\tPath:")
            # If you want to see all the attributes of the "op.Path"
            #print("\t\t\t\tDir Op Path:",dir(op.Path))

            
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
  
    print("\nWalking the file based on TOOLS (in all jobs)\n\n\n\n")
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
    


    print("\nWalking the file based on OPERATIONS (in all JOB)\n\n\n\n")
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

# Be polite and close the document
print("\n\nClosing the file: ",doc.Name,"\n\n")
FreeCAD.closeDocument(doc.Name) 

# Exit with normal termination
exit(0)
