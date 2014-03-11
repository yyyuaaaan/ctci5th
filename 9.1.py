"""__author__ = 'anyu'
9.1 A child is running up a staircase with n steps, and can hop either 1step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""
def npermu(n): # wrong! not permutation, there is no difference between hops
    if n is 1: return 1
    if n is 2: return 2
    if n is 3: return 4
    else:
        if n//3 is 0: return 4*(n-1)*npermu(n-3)
        if n//2 is 0: return 2*(n-1)*npermu(n-2)
        return n*npermu(n-1)


def count_ways(n):
    """
    like fibonacci
    """
    if n <0: return 0
    if n is 0: return 1
    return count_ways(n-1)+ count_ways(n-2)+count_ways(n-3)

print count_ways(2)

def count_ways_iter(n):
    """
    iteratively
    """
    if n <0: return 0
    if n is 0: return 1

    tempcount = [0]*(n+1)
    tempcount[0]=1; tempcount[1]=1; tempcount[2]=2
    for i in range(3,n+1):
        tempcount[i] = tempcount[i-1]+tempcount[i-2]+tempcount[i-3]
    return tempcount[n]

print count_ways_iter(1000)

def count_ways_iter_haha(n):
    """
    iteratively, do not even maintain a array, only 6 temp variables
    """
    if n <0: return 0
    if n is 0: return 1
    if n is 1: return 1

    t1=0; t2=1; t3=1

    for i in range(2,n+1):
        t4= t1+t2+t3
        t1=t2
        t2=t3
        t3=t4
    return t4

print count_ways_iter_haha(10000)  # very funny！！！

"""
matrix edition code too long, though O(logn), code hard to maintain and read, developing time
空间复杂度O(1)，时间复杂度O(n)，看起来既简单又快速。可是，我们还有更快的解法。 根据上面的递推公式，我们可以得到它的矩阵版本：
从上图可以看出，写成矩阵递推形式，可以让我们一推到底。最后的f(1)=f(2)=1， 因此，这个问题就转换成了，如何求矩阵的幂。
当然了，要快速，不然就没有什么意义了。 我们先把问题退化一下，先不考虑求矩阵的幂，而是求一个整数的幂，这个够简单的吧。
先来看看最naive的解法：(方便起见，这里假设n为非负数，不对n小于0的情况做讨论)
时间复杂度O(n)。现在让我们来考虑一种更快的方法，假设我们要计算m^13 ， 然后我们把指数13写成二进制形式13=1101，
一开始结果res=1.我们要计算的幂可以写成：
m^13 = m^1 * m^4 * m^8
而且由于每次res去乘以的数(如果该位为0则不乘)都是上一次那个数的平方， 所以，这个数我用完一次，就对它取平方，准备下一次的使用即可。看代码：
时间复杂度O(logn)，正是我们想要的快速版本。OK， 这时候如果让你快速求矩阵的幂，是不是很简单了？只需要将实数乘法改成矩阵乘法即可。






"""