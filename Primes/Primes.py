class Primes(object):
    def count_primes(num):
        """
        takes num and finds all primes lower or equal to it
        """
        primeSet = [2]
        for i in range(num): 
            if i >2:   # 2 until ==num
    
                is_new_prime = True
                for x in primeSet:
                    if i%x==0: # until x == i(iteratingNumber)
                        is_new_prime = False
                if is_new_prime == True:
    
                    primeSet.append(i)
        primes = list(set(primeSet))
        primes.sort()
        print(primes)
        return len(primes)
    
    def next_prime(num):
        """
        iterates through a range starting at num and ending at num*2, 
        tries to find any multiple of current_number and sets is_new_prime to True
        after current_number is iterated through / hits a break it will check for print the prime found and break out of the last loop
        """
        is_new_prime= False
        for current_number in range(num, num*2):  # next prime has to be between num and num*2
            is_new_prime = True
            for number in range(2, current_number -1): ## is_new_prime set to False if number can be divided within this loop
                if current_number % number == 0 : 
                    is_new_prime= False
                    break;
            if is_new_prime == True:
                print(f"{current_number} is the next prime after {num}")
                return current_number
        

    def factoral_finder(num:int):
        """takes num and finds the factoral of it"""
        from math import factorial
        answer = factorial(num)
        print(answer)
        return answer
        


Primes.count_primes(15)
Primes.next_prime(15)
Primes.factoral_finder(5)
