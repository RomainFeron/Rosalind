import os
import sys

# Problem name
problem = sys.argv[1]

# Directories initialisation
root_dir = '/home/rferon/perso/rosalind/'
data_dir = os.path.join(root_dir, 'problems', 'data', problem)
output_dir = os.path.join(root_dir, 'problems', 'output', problem)

# Import problem code
module_path = os.path.join(root_dir, 'problems', 'code')
sys.path.append(module_path)
solution = __import__(problem)

solution.run(data_dir, output_dir)
