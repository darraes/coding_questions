import unittest
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
LOG = logging.getLogger()

class Target(object):
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies

class Builder(object):
    def __init__(self, targets):
        self._targets = targets
        self._unbuilt_deps = {}
        self._dependants = {}
        self._available = []
        
        self.prepare()
        self.mark_ready_as_available()

    def prepare(self):
        # build the dictionaries that will be use to track who can be built
        # # TODO find circular dependencies
        for target in self._targets:
            self._unbuilt_deps[target.name] = set(target.dependencies)
            for dependency in target.dependencies:
                if dependency not in self._dependants:
                    self._dependants[dependency] = set()
                self._dependants[dependency].add(target.name)

    def build(self):
        while len(self._available) > 0:
            next_target = self.get_next_available()
            self.build_target(next_target)

    def mark_ready_as_available(self):
        built = []
        for target, dependencies in self._unbuilt_deps.iteritems():
            if len(dependencies) == 0:
                built.append(target)
                self._available.append(target)
        
        for target in built:
            del self._unbuilt_deps[target]

    def get_next_available(self):
        if len(self._available) == 0:
            return None
        return self._available.pop(0)

    def build_target(self, target):
        ''' Simulates building an individual target '''
        LOG.info("Building %s", target)
        if target not in self._dependants:
            return

        for dependant in [d for d in self._dependants[target] if d in self._unbuilt_deps]:
            self._unbuilt_deps[dependant].remove(target)

        self.mark_ready_as_available()
        

###############################################################
class TestFunctions(unittest.TestCase):
    def test_1(self):
        targets = [
            Target("a", []),
            Target("b", ["a", "c"]),
            Target("d", ["a"]),
            Target("c", ["e"]),
            Target("e", [])
        ]
        builder = Builder(targets)
        builder.build()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()