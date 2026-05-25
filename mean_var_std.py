import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # List to 3x3 matrix
    matrix = np.array(list).reshape(3,3) # reshape the list into a bidimensional array (3x3)
    
    means = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).item()]
    variances = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).item()]
    stds = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).item()]
    maximums = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).item()]
    minimums = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).item()]
    sums = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).item()]
    
    # .item() is used to return python type values
    
    calculations = {
        "mean": means,
        "variance": variances,
        "standard deviation": stds,
        "max": maximums,
        "min": minimums,
        "sum": sums
    }


    return calculations