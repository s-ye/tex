loadPackage "NormalToricVarieties"

M = matrix{}


-- Define the columns you want to add
columns = {
    {1,0,0,0,0,0,1,0,0,0,0,0,1},
    {1,0,0,0,0,0,1,0,0,1,0,0,1},
    {1,0,0,0,0,0,1,0,0,1,0,1,1},

    {1,0,0,0,1,0,1,0,0,0,0,0,1},
    {1,0,0,0,1,0,1,0,0,1,0,0,1},
    {1,0,0,0,1,0,1,0,0,1,0,1,1},

    {1,0,0,1,1,0,1,0,0,0,0,0,1},
    {1,0,0,1,1,0,1,0,0,1,0,0,1},
    {1,0,0,1,1,0,1,0,0,1,0,1,1},

    {1,1,0,1,1,1,1,1,0,1,1,1,1},
    {1,1,0,1,1,1,1,1,0,1,0,1,1},
    {1,1,0,1,1,1,1,1,0,1,0,0,1},

    {1,1,0,1,1,0,1,1,0,1,1,1,1},
    {1,1,0,1,1,0,1,1,0,1,0,1,1},
    {1,1,0,1,1,0,1,1,0,1,0,0,1},

    {1,1,0,0,1,0,1,1,0,1,1,1,1},
    {1,1,0,0,1,0,1,1,0,1,0,1,1},
    {1,1,0,0,1,0,1,1,0,1,0,0,1},
    
    {1,-1,0,0,0,0,0,0,0,0,0,0,1},
    {1,0,-1,0,0,0,0,0,0,0,0,0,1}
};

columns = {
    {1,0,0,0,0,0,1,0,0,0,0,0,1},
    {1,0,0,0,0,0,1,0,0,1,0,0,1},
    {1,0,0,0,0,0,1,0,0,1,0,1,1},

    {1,0,0,0,1,0,1,0,0,0,0,0,1},
    {1,0,0,0,1,0,1,0,0,1,0,0,1},
    {1,0,0,0,1,0,1,0,0,1,0,1,1},

    {1,0,0,1,1,0,1,0,0,0,0,0,1},
    {1,0,0,1,1,0,1,0,0,1,0,0,1},
    {1,0,0,1,1,0,1,0,0,1,0,1,1},

    {1,1,0,1,1,1,1,1,0,1,1,1,1},
    {1,1,0,1,1,1,1,1,0,1,0,1,1},
    {1,1,0,1,1,1,1,1,0,1,0,0,1},

    {1,1,0,1,1,0,1,1,0,1,1,1,1},
    {1,1,0,1,1,0,1,1,0,1,0,1,1},
    {1,1,0,1,1,0,1,1,0,1,0,0,1},

    {1,1,0,0,1,0,1,1,0,1,1,1,1},
    {1,1,0,0,1,0,1,1,0,1,0,1,1},
    {1,1,0,0,1,0,1,1,0,1,0,0,1}
};

-- Loop through each column and add it to the matrix
for i from 0 to #columns-1 do (
    columnVector = transpose matrix {columns#i};
    if i == 0 then
        M = columnVector
    else
        M = M | columnVector;
);

-- Display the matrix
M
gens ker M
rank M

-- Create a polynomial ring with variables for each column
n = numColumns M;
print n
R = QQ[x_0..x_(n-1)]

-- Create the binomial ideal from the kernel of M
kernelM = gens ker M;

binomialIdeal = ideal apply(numColumns kernelM, i -> (
    -- Extract the coefficients of the i-th kernel generator (column)
    coeffs = flatten entries transpose kernelM_{i};
    print coeffs;
    
    -- Separate positive and negative coefficients
    posTerms = 1_R;
    negTerms = 1_R;
    
    for j from 0 to #coeffs-1 do (
        c = coeffs#j;
        if c > 0 then
            posTerms = posTerms * (x_j)^c
        else if c < 0 then
            negTerms = negTerms * (x_j)^(-c)
    );
    
    -- Create the binomial for this kernel generator
    posTerms - negTerms
));

-- Print the generators of the ideal one per line
print "Generators of the binomial ideal:";
scan(numgens binomialIdeal, i -> (
    g := binomialIdeal_i;
    print toString g;
));

X = Proj(R/binomialIdeal)
degree X
dim X