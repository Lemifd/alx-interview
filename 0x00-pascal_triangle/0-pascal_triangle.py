def pascal_triangle(n):
    a=[1]
    for i in range(1,n+1):
      for k in range(1,i):
         a.insert(i,k)
      print(a)

pascal_triangle(4)
