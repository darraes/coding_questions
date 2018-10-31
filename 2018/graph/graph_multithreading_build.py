import unittest

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
        
        self._prepare()
        self._mark_ready_as_available()

    def _prepare(self):
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
            next_target = self._get_next_available()
            self._build_target(next_target)

    def _mark_ready_as_available(self):
        ''' Looks through out the built dependencies and mark targets that are
            ready to be built as "available".
            In a multi-threaded scenario, we would tick idle threads every time
            a new target is available to avoid polling loops
        '''
        built = []
        for target, dependencies in self._unbuilt_deps.iteritems():
            if len(dependencies) == 0:
                built.append(target)
                self._available.append(target)
        
        for target in built:
            del self._unbuilt_deps[target]

    def _get_next_available(self):
        ''' Gets an available target to build.
            If this was multi-threaded, threads would just get a target to build
            by calling this method.
        '''
        if len(self._available) == 0:
            return None
        return self._available.pop(0)

    def _build_target(self, target):
        ''' Simulates building an individual target '''
        print "Building ", target
        if target not in self._dependants:
            return

        for dependant in [d for d in self._dependants[target] if d in self._unbuilt_deps]:
            self._unbuilt_deps[dependant].remove(target)

        self._mark_ready_as_available()
        

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


if __name__ == '__main__':
    unittest.main()