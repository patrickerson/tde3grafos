
from dotenv import load_dotenv
from os.path import realpath
from os import environ



path_dotenv = realpath(".env")
load_dotenv(path_dotenv)
WORKDIR=realpath(environ.get("WORKDIR"))
ROOTDIR=realpath(environ.get("ROOTDIR"))
TESTDIR=realpath(environ.get("TESTDIR"))


