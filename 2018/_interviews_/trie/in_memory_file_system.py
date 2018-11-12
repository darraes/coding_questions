# Develop an in-memory structure to store files given their paths.
# The methods that should be present are:
# 
# - create_or_update_file(dir_path, file)
# - create_directory(dir_path)
# - remove_file(dir_path, file)
# - remove_file(dir_path)
# - attach_watcher(dir_path, file)
# - attach_watcher(dir_path)
# 
# Note that the dir_path is a path to the directory with the format "a/b/c".
# For simplicity we are not passing the file name as part of the path and
# already dealing with the broken down directory/file

class FileSystem(object):
    def __init__(self):
        pass
        

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        pass