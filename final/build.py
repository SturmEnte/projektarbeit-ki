# Author: SturmEnte (Jonas)

import os
from shutil import copy2 as copy
from shutil import copytree as copy_folder
from shutil import rmtree as del_folder

if os.path.exists("build"):
    del_folder("build")

os.mkdir("build")
os.mkdir("build/color-ai")

os.system("cd color-ai && cargo build --release")

if os.name == "nt": # Windows
    copy("color-ai/target/release/color_ai_neuroflow.exe", "build/color-ai/color_ai.exe")
elif os.name == "posix": # Linux
    copy("color-ai/target/release/color_ai_neuroflow", "build/color-ai/color_ai")
else:
    raise "OS not recognised!"

copy("webserver.py", "build/webserver.py")
copy("color-ai/2023_2_cai", "build/color-ai/2023_2_cai")
copy_folder("color-ai/website", "build/color-ai/website")
copy_folder("index", "build/index")
copy_folder("game-ai/web", "build/game-ai/web")