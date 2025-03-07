from sage.all import *
from sage.combinat.diagram import RotheDiagram
import numpy as np

# Import SageMath modules
n = 8

# hyperparameter for general KL variety or specifically Matrix Space
general = True


# get all permutations of n which avoid the pattern 321
avoiding = Permutations(n,avoiding=[Permutation([3,2,1])])
# work over a polynomial ring in n^2 variables
R = PolynomialRing(QQ, (n/2)**2, 'x', order = 'degrevlex')
T = PolynomialRing(QQ, (n/2), 't', order = 'degrevlex')




x = R.gens()
t = T.gens()

# let w and v be permutations, w < v
# wfixed = Permutation([1,2,3,4,5,6])
# vfixed = Permutation([4,5,6,1,2,3])

wfixed = Permutation([1,2,3,4,5,6,7,8])
vfixed = Permutation([5,6,7,8,1,2,3,4])

# wfixed = Permutation([1,2,3,4,5,6,7,8,9,10])
# vfixed = Permutation([6,7,8,9,10,1,2,3,4,5])

Tindices = []

allperms = Permutations(n)

# def bruhat-organize(n):




#w,v are Permutations
def space(v, w):
    #fix coordinates globally
    vfixed = v
    wfixed = w
    E = RotheDiagram(vfixed)
    count = 0
    V = vfixed.to_matrix()
    V = Matrix(R, V).transpose()
    for (i, j) in E:
        V[i, j] = x[count]
        count += 1
        Tindices.append((i, j))
    def rankconditions(w):
        # to matrix
        W = w.to_matrix()
        # W to polynomial matrices
        W = Matrix(R, W).transpose()
    
        # print("Coordinates correspondg to v")
        # print(V)
        # Rothe diagram
        D = RotheDiagram(w)
    
        # print("\n")
        # print("Rothe diagram of w " )
        # D.pp()
        totalminors = []
        for i in range(len(D)):
            #check if there are no boxes in D to the direct right or below (i, j)
            (i, j) = D[i]
            if (i+1, j) not in D and (i, j+1) not in D:    
                # then this box imposes rank conditions on the matrix V
                # in particular, count the number of 1s in the submatrix of w (1,1) to (i,j), call that k
                # we impose the condition that every k+1 by k+1 minor of the (1,1) to (i,j) submatrix of V is zero
                Vsubmatrix = V[0:i+1, 0:j+1]
                count = 0
                for a in range (0, i+1):
                    for b in range (0, j+1):
                        if W[a, b] == 1:
                            count += 1
                minors = Vsubmatrix.minors(count+1)
                for minor in minors:
                    totalminors.append(minor)
        
        J = R.ideal(totalminors)
        return J, totalminors
    
    # Open a file to write the output
    with open('/Users/songye03/Desktop/writing-fall2024/output.txt', 'w') as f:

        #global staticstics what we want to keep track of


        #print
        print("wfixed " + str(wfixed))
        f.write("wfixed " + str(wfixed) + "\n")

        print("avoids 321:" + str(wfixed in avoiding))
        f.write("avoids 321:" + str(wfixed in avoiding) + "\n")
        
        print("vfixed " + str(vfixed))
        f.write("vfixed " + str(vfixed) + "\n")
        
        print("\n")
        f.write("\n")
        
        #print the coordinates on V
        print("Coordinates corresponding to v")
        f.write("Coordinates corresponding to v\n")
        
        print(V)
        f.write(str(V) + "\n")
        
        print("\n")
        f.write("\n")
        
        print("Diagram of w")
        f.write("Diagram of w\n")
        
        D = RotheDiagram(wfixed)
        D.pp()
        f.write(str(D) + "\n")
        
        # create a list of all permutations of n 
        perms = []
        
        if general:
            perms = Permutations(n)
        if not general:
            temp = Permutations(int(n/2))
            for perm in temp:
                l = [perm[i] for i in range(int(n/2))]
                m = l + [int(n/2) + i + 1 for i in range(int(n/2))]
                perms.append(Permutation(m))
        #loop over perms (this is to get the stratification)
        #l = bruhat length of vfixed
        
        l = vfixed.length()
        # sort perms by bruhat order
        perms = sorted(perms, key = lambda x: x.length())
        # reverse
        perms = perms[::-1]
        grobnerlengths = {}

        for pi in perms:
            if pi.bruhat_lequal(vfixed) and wfixed.bruhat_lequal(pi):
                print(pi)
                f.write(str(pi) + "\n")
                
                print("dimension " + str(l - pi.length()))
                f.write("dimension " + str(l - pi.length()) + "\n")

                print("avoids 321:" + str(pi in avoiding))
                f.write("avoids 321:" + str(pi in avoiding) + "\n")
                

                J,totalminors = rankconditions(pi)

                #print a Groebner basis of the ideal
                groebner_basis = J.groebner_basis()
                grobnerlengths[pi] = len(groebner_basis)

                #for all the permutations which cover pi in the Bruhat order
                # check if the Groebner basis is size 1 more than the Groebner basis of pi
                covers = pi.bruhat_succ()

                for cover in covers:
                    if cover.bruhat_lequal(vfixed):
                        print("covered by " + str(cover))
                        f.write("covered by " + str(cover) + "\n")
                        if grobnerlengths[cover] != len(groebner_basis) + 1:
                            print("Groebner basis length WRONG by difference " + str(len(groebner_basis) - grobnerlengths[cover]))
                            f.write("Groebner basis length WRONG by difference " + str(len(groebner_basis) - grobnerlengths[cover]) + "\n")
                        else:
                            print("Groebner basis length RIGHT")
                            f.write("Groebner basis length RIGHT \n")

                            

                print("Groebner basis")
                f.write("Groebner basis\n")
                for g in groebner_basis:
                    #get the leading term and calculate its weight
                    #print it and write it to the file
                    lt = g.lm()
                    #exponent vector
                    # exp = lt.exponents()


                    # print(exp)
                    # f.write(str(exp) + "\n")

                    #evaluate at xi = t_it_j^{-1} where i is the row and j is the column in which xi is located
                    #this is the weight of the leading term
                    a = lt.subs({x[i]: t[Tindices[i][0]]/t[Tindices[i][1]] for i in range(len(Tindices))})
                    # convert a to exponent vector of integers, maybe negative
                    num = a.numerator()
                    den = a.denominator()

                    # if num is not a constant

                    if num.is_constant() == False:
                        numtup = num.exponents()
                        dentup = den.exponents()


                        #to numpy
                        tup = np.subtract(numtup, dentup)

                        print(g, str(tup[0]))
                        f.write(str(g) + " " + str(tup[0]) + "\n")
                    else:
                        print(g, str(num))
                        f.write(str(g) + " " + str(num) + "\n")


                print("\n")
                f.write("\n")

space(vfixed, wfixed)