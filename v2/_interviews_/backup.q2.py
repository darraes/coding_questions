from os import path


class ZNode:
    def __init__(self, name, parent, value):
        self.name = name
        self.parent = parent
        self.value = value
        self.edges = {}
        self.watcher_callback = None


class ZooKeeper:
    def __init__(self):
        self._root = ZNode("", None, None)

    def create(self, p, v):
        # TODO Validations
        parts = p.split("/")

        current = self._root
        for i in range(len(parts) - 1):
            if parts[i] in current.edges:
                current = current.edges[parts[i]]
            else:
                return False

        if parts[-1] in current.edges:
            return False

        current.edges[parts[-1]] = ZNode(parts[-1], current, v)
        return True

    def set(self, p, v):
        # TODO Validations
        parts = p.split("/")

        current = self._root
        for i in range(len(parts)):
            if parts[i] in current.edges:
                current = current.edges[parts[i]]
            else:
                return False

        current.value = v
        self._fire_callback_chain(current, p, v)
        return True

    def get(self, p):
        # TODO Validations
        parts = p.split("/")

        current = self._root
        for i in range(len(parts)):
            if parts[i] in current.edges:
                current = current.edges[parts[i]]
            else:
                return None

        return current.value

    def watch(self, p, callback):
        # TODO Validations
        parts = p.split("/")

        current = self._root
        for i in range(len(parts)):
            if parts[i] in current.edges:
                current = current.edges[parts[i]]
            else:
                return False

        current.watcher_callback = callback
        return True

    def _fire_callback_chain(self, current, p, v):
        while current:
            if current.watcher_callback:
                try:
                    current.watcher_callback(p, v)
                except:
                    print("Error")
            current = current.parent


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        zk = ZooKeeper()
        self.assertTrue(zk.create("a", "v1"))
        self.assertTrue(zk.create("a/b", "v2"))
        self.assertTrue(zk.create("a/b/c", "v3"))

        self.assertEqual("v1", zk.get("a"))
        self.assertEqual("v2", zk.get("a/b"))
        self.assertEqual("v3", zk.get("a/b/c"))

        self.assertTrue(zk.set("a/b/c", "v4"))
        self.assertTrue(zk.set("a/b", "v5"))
        self.assertEqual("v4", zk.get("a/b/c"))
        self.assertEqual("v5", zk.get("a/b"))

        self.assertFalse(zk.create("a/e/c", "v30"))
        self.assertFalse(zk.create("b/b/c", "v30"))

    def test_2(self):
        def callback1(p, v):
            print("callback1", p, v)

        def callback2(p, v):
            print("callback2", p, v)

        zk = ZooKeeper()
        self.assertTrue(zk.create("a", "v1"))
        self.assertTrue(zk.create("a/b", "v2"))
        self.assertTrue(zk.create("a/b/c", "v3"))
        self.assertTrue(zk.create("a/b/e", "v30"))

        self.assertTrue(zk.watch("a/b/c", callback1))
        self.assertTrue(zk.watch("a", callback2))
        self.assertTrue(zk.set("a/b/c", "v41"))

        print("===")
        self.assertTrue(zk.set("a/b", "v51"))

        print("===")
        self.assertTrue(zk.set("a/b/e", "v61"))


if __name__ == "__main__":
    unittest.main()
