import torch

def tensor_to_obj(tensor, filename):
    # Ensure tensor is on CPU and detached from computation graph
    tensor = tensor.cpu().detach()
    
    # Open the file for writing
    with open(filename, 'w') as f:
        # Write the header
        f.write('# OBJ File\n\n')
        
        # Write vertices
        for i in range(tensor.shape[1]):
            for j in range(3):
                vertex = tensor[0, i, j]
                f.write(f'v {vertex[0]} {vertex[1]} {vertex[2]}\n')
        
        # Write faces
        for i in range(tensor.shape[1]):
            f.write(f'f {i*3+1} {i*3+2} {i*3+3}\n')


