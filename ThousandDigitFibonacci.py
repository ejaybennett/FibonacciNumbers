from decimal import *
'''1186721674525829159676708848596666927379858210009575892764858661997593068776409502596821517739657069326570396243812569971194105956254519426607596181188369313476221637121831119600442412
3489176045121333888565534924242378605373120526670329845322631737678903926970677861161240351447136066048164999599442542656514905088616976279305745609791746515632977790194938965236778055329
9673260385443562097458568551590589334764162587692643983738625841070119867818916566522943543033842426724086237903319639654571961742285743148209770145490616413074511017741667369402185941683
3725171051313818308623782752439317724601180095341499467031519769641945576898869297370019337267823602316664588646031135637635555916528437429566167604774250301635870834813744525426464475933
47480272900439663908918437444078457696202601209186612642494985683994167
52809338209739872047617689422485537053988895817801983866648336679027270843804302586168051835624516823216354234081479331553304809262608491851078404280454207286577699580222132259241827433'''

#Before I continue, I want to note that I know that the stupid way of doing
#this works. Here's the code for it:
a0 = 0
a1 = 1
while(len(str(a1))<=1000):
    temp = a0
    a0 = a1
    a1= temp+a1
print("Easy way generated answer: " + str(a1))
print("Easy way digits: "+ str(len(str(a1))))

#That felt underwhelming though, so here's the mathy way of doing it.
#From the recurrence relation a(n) = a(n-1) + a(n-2), we can get the
#characteristic polynomial of r^n - r^(n-1) - r(n-2), whose solutions are
#r1=(1+sqrt(5))/2=~1.618 and r2 = (1-sqrt(5))/2 =~ -0.618
getcontext().prec = 1500
r1 = (Decimal(1) + Decimal(5)**Decimal(.5))/Decimal(2)
r2 = (Decimal(1) - Decimal(5)**Decimal(.5))/Decimal(2)

#Now, we know that the nth term of the fibonacci sequence is equal to
#a*r1^n + b*r2^n for some a and b. We can find these a and b by using the
#initial conditions for the fibonacci sequence, a(0) = 0 and a(1) = 1
#to find that 0 = a*r1^0 +b*r1^0 and 1=a*r1^1 +b*r2^1, so a=1/sqrt(5)
#and b=-a=-1/sqrt(5)
a = Decimal(1) / Decimal(5)**Decimal(.5)
b = -a

#The second term in a*r1^n + b*r2^n is very small for large numbers of n,
#so we can safely ignore it for now. The first fibocci term with 1001 digits
#is the first value greater than 10^1000, so we can use the equality
#n = ln(10^1000 /a)/ln(r1) to find the digit
n = ((Decimal(10**1000)/a).ln() )/r1.ln()

#Now we simply need to round n up
n = n.quantize(Decimal('1.'), rounding=ROUND_UP)

#And use the equation above to find our number
thousandOneDigitFibonacci = a*r1**n + b*r2**n

#And round
thousandOneDigitFibonacci = thousandOneDigitFibonacci.quantize(Decimal('1.'), rounding=ROUND_HALF_DOWN)

print("Mathy way generated answer: " + str(thousandOneDigitFibonacci))
print("Mathy way digits: "+ str(len(str(thousandOneDigitFibonacci))))

