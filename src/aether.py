from math import cos,sin
r2=0.70710678118


class QuantumCircuit:

  def __init__(c,n,m=0):
    c.n=n
    c.m=m
    c.data=[]

  def __add__(c,c2):
    c3=QuantumCircuit(max(c.n,c2.n),max(c.m,c2.m))
    c3.data=c.data+c2.data
    return c3

  def initialize(c,k):
    c.data.clear()
    c.data.append(('init',[e for e in k]))

  def x(c,q):
    c.data.append(('x',q))

  def rx(c,T,q):
    c.data.append(('r',T,q))

  def h(c,q):
    c.data.append(('h',q))

  def cx(c,s,t):
    c.data.append(('cx',t))

  def measure(c,q,b):
    assert(b<c.m)
    c.data.append(('m',q,b))
  
def simulate(c,shots=1024,get='counts'):
  def s(x,y):
    return [r2*(x[j]+y[j])for j in range(2)],[r2*(x[j]-y[j])for j in range(2)]
  def t(x,y,T):
    return ((x[0]*cos(T/2)+y[1]*sin(T/2),x[1]*cos(T/2)-y[0]*sin(T/2)),
            (y[0]*cos(T/2)+x[1]*sin(T/2),y[1]*cos(T/2)-x[0]*sin(T/2)))
  if get!='statevector':
      raise NotImplementedError()
  k = [(0,0) for _ in range(2**c.n)]
  k[0] = (1.0,0.0)
  for gate in c.data:
    if gate[0]=='init':
      if not isinstance(gate[1][0], (list, tuple)):
        k = [[e,0] for e in gate[1]]
      else:
        k = [e for e in gate[1]]
    elif gate[0]=='x':
      if c.n==1 and gate[1]==0:
        k[0],k[1]=k[1],k[0]
      elif gate[1]==0:
        k[0],k[1]=k[1],k[0]
        k[2],k[3]=k[3],k[2]
      else:
        k[0],k[2]=k[2],k[0]
        k[1],k[3]=k[3],k[1]
    elif gate[0]=='h':
      if c.n==1 and gate[1]==0:
        k[0],k[1]=s(k[0],k[1])
      elif gate[1]==0:
        k[0],k[1]=s(k[0],k[1])
        k[2],k[3]=s(k[2],k[3])
      else:
        k[0],k[2]=s(k[0],k[2])
        k[1],k[3]=s(k[1],k[3])
    elif gate[0]=='r':
      T=gate[1]
      if c.n==1 and gate[2]==0:
        k[0],k[1]=t(k[0],k[1],T)
      elif gate[2]==0:
        k[0],k[1]=t(k[0],k[1],T)
        k[2],k[3]=t(k[2],k[3],T)
      else:
        k[0],k[2]=t(k[0],k[2],T)
        k[1],k[3]=t(k[1],k[3],T)
    elif gate[0]=='cx':
      if gate[1]==1:
        k[1],k[3]=k[3],k[1]
      else:
        k[2],k[3]=k[3],k[2]
  return k
