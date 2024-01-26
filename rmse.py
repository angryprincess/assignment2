import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    n = len(pred)


    rmse = np.sqrt(1/n * sum((pred-tar)**2)) # TODO: Implement RMSE Calculation here...
    return rmse