import numpy as np
import scipy
from scipy.linalg import expm
def heisenberg_2body():
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    Hzz = np.kron(Sz,Sz)
    Hyy = np.kron(Sy,Sy).real
    Hxx = np.kron(Sx,Sx)
    Hmz = np.kron(Sz,I) + np.kron(I,Sz)
    Hmx = np.kron(Sx,I) + np.kron(I,Sx)
    return Hxx, Hyy, Hzz, Hmx, Hmz
def heisenberg_2body_assemble(Jx=1,Jy=1,Jz=1,hx=0,hz=0):
    xx, yy, zz, mx, mz = heisenberg_2body()
    H = Jx * xx + Jy * yy + Jz * zz + hx * mx + hz * mz
    return H

def heisenberg_3body(bound_cond='periodic'):
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    if bound_cond is 'periodic':
        Hzz = np.kron(np.kron(Sz,Sz),I) + np.kron(np.kron(I,Sz),Sz) + np.kron(np.kron(Sz,I),Sz)
        Hxx = np.kron(np.kron(Sx,Sx),I) + np.kron(np.kron(I,Sx),Sx) + np.kron(np.kron(Sx,I),Sx)
        Hyy = np.kron(np.kron(Sy,Sy),I) + np.kron(np.kron(I,Sy),Sy) + np.kron(np.kron(Sy,I),Sy)
        Hyy = Hyy.real
    elif bound_cond is 'open':
        Hzz = np.kron(np.kron(Sz, Sz), I) + np.kron(np.kron(I, Sz), Sz)
        Hxx = np.kron(np.kron(Sx, Sx), I) + np.kron(np.kron(I, Sx), Sx)
        Hyy = np.kron(np.kron(Sy, Sy), I) + np.kron(np.kron(I, Sy), Sy)
        Hyy = Hyy.real
    Hmz = np.kron(np.kron(Sz,I),I) + np.kron(np.kron(I,Sz),I) + np.kron(np.kron(I,I),Sz)
    Hmx = np.kron(np.kron(Sx,I),I) + np.kron(np.kron(I,Sx),I) + np.kron(np.kron(I,I),Sx)
    return Hxx, Hyy, Hzz, Hmx, Hmz

def heisenberg_3body_assemble(Jx=1,Jy=1,Jz=1,hx=0,hz=0,bound_cond='periodic'):
    xx, yy, zz, mx, mz = heisenberg_5body(bound_cond=bound_cond)
    H = Jx * xx + Jy * yy + Jz * zz + hx * mx + hz * mz
    return H

def heisenberg_4body(bound_cond='periodic'):
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    if bound_cond is 'periodic':
        Hzz = np.kron(np.kron(np.kron(Sz,Sz),I),I) + np.kron(np.kron(np.kron(I,Sz),Sz),I) + \
              np.kron(np.kron(np.kron(I,I),Sz),Sz) + np.kron(np.kron(np.kron(Sz,I),I),Sz)
        Hxx = np.kron(np.kron(np.kron(Sx, Sx), I), I) + np.kron(np.kron(np.kron(I, Sx), Sx), I) + \
              np.kron(np.kron(np.kron(I, I), Sx), Sx) + np.kron(np.kron(np.kron(Sx, I), I), Sx)
        Hyy = np.kron(np.kron(np.kron(Sy,Sy),I),I) + np.kron(np.kron(np.kron(I,Sy),Sy),I) + \
              np.kron(np.kron(np.kron(I,I),Sy),Sy) + np.kron(np.kron(np.kron(Sy,I),I),Sy)
        Hyy = Hyy.real
    elif bound_cond is 'open':
        Hzz = np.kron(np.kron(np.kron(Sz, Sz), I), I) + np.kron(np.kron(np.kron(I, Sz), Sz), I) + \
              np.kron(np.kron(np.kron(I, I), Sz), Sz)
        Hxx = np.kron(np.kron(np.kron(Sx, Sx), I), I) + np.kron(np.kron(np.kron(I, Sx), Sx), I) + \
              np.kron(np.kron(np.kron(I, I), Sx), Sx)
        Hyy = np.kron(np.kron(np.kron(Sy, Sy), I), I) + np.kron(np.kron(np.kron(I, Sy), Sy), I) + \
              np.kron(np.kron(np.kron(I, I), Sy), Sy)
        Hyy = Hyy.real
    Hmz = np.kron(np.kron(np.kron(Sz,I),I),I) + np.kron(np.kron(np.kron(I,Sz),I),I) + \
          np.kron(np.kron(np.kron(I,I),Sz),I) + np.kron(np.kron(np.kron(I,I),I),Sz)
    Hmx = np.kron(np.kron(np.kron(Sx, I), I), I) + np.kron(np.kron(np.kron(I, Sx), I), I) + \
          np.kron(np.kron(np.kron(I, I), Sx), I) + np.kron(np.kron(np.kron(I, I), I), Sx)
    return Hxx, Hyy, Hzz, Hmx, Hmz


def heisenberg_5body(bound_cond='periodic'):
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    if bound_cond is 'periodic':
        Hzz = np.kron(np.kron(np.kron(np.kron(Sz, Sz), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sz), Sz), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sz), Sz), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), Sz) + \
              np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), Sz)
        Hyy = np.kron(np.kron(np.kron(np.kron(Sy, Sy), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sy), Sy), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sy), Sy), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sy), Sy) + \
              np.kron(np.kron(np.kron(np.kron(Sy, I), I), I), Sy)
        Hyy = Hyy.real
        Hxx = np.kron(np.kron(np.kron(np.kron(Sx, Sx), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sx), Sx), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sx), Sx), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), Sx) + \
              np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), Sx)
    elif bound_cond is 'open':
        Hzz = np.kron(np.kron(np.kron(np.kron(Sz, Sz), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sz), Sz), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sz), Sz), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), Sz)
        Hyy = np.kron(np.kron(np.kron(np.kron(Sy, Sy), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sy), Sy), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sy), Sy), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sy), Sy)
        Hyy = Hyy.real
        Hxx = np.kron(np.kron(np.kron(np.kron(Sx, Sx), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, Sx), Sx), I), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), Sx), Sx), I) + \
              np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), Sx)
    Hmz = np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, Sz), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), Sz), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sz)
    Hmx = np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, Sx), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), Sx), I), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), I) + \
          np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sx)
    return Hxx, Hyy, Hzz, Hmx, Hmz

def heisenberg_5body_assemble(Jx=1,Jy=1,Jz=1,hx=0,hz=0,bound_cond='periodic'):
    xx, yy, zz, mx, mz = heisenberg_5body(bound_cond=bound_cond)
    H = Jx * xx + Jy * yy + Jz * zz + hx * mx + hz * mz
    return H


def heisenberg_6body(bound_cond='periodic'):
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    if bound_cond is 'periodic':
        Hzz = np.kron(np.kron(np.kron(np.kron(np.kron(Sz, Sz), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sz), Sz), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sz), Sz), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), Sz), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sz), Sz) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), I), Sz)

        Hyy = np.kron(np.kron(np.kron(np.kron(np.kron(Sy, Sy), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sy), Sy), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sy), Sy), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sy), Sy), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sy), Sy) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(Sy, I), I), I), I), Sy)
        Hyy = Hyy.real

        Hxx = np.kron(np.kron(np.kron(np.kron(np.kron(Sx, Sx), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sx), Sx), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sx), Sx), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), Sx), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sx), Sx) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), I), Sx)

    elif bound_cond is 'open':
        Hzz = np.kron(np.kron(np.kron(np.kron(np.kron(Sz, Sz), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sz), Sz), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sz), Sz), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), Sz), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sz), Sz)

        Hyy = np.kron(np.kron(np.kron(np.kron(np.kron(Sy, Sy), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sy), Sy), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sy), Sy), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sy), Sy), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sy), Sy)
        Hyy = Hyy.real

        Hxx = np.kron(np.kron(np.kron(np.kron(np.kron(Sx, Sx), I), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, Sx), Sx), I), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sx), Sx), I), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), Sx), I) + \
              np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sx), Sx)

    Hmz = np.kron(np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, Sz), I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sz), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sz), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), I), Sz)

    Hmx = np.kron(np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, Sx), I), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), Sx), I), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), I), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sx), I) + \
          np.kron(np.kron(np.kron(np.kron(np.kron(I, I), I), I), I), Sx)

    return Hxx, Hyy, Hzz, Hmx, Hmz