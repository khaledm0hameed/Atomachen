import os,shutil
os.chdir("exampel")
for filename in os.listdir("."):
    if filename.endswith('png')or filename.endswith('jpg')or filename.endswith('jpeg'):
        shutil.move(filename,"img")
    elif filename.endswith("mp4"):
         shutil.move(filename,"mp4")
    else :
         if filename.endswith('img'):
              continue
         shutil.move(filename,"other")

