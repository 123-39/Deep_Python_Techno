"""
Profiler
"""
import weakref
import cProfile
import pstats
import io
from memory_profiler import profile


NUM_IMG = 500_000


class SimpleClass():
    """
    Class without slots
    """

    def __init__(self, model, cost):
        self.model = model
        self.cost = cost


class SlotsClass():
    """
    Class with slots
    """

    __slots__ = ("model", "cost")

    def __init__(self, model, cost):
        self.model = model
        self.cost = cost


def profile_deco(func):
    """
    Profiler decorator
    """
    def wrap(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)

        profiler.disable()
        out = io.StringIO()
        stats = pstats.Stats(profiler, stream=out)
        stats.print_stats()
        print(out.getvalue())
        return result

    return wrap


def process_list(lst):
    """
    class operations
    """
    for obj in lst:
        new_cost = obj.model + obj.cost
        obj.model += obj.cost
        obj.cost = new_cost


@profile
def memory_profile():
    """
    Check memory profiler
    """

    simple_classes = [SimpleClass(1, 4) for _ in range(NUM_IMG)]

    slots_classes = [SlotsClass(1, 4) for _ in range(NUM_IMG)]

    weakref_class = []
    parent_class = SimpleClass(1, 4)
    for _ in range(NUM_IMG):
        weakref_class.append(weakref.ref(parent_class)())

    process_list(simple_classes)
    process_list(slots_classes)
    process_list(weakref_class)

    del simple_classes
    del slots_classes
    del weakref_class


@profile_deco
def call_profile():
    """
    Check call profiler
    """

    simple_classes = [SimpleClass(1, 4) for _ in range(NUM_IMG)]

    slots_classes = [SlotsClass(1, 4) for _ in range(NUM_IMG)]

    weakref_class = []
    parent_class = SimpleClass(1, 4)
    for _ in range(NUM_IMG):
        weakref_class.append(weakref.ref(parent_class)())

    process_list(simple_classes)
    process_list(slots_classes)
    process_list(weakref_class)

    del simple_classes
    del slots_classes
    del weakref_class


if __name__ == '__main__':

    memory_profile()

    call_profile()
