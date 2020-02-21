from typing import Set, Dict, Any


class TaskGraph(object):
    def __init__(self, dependencies: Dict[Any, Set[Any]]):
        """Initializes the dependency graph from a dict of each task to its set of dependencies."""
        pass

    def executable_tasks(self) -> Set[Any]:
        """Returns the set of all tasks that can execute immediately because they have no dependencies."""
        pass

    def task_executed(self, task: Any) -> Set[Any]:
        """Marks a task as executed and returns any _new_ executable tasks in a set."""
        pass

    def all_tasks_executed(self) -> bool:
        """Returns true when all tasks have executed."""
        pass


def make_graph():
    return TaskGraph({
        "A": set(),
        "B": {"A"},
        "C": {"B"},
        "D": {"B", "G"},
        "E": {"B", "C", "D"},
        "F": {"E"},
        "G": set(),
    })


def run_tests():
    dag = make_graph()
    assert dag.executable_tasks() == {"A", "G"}

    assert dag.task_executed("A") == {"B"}
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"B", "G"}

    assert dag.task_executed("B") == {"C"}
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"C", "G"}

    assert dag.task_executed("G") == {"D"}
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"C", "D"}

    assert dag.task_executed("C") == set()
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"D"}

    assert dag.task_executed("D") == {"E"}
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"E"}

    assert dag.task_executed("E") == {"F"}
    assert not dag.all_tasks_executed()
    assert dag.executable_tasks() == {"F"}

    assert dag.task_executed("F") == set()
    assert dag.all_tasks_executed()
    assert dag.executable_tasks() == set()

if __name__ == '__main__':
    run_tests()