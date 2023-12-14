import os
from shutil import copy2 as copy
from shutil import rmtree as del_folder

if os.path.exists("build"):
    del_folder("build")

os.mkdir("build")

os.system("cd color-ai && cargo build --release")

copy("color-ai/target/release/color_ai_neuroflow.exe", "build/color_ai.exe")