
Recall
\[\sin(x) = opp/hyp\]
\[\cos(x) = adj/hyp\]
\[\tan(x) = opp/adj = \sin(x)/\cos(x)\]

Unit Circle

- measured in radians
- best way to remember radians to degrees: 360 degrees = 2$\pi$ radians = 1 circle (2$\pi$ is the number in the formula for the circumference)
\[1 \text{ radians} = 180/\pi \text{ degrees} \]
- On the unit circle, you have to remember the sin, cos, tan, of the angles 30, 45, 60 ($\pi/6, \pi/4, \pi/3$)
- You have to remember the special right triangles 30, 60, 90 and 45-45-90
- $\sin(45) = 1/\sqrt{2} = \sqrt{2}/2$
- $\cos(45) = 1/\sqrt{2} = \sqrt{2}/2$
- $\tan(45) = 1$ because sin and cos are the same
- $\sin(30) = 1/2$ and $\cos(30) = \sqrt{3}/2$
- the way to remember which one is which is you just think about which side is longer

Trig properties:
- Pythagorean theorem \[a^2 + b^2 = c^2\]
\[adj^2 + opp^2 = hyp^2\]
- If you divide by $c^2$ you get \[\sin(x)^2 + \cos(x)^2 = 1\]
- If you divide by $adj^2$ you get \[
    1 + \tan^2(x) = \sec^2(x)
    \]
- If you divide by $opp^2$ you get \[
    \cot^2(x) + 1 = \csc^2(x)
    \]

Sum formula 
\[
    \sin(a+b) = \cos(a)\sin(b) + \sin(a)\cos(b)
    \]

\[
    \cos(a+b) = \cos(a)\cos(b) - \sin(a)\sin(b)
    \]

If you $a=b$ you get the double angle formulas \[
 \sin(2a) = 2\cos(a)\sin(a)   
\]    
\[
    \cos(2a) = \cos^2(a) - \sin^2(a) = 1 - 2\sin^2(a) = 2\cos^2(a) - 1
    \]

$\sin(2x) + \cos(x) = 0$

We need get rid of the double angle:

\[
    2\cos(x)\sin(x) + \cos(x) = 0
    \]

Factor 

\[
        \cos(x) (2\sin(x) + 1) = 0
        \]

So either $\cos(x)$ = 0 or $2\sin(x) + 1 = 0$. If $\cos(x) = 0$ then $x = \pi/2, -\pi/2$ plus all the periods of those two guys.
If $2\sin(x) + 1 = 0$ then $\sin(x) = -1/2$. So that means $x = -\pi/6, 7\pi/6$.

Anytime you solve $\sin(x) = $ something or $\cos(x) = $ something always has two answers, then plus the period $2\pi$.

Answer $\pi/2, 3\pi/2, -\pi/6 + 2\pi = 11\pi/6, 7\pi/6$

Solve $3\sin(x) = 1 + \cos(2x)$. Use double angle formula for $\cos(2x)$:
\[
    3\sin(x) = 1 + \cos^2(x) - \sin^2(x)
    \]

Use Pythagoras, plug in $\cos^2(x) = 1 - \sin^2(x)$. We want everything in terms of $\sin$. Get rid of the cosine.

\[
    3\sin(x) = 2 - 2\sin^2(x)
        \]

Bring everything over to one side: 

\[ 2\sin^2(x) + 3\sin(x) - 2 = 0
    \]

Factor it:

\[
    2u^2 + 3u - 2 = 0
    \]

$u = (-3 \pm \sqrt{3^2 - 4(2)(-2)})/4$ so $u = (-3 \pm \sqrt{25})/4$ so $u = -2$ or $u = 1/2$

$\sin(x) = -2$ or $\sin(x) = 1/2$. So $x = \pi/6, 5\pi/6$ for $\sin(x) = 1/2$. For the other one, there are no solutions. $\sin, \cos$ are always between negative one and one.


$\sin(x)\cos(2x) + \sin(2x)\cos(x) = 1/2$. Solve for $x$. Use the sum formula to combine the left hand side.

The left hand side becomes \[
    \sin(x)\cos(2x) + \sin(2x)\cos(x) = \sin(3x)
    \]
    So the equation is
\[
    \sin(3x) = 1/2
    \]

Let $u = 3x$ then $\sin(u) = 1/2$. So that means $u = \pi/6$ or $5\pi/6$. So $x = \pi/18 $ or $5\pi/18$.

What if $u = \pi/6 + 2\pi$. Then $u = 13\pi/6$ and $x = 13\pi/18$ which is between $0$ and $2\pi$.
What if $u = \pi/6 + 4\pi$. Then $u = 25\pi/6$ so $x = 25\pi/18$ and thats another solution.

$u = 5\pi/6 + 2\pi, 5\pi/6 + 4\pi$ and then dividing by $3$, gives $x = 17\pi/18, 29\pi/18$.

$\sin(u)$ has period 2$\pi$ in the variable $u$ but $\sin(3x)$ has period $2\pi/3$ in the variable $x$.

In total, the equation $\sin(3x) = 1/2$ has six solutions between $0$ and $2\pi$. The reason for this is because the periods got shorter. 
If the equation looks like $\sin(nx) = c$ then there will be $2n$ solutions between zero and $2\pi$. If $n=1$ then there are two solutions. The same thing for $\cos$.

$4\sin(x)\cos(x) = \cos^2(x) + \sin^2(x)$

On the right we get $1$. On the left, we use $\sin$ double angle, get $2\sin(2x)$.

So \[2\sin(2x) = 1
    \]

\[\sin(2x) = 1/2\]

$u = 2x$, then $\sin(u) = 1/2$ so $u = \pi/6, 5\pi/6, 13\pi/6, 17\pi/6$ and then dividing by $2$ gives $x = \pi/12, 5\pi/12, 13\pi/12, 17\pi/12$. So there are 4 answers for $x$.