'''
Дано натуральное N⩽100. Выведите произведение всех нечётных натуральных чисел, не превосходящих N.
'''

N = int(input())
N_double_fact=1
for i in range(0,N+1):
    if i%2==1:
        N_double_fact= N_double_fact*i
print(N_double_fact)

'''
Пусть у нас есть следующий список, в котором элементы -- tuple из строк:

items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]

Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:

sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'),]

Что нужно вставить вместо "###" в следующем выражении, чтобы получить сортировку?
'''

sorted_items = sorted(items, key=lambda x:x[1][-1])

'''
Дан массив A[0,...,N-1]. Напишите функцию, принимающую один обязательный аргумент A и один опциональный аргумент erase, по умолчанию равный 1 и возвращающую массив B[0,…,N−1],
где B_i = A_0 + ... + A_{i}B --- массив частичных сумм массива AA, предварительно удалив из массива BB все элементы, равные erase.

Постарайтесь сделать это за время O(N)O(N) без использования Numpy.
'''

def cumsum_and_erase(A,erase=1):
    B=list()
    for i in range(0,len(A)):
        if sum(A[:i+1])!= erase:            
            B.append(sum(A[:i+1]))
    return B
   
'''
Реализуйте класс "Нейрон", у которого будет несколько методов
 __init__. Принимает на вход массив весов нейрона --- w = (w_1, \ldots, w_n), 
 а также функцию активации f (аргумент по умолчанию f(x)=x). Сохраняет веса и функцию внутри класса.
forward. 

Принимает на вход массив x = (x_1, \ldots, x_N) --- входы нейрона. Возвращает f(w_1x_1 + \ldots + w_nx_n). 
Возвращает массив x, который подавался на вход функции forward при её последнем вызове.
'''

class Neuron:
    def __init__(self, w, f = lambda x: x):
        self.w=w
        self.f=f

    def forward(self, x):
        self.x=x
        return self.f(sum([self.x[i]*self.w[i] for i in range(len(self.x))]))
    def backlog(self):
        return self.x
        
