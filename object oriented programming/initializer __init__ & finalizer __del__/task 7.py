"""
https://stepik.org/lesson/701975/step/9?unit=702076
"""
from typing import Union, List


class CPU:
    def __init__(self, name: str = None, fr: Union[int, float] = None):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str = None, volume: Union[int, float] = None):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str = None, cpu: CPU = None, total_mem_slots: int = 4, mem_slots: List[Memory] = None):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots if mem_slots is not None else []

    def get_config(self):
        memory_info = '; '.join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots])
        return [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            f'Память: {memory_info}'
        ]


mb = MotherBoard(cpu=CPU(), mem_slots=[Memory(), Memory()])
