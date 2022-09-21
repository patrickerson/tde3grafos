
from dotenv import load_dotenv
import os
from importlib import import_module

path_dotenv = os.path.realpath(".env")
load_dotenv(path_dotenv)
WORKDIR=os.environ.get("WORKDIR")
ROOTDIR=os.environ.get("ROOTDIR")
TESTDIR=os.environ.get("TESTDIR")
my_module = import_module("src.preprocessing")
t = my_module.Preprocessing()