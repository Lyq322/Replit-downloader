import shutil
import os

for root, dirs, files in os.walk("./Files/", topdown=False):
    for name in files:
        if name.endswith(".zip"):
            try:
                os.mkdir("./Replits/" + root[8:] + "/" + name[:-4])
            except:
                pass

            print(os.path.join(root, name), "./Replits/" + root[8:] + "/" + name[:-4])
            shutil.unpack_archive(os.path.join(root, name), "./Replits/" + root[8:] + "/" + name[:-4])

    for name in dirs:
        #print(os.path.join(root, name))
        pass

shutil.rmtree("./Files")
