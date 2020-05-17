import numpy as np

def get_rotation_matrix(rad):
    """ 
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                  [np.sin(rad), np.cos(rad)]])
    return rot

A, B, H, M = map(int, input().split())

tan = np.array([0, A])
chou = np.array([0, B])

tanrot = get_rotation_matrix(((-30*H-0.5*M)*np.pi)/180) #分にも影響される
chourot = get_rotation_matrix(((-6*M)*np.pi)/180)

tan = np.dot(tanrot, tan)
chou = np.dot(chourot, chou)
zero = np.array([0, 0])

print(np.linalg.norm(chou-tan))