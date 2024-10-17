import importlib
import os

# Specify the folder name (which should be treated as a package)
folder_name = 'Functions'

# Dictionary to hold points for each module
points = {}

# List to hold the imported modules
modules = []

# Import all Python files in the folder and initialize points
for file_name in os.listdir(folder_name):
    if file_name.endswith('.py') and file_name != '__init__.py':
        module_name = file_name[:-3]  # Remove the '.py' extension
        # Dynamically import the module
        module = importlib.import_module(f"{folder_name}.{module_name}")
        modules.append(module)
        # Initialize points for each module
        points[module_name] = 0

# Run the matches between each pair of modules
for i in range(100):
    for j in range(len(modules)):
        for k in range(j+1, len(modules)):  # This ensures each pair plays only once per round
            module_1 = modules[j]
            module_2 = modules[k]
            
            # Get module names from the imported module objects
            module_1_name = module_1.__name__.split('.')[-1]
            module_2_name = module_2.__name__.split('.')[-1]

            # Get the current move lists
            module_1_moves = getattr(module_1, f"{module_1_name}_moves")
            module_2_moves = getattr(module_2, f"{module_2_name}_moves")

            # Call the `algo` method for each module with the moves of the other
            module_1_move = module_1.algo(module_2_moves)
            module_2_move = module_2.algo(module_1_moves)
            
            # Update the move lists for each module
            module_1_moves.append(module_1_move)
            module_2_moves.append(module_2_move)

            print(f"Game {i+1}: {module_1_name} move: {module_1_move}, {module_2_name} move: {module_2_move}")

            # Assign points based on the conditions
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

# Print the final points and move counts for each module
for module_name, point in points.items():
    module = importlib.import_module(f"{folder_name}.{module_name}")
    moves = getattr(module, f"{module_name}_moves")
    print(f"{module_name}_points: {point}")
    print(f"{module_name}_total_moves: {len(moves)}")