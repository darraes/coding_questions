# https://www.careercup.com/question?id=6282171643854848


def allocate_task_impl(task_id, allocations, tasks, capacities):
    if task_id == len(tasks):
        return True

    for idx, server_capacity in enumerate(capacities):
        if tasks[task_id] <= server_capacity:
            capacities[idx] -= tasks[task_id]
            allocations[task_id] = idx

            if allocate_task_impl(task_id + 1,
                                  allocations,
                                  tasks,
                                  capacities):
                return True

            capacities[idx] += tasks[task_id]
            del allocations[task_id]

    return False


def allocate_task(tasks, capacities):
    return allocate_task_impl(0, {}, tasks, capacities)
    


####### =============== TESTS =============== 
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertTrue(allocate_task(
            [8, 4, 8, 4, 6, 6, 8, 8 ], [8, 16, 8, 32]))
        self.assertFalse(allocate_task([4 ], [1, 3]))


if __name__ == '__main__':
    unittest.main()