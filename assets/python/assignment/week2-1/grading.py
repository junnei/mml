import numpy as np

def grading_matrix_addition(func):
    for idx in range(100):
        x = np.random.randint(100)
        y = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, y))
        B = np.random.randint(-100,100,size=(x, y))
        if (func(A,B)!=A+B).any():
            print("Something Wrong. Try again!")
            return False
    print("Success! Go to next step!")
    return True

def grading_matrix_multiplication(func):
    for idx in range(100):
        x = np.random.randint(100)
        y = np.random.randint(100)
        z = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, y))
        B = np.random.randint(-100,100,size=(y, z))
        if (func(A,B)!=A@B).any():
            print("Something Wrong. Try again!")
            return False
    print("Success! Go to next step!")
    return True
    

def grading_hadamard_product(func):
    for idx in range(100):
        x = np.random.randint(100)
        y = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, y))
        B = np.random.randint(-100,100,size=(x, y))
        if (func(A,B)!=A*B).any():
            print("Something Wrong. Try again!")
            return False
    print("Success! Go to next step!")
    return True


def grading_inverse(func):
    for idx in range(100):
        x = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, x))
        if (func(A)!=np.linalg.inv(A)).any():
            return False
    print("Success! Go to next step!")
    return True
    

def grading_transpose(func):
    for idx in range(100):
        x = np.random.randint(100)
        y = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, y))
        if (func(A)!=A.T).any():
            print("Something Wrong. Try again!")
            return False
    print("Success! Go to next step!")
    return True
    
def grading_is_symmetric(func):
    for idx in range(100):
        x = np.random.randint(100)
        A = np.random.randint(-100,100,size=(x, x))
        B = np.transpose(A)
        if func(A)!=np.allclose(A,B):
            print("Something Wrong. Try again!")
            return False
    print("Success! Go to next step!")
    return True