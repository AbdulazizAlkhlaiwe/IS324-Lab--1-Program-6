n=int(input('Enter a number: '))

if n > 1:
    prime= True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break;

if prime:
    factorial =1
    for i in range(2,n+1):
        factorial = factorial * i
    print(n, ' is Prime.')
    print('its factorial : ', factorial  )

else:
    print(n, 'Not a prime number.')