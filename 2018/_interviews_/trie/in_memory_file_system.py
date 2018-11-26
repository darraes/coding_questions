# Develop an in-memory structure to store files given their paths.
# The methods that should be present are:
# 
# - save_file(dir_path, file_name, file_contents)
# - create_directory(dir_path)
# - list_files(dir_path, recurse)
# - attach_watcher(dir_path, callback)
# 
# For the watcher, if the trigger is on node A, we must callback on the watcher
# of all parent directories of node A. Only file add/update/remove trigger
# callbacks
# 
# Note that the dir_path is a path to the directory with the format "a/b/c".
# For simplicity we are not passing the file name as part of the path and
# already dealing with the broken down directory/file

from copy import copy
from collections import deque
from os import path

class DirNode(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.sub_dirs = {}
        self.files = {}
        self.dir_watcher_callback = None

    def ensure_sub_dir(self, dir_name):
        if dir_name not in self.sub_dirs:
            self.sub_dirs[dir_name] = DirNode(dir_name, self)
        return self.sub_dirs[dir_name]

    def remove_dir(self, dir_name):
        if dir_name in self.sub_dirs:
            del self.sub_dirs[dir_name]
            return True
        return False

    def save_file(self, file_name, file_contents):
        self.files[file_name] = file_contents

    def remove_file(self, file_name):
        if file_name in self.files:
            del self.files[file_name]
            return True
        return False

    def attach_dir_watcher(self, watcher_callback):
        self.dir_watcher_callback = watcher_callback


class FileSystem(object):
    def __init__(self):
        self.root = DirNode("/", parent=None)


    def split_path(self, path):
        return [d for d in path.split("/") if d != ""]


    def ensure_directory(self, dir_path):
        dir_parts = self.split_path(dir_path)

        node = self.root
        for sub_dir in dir_parts:
            node = node.ensure_sub_dir(sub_dir)

        return node


    def list_files(self, dir_path, recurse):
        node = self.ensure_directory(dir_path)
        results = []
        queue = deque()
        queue.append((dir_path, node))

        while len(queue) > 0:
            cur_dir, cur_node = queue.popleft()
            for file in cur_node.files:
                results.append(path.join(cur_dir, file))

            if not recurse:
                break

            for sub_name, sub_node in cur_node.sub_dirs.items():
                queue.append((path.join(cur_dir, sub_name), sub_node))

        return results


    def remove_directory(self, dir_path):
        dir_parts = self.split_path(dir_path)

        node = self.root
        for sub_dir in dir_parts:
            if sub_dir not in self.sub_dirs:
                return False
            node = node.sub_dirs[sub_dir]

        return node.parent.remove_dir(dir_parts[-1])


    def save_file(self, dir_path, file_name, file_contents):
        node = self.ensure_directory(dir_path)
        node.save_file(file_name, file_contents)
        self._fire_callback_chain(node, file_name)


    def remove_file(self, dir_path, file_name):
        dir_parts = self.split_path(dir_path)

        node = self.root
        for sub_dir in dir_parts:
            if sub_dir not in self.sub_dirs:
                return False
            node = node.sub_dirs[sub_dir]

        res = node.remove_file(file_name)
        self._fire_callback_chain(node, file_name)
        return res


    def _fire_callback_chain(self, node, file_name):
        while node:
            if node.dir_watcher_callback:
                node.dir_watcher_callback()
            node = node.parent


    def attach_dir_watcher(self, dir_path, callback):
        node = self.ensure_directory(dir_path)
        node.attach_dir_watcher(callback)


    def print_all(self):
        self._print_impl(self.root)


    def _print_impl(self, node, level = 0, connectors = set(), is_last = set()):
        pad_count = 2 * level
        padding = [" "] * pad_count

        dir_line = padding + ["-"] + list(node.name) + [")"]
        for connector in copy(connectors):
            # For each connector request, print it on the right index
            dir_line[connector + 1] = "|"
            # if this is suppose to the be last instance of this connector
            # remove it from the request list
            if connector in is_last:
                connectors.remove(connector)
                is_last.remove(connector)
        print("".join(dir_line))

        i = 0
        for _, child in node.sub_dirs.items():
            if i < len(node.sub_dirs) - 1:
                # if this is not the last directory tell all nodes below that
                # they should print the '|' on the position @pad_count so the
                # vertical line connecting to this node is rendered
                connectors.add(pad_count)
            elif pad_count in connectors:
                # This is will be the very last sub-directory, so we tell it to
                # print the connector '|' and remove it from the @connectors
                # printing list requests after that. Basically the next
                # sub-directory print should be the last for this instance of
                # the connector
                is_last.add(pad_count)
            self._print_impl(child, level + 1, connectors, is_last)
            i += 1

        for file_name, _ in node.files.items():
            # do the file printing
            file_line = padding + [" |_ "] + list(file_name)
            # For each connector request, print it on the right index
            for connector in connectors:
                file_line[connector + 1] = "|"
            print("".join(file_line))




###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        file_system = FileSystem()
        file_system.save_file("a/b/c/d", "daniel.pdf", "")
        file_system.save_file("a/b/c/d", "daniel2.pdf", "")
        file_system.save_file("a/b/e", "daniel3.pdf", "")
        file_system.ensure_directory("a/b/c/f")
        file_system.attach_dir_watcher("a/b", lambda : print("in b"))
        file_system.attach_dir_watcher("a", lambda : print("in a"))
        file_system.save_file("a/b/e", "daniel3.pdf", "")
        file_system.ensure_directory("a/g")
        file_system.ensure_directory("a/g/b")
        file_system.save_file("a/g/b", "daniel2.pdf", "")
        file_system.save_file("a/g/b", "daniel4.pdf", "")
        file_system.ensure_directory("a/g/d")
        file_system.print_all()

        files = file_system.list_files("a", True)
        print()
        for f in files:
            print(f)


if __name__ == '__main__':
    unittest.main()