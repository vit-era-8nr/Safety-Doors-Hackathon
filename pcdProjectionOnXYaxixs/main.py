import numpy as np
import open3d as o3d
import os

def getFilesName(path):
    files = os.listdir(path)
    return files

def rewriteFile(sourcePath, resPath):
 result = []
 with open(sourcePath, "r") as file:
  lines = file.readlines()
  for i in range(len(lines)):
   if i < 11:
    result.append(lines[i])
   else:
    splittedL = lines[i].split(" ")
    splittedL[2] = "0.0"
    res = " ".join(splittedL)
    result.append(res)
 with open(resPath, "a") as file:
  for r in result:
   file.write(r)

def changeExtension(fileName, fileType, path):
    sourceName = path + fileName
    base = os.path.splitext(sourceName)[0]
    os.rename(sourceName, base + fileType)

def createJPG(path, imagePath):
    pcd = o3d.io.read_point_cloud(path, format="pcd")
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.get_render_option().point_color_option = o3d.visualization.PointColorOption.Color
    vis.get_render_option().point_size = 10.0
    vis.add_geometry(pcd)
    vis.capture_screen_image(imagePath, do_render=True)
    vis.destroy_window()

def main():
    testPath = "test/"
    testResPath = "testRes/"
    testFileNames = getFilesName(testPath)
    for t in testFileNames:
        changeExtension(t, ".txt", testPath)

    tfn = getFilesName(testPath) # (...).txt
    for t in tfn:
        rewriteFile(testPath + t, testResPath + t)

    testResFileNames = getFilesName(testResPath)
    for trfn in testResFileNames:
        changeExtension(trfn, ".pcd", testResPath)

    pathToPCD = getFilesName(testResPath)
    for ptPCD in pathToPCD:
        pathJPG = "".join(ptPCD.split(".")[0]) + ".jpg"
        createJPG(testResPath + ptPCD, "resultJPG/" + pathJPG) # arg_1 путь до pcd arg_2 путь до картинки








if __name__ == "__main__":
 main()