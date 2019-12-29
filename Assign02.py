# 完全数を求めるプログラム
# 2019/Dec/19


def sumDivisors( n ):
    summ = 0
    for m in range( 1, n//2+1 ):
        if n % m == 0: summ += m
    return summ
 
# 低速版   
for n in range( 6, 1000 ):
    if sumDivisors( n ) == n:
        print( n )

# メルセンヌ数を使った高速版 
import math

bcomp = "1"
bmelsen = "1"
for n in range( 30 ):
    bmelsen = bmelsen + "1"
    bcomp = "1" + bcomp + "0"

    #メルセンヌ数が素数であるかどうか

    number = int( bmelsen , base=2 )

    def sosu( target ):
        dest = int( math.sqrt(target) )

        for i in range( 2,dest+1 ):
            if target % i == 0:
                print( str(target) + 'は素数ではない。')
                return
        print( str(target) + 'は素数である。')

    sosu( number )    

    #print( "メルセンヌ数：", bmelsen, int( bmelsen, base=2 ), end=" " )
    #print( "完全数の候補：", bcomp, int( bcomp, base=2) )
    print( "メルセンヌ数", int( bmelsen, base=2 ), "完全数の候補：", int( bcomp, base=2))