class A():
    def mesg(self):
        print("A")
  
  class F(A):
      def mesg(self):
        print("F")
        super(F, self).mesg()
  
  class B(A):
      def mesg(self):
          print("B")
          super(B, self).mesg()
  
  class C(A):
    def mesg(self):
        print("C")
        super(C, self).mesg()
  
  class D(C, B, F):
      def mesg(self):
          print("D")
          super(D,self).mesg()
  
  print("From D:")
  D().mesg()
  print("From C:")
  C().mesg()
  print(D.__mro__)
  print(D.mro())