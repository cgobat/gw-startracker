from numpy.core import  array, dot, sqrt
import time



num_test = 100000

def norm(x):
    return sqrt(dot(x, x))



def p_norm(x):
    return sqrt( x[0]*x[0] + x[1]*x[1] + x[2]*x[2]  )





x = [ 0.12645715, -0.0821628,  -0.22324085]
np_x = array( [ 0.12645715, -0.0821628,  -0.22324085] )





from ctypes import c_float, cdll
lib = cdll.LoadLibrary('./libfoo.so')

# Call C From Python
start_millis = int(round(time.time() * 1000))
print("\n\n100000 vect norm with C from Python using lists")
print("norm("+ str(x) +") = "+ str( lib.m_norm(c_float(x[0]), c_float(x[1]), c_float(x[2])) ) )
i = 0
while(i<num_test):
	res = lib.m_norm(c_float(x[0]), c_float(x[1]), c_float(x[2]))
	i+=1
print("T: " + str( int(round(time.time() * 1000)) - start_millis ))







# Numpy and List
start_millis = int(round(time.time() * 1000))
print("\n\n100000 vect norm with numpy and list")
print("norm("+ str(x) +") = "+ str(norm(x)))
i = 0
while(i<num_test):
	res = norm(x)
	i+=1
print("T: " + str( int(round(time.time() * 1000)) - start_millis ))


# Numpy and array
start_millis = int(round(time.time() * 1000))
print("\n\n100000 vect norm with numpy and array")
print("norm("+ str(np_x) +") = "+ str(norm(np_x)))
i = 0
while(i<num_test):
	res = norm(np_x)
	i+=1
print("T: " + str( int(round(time.time() * 1000)) - start_millis ))



# Manual and List
start_millis = int(round(time.time() * 1000))
print("\n\n100000 vect norm with numpy and list")
print("norm("+ str(x) +") = "+ str(p_norm(x)))
i = 0
while(i<num_test):
	res = p_norm(x)
	i+=1
print("T: " + str( int(round(time.time() * 1000)) - start_millis ))



# Manual and array
start_millis = int(round(time.time() * 1000))
print("\n\n100000 vect norm with numpy and array")
print("norm("+ str(np_x) +") = "+ str(p_norm(np_x)))
i = 0
while(i<num_test):
	res = p_norm(np_x)
	i+=1
print("T: " + str( int(round(time.time() * 1000)) - start_millis ))




