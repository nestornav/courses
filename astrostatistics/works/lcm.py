def linear_congruence(iteration,seed,a,c,m):
    random_values = []
    for it in xrange(iteration):
        pass_increment = (a * seed + c) % m
        seed = pass_increment
        random_values.append(pass_increment)        
    return random_values

if __name__  == '__main__':
    print linear_congruence(10,0,4,1,9);
