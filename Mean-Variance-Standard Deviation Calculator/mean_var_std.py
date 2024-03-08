import numpy as np

def calculate(list):
    if len(list) == 9:
        array = np.array(list).reshape((3,3))
        dictionary = {}

        dictionary['mean'] = [
            np.mean(array, axis=0).astype(float).tolist(),
            np.mean(array, axis=1).astype(float).tolist(),
            np.mean(array).astype(float)
        ]

        dictionary['variance'] = [
            np.var(array, axis=0).astype(float).tolist(),
            np.var(array, axis=1).astype(float).tolist(),
            np.var(array).astype(float)
        ]

        dictionary['standard deviation'] = [
            np.std(array, axis=0).astype(float).tolist(),
            np.std(array, axis=1).astype(float).tolist(),
            np.std(array).astype(float)
        ]

        dictionary['max'] = [
            np.max(array, axis=0).astype(float).tolist(),
            np.max(array, axis=1).astype(float).tolist(),
            np.max(array).astype(float)
        ]

        dictionary['min'] = [
            np.min(array, axis=0).astype(float).tolist(),
            np.min(array, axis=1).astype(float).tolist(),
            np.min(array).astype(float)
        ]

        dictionary['sum'] = [
            np.sum(array, axis=0).astype(float).tolist(),
            np.sum(array, axis=1).astype(float).tolist(),
            np.sum(array).astype(float)
        ]
    else:

        raise ValueError("List must contain nine numbers.")

    return dictionary 