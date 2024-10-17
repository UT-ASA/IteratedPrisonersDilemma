import importlib
import os

"""
DO NOT MODIFY!!
This is the runner code to test your functions
Run this file to verify that your code is doing what you want it to do
"""

folder_name = 'Functions'
points = {}
modules = []

for file_name in os.listdir(folder_name):
    if file_name.endswith('.py') and file_name != '__init__.py':
        module_name = file_name[:-3]  
        module = importlib.import_module(f"{folder_name}.{module_name}")
        modules.append(module)
        points[module_name] = 0

for i in range(1000):
    for j in range(len(modules)):
        for k in range(j+1, len(modules)):
            module_1 = modules[j]
            module_2 = modules[k]
            
            module_1_name = module_1.__name__.split('.')[-1]
            module_2_name = module_2.__name__.split('.')[-1]

            module_1_moves = getattr(module_1, f"{module_1_name}_moves")
            module_2_moves = getattr(module_2, f"{module_2_name}_moves")

            module_1_move = module_1.algo(module_2_moves)
            module_2_move = module_2.algo(module_1_moves)
            
            module_1_moves.append(module_1_move)
            module_2_moves.append(module_2_move)

            if not module_1_move and not module_2_move:
                points[module_1_name] += 3
                points[module_2_name] += 3
            elif not module_1_move and module_2_move:
                points[module_2_name] += 5
            elif module_1_move and not module_2_move:
                points[module_1_name] += 5
            else:
                points[module_1_name] += 1
                points[module_2_name] += 1

for module_name, point in points.items():
    module = importlib.import_module(f"{folder_name}.{module_name}")
    moves = getattr(module, f"{module_name}_moves")
    print(f"{module_name}_points: {point}")
    print(f"{module_name}_total_moves: {len(moves)}")