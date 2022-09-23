# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:34:17 2022

@author: Trent
"""

import random
import math

MIN_PRIME_NUMBER = 1_000_000
MAX_PRIME_NUMBER = 10_000_000
prime_candidates = set()

def FermatPrimalityTest(n):
    # Arbitrairly test 20 values within range to verify primality
    for test in range(1, 20):
        test = random.randint(MIN_PRIME_NUMBER + 1, MAX_PRIME_NUMBER - 1)
        
        if pow(test, n-1, n) != 1:
            return False
        else:
            prime_candidates.add(n)
            return True
    # Pass Fermat test if all 20 tests pass

class User:
    
    def __init__(self):
        tmp_p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        tmp_q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        
        # If p_val is not prime, generate another p_val
        while not FermatPrimalityTest(tmp_p_val):
            tmp_p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
            
        # If q_val is not prime, generate another q_val
        while not FermatPrimalityTest(tmp_q_val):
            tmp_q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        
        n = tmp_p_val * tmp_q_val
        tmp_phi = (tmp_p_val - 1) * (tmp_q_val - 1)
        e = random.randint(1, tmp_phi + 1)
        
        # Generate random e (public key) using Euclid's algorithm until its relatively prime to phi
        while not math.gcd(e, tmp_phi) == 1: 
            e = random.randint(1, tmp_phi + 1)
        
        self.public_key = e
        self.length = n
        self.phi = tmp_phi
            
class Public(User):
    def __init__(self):
        super().__init__()
        
    def encrypt(self, message, e, n):
        upper_msg = message.upper()
        char_to_ascii = [ord(x) for x in upper_msg]
        # Encrypt each ASCII code using Fast Modular Exponentiation with Public Key
        encryptedM = [pow(m,e,n) for m in char_to_ascii]
        
        self.encrypted_msg = encryptedM
        print("Encrypted Message: " + str(self.encrypted_msg))
        return encryptedM

class Private(User):
    def __init__(self):
        super().__init__()
        self.d = math.gcd(self.public_key, self.phi)
        
    def decrypt(self, e_msg,d,n):
        finish = ''
        # Decrypt using Fast Modular Exponentiation
        char_to_ascii = [pow(c,d,n) for c in e_msg]
        # Map ASCII code-> char
        d_msg = [chr(x) for x in char_to_ascii]
        for x in d_msg:
            finish += x
            
        return finish
    
        (x, y, d) = math.gcd(math.gcd.b, math.gcd.a%math.gcd.b)
        return y, x - math.gcd.a//math.gcd.b*y, d
