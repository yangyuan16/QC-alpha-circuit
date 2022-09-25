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

#
def heisenberg_5body_trotter_block():
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    I = np.array([[1, 0], [0, 1]])
    #
    Hzz_01 = np.kron(np.kron(np.kron(np.kron(Sz, Sz), I), I), I)
    Hyy_01 = np.kron(np.kron(np.kron(np.kron(Sy, Sy), I), I), I)
    Hyy_01 = Hyy_01.real
    Hxx_01 = np.kron(np.kron(np.kron(np.kron(Sx, Sx), I), I), I)
    Hmz_01 = np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), I)
    Hmx_01 = np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), I)
    #
    Hzz_12 = np.kron(np.kron(np.kron(np.kron(I, Sz), Sz), I), I)
    Hyy_12 = np.kron(np.kron(np.kron(np.kron(I, Sy), Sy), I), I)
    Hyy_12 = Hyy_12.real
    Hxx_12 = np.kron(np.kron(np.kron(np.kron(I, Sx), Sx), I), I)
    Hmz_12 = np.kron(np.kron(np.kron(np.kron(I, Sz), I), I), I)
    Hmx_12 = np.kron(np.kron(np.kron(np.kron(I, Sx), I), I), I)
    #
    Hzz_23 = np.kron(np.kron(np.kron(np.kron(I, I), Sz), Sz), I)
    Hyy_23 = np.kron(np.kron(np.kron(np.kron(I, I), Sy), Sy), I)
    Hyy_23 = Hyy_23.real
    Hxx_23 = np.kron(np.kron(np.kron(np.kron(I, I), Sx), Sx), I)
    Hmz_23 = np.kron(np.kron(np.kron(np.kron(I, I), Sz), I), I)
    Hmx_23 = np.kron(np.kron(np.kron(np.kron(I, I), Sx), I), I)
    #
    Hzz_34 = np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), Sz)
    Hyy_34 = np.kron(np.kron(np.kron(np.kron(I, I), I), Sy), Sy)
    Hyy_34 = Hyy_34.real
    Hxx_34 = np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), Sx)
    Hmz_34 = np.kron(np.kron(np.kron(np.kron(I, I), I), Sz), I)
    Hmx_34 = np.kron(np.kron(np.kron(np.kron(I, I), I), Sx), I)
    #
    Hzz_04 = np.kron(np.kron(np.kron(np.kron(Sz, I), I), I), Sz)
    Hyy_04 = np.kron(np.kron(np.kron(np.kron(Sy, I), I), Sy), Sy)
    Hyy_04 = Hyy_04.real
    Hxx_04 = np.kron(np.kron(np.kron(np.kron(Sx, I), I), I), Sx)
    Hmz_04 = np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sz)
    Hmx_04 = np.kron(np.kron(np.kron(np.kron(I, I), I), I), Sx)
    #
    Hzz = {'01': Hzz_01, '12': Hzz_12, '23':Hzz_23, '34':Hzz_34, '04':Hzz_04}
    Hyy = {'01': Hyy_01, '12': Hyy_12, '23':Hyy_23, '34':Hyy_34, '04':Hyy_04}
    Hxx = {'01': Hxx_01, '12': Hxx_12, '23':Hxx_23, '34':Hxx_34, '04':Hxx_04}
    Hmz = {'01': Hmz_01, '12': Hmz_12, '23':Hmz_23, '34':Hmz_34, '04':Hmz_04}
    Hmx = {'01': Hmx_01, '12': Hmx_12, '23':Hmx_23, '34':Hmx_34, '04':Hmx_04}
    return Hxx, Hyy, Hzz, Hmz, Hmx
