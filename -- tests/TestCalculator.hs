module TestCalculator where

import Calculator

-- Assuming a simple testing approach; in practice, use a testing library like HUnit
testAdd :: Bool
testAdd = (add 2 3 == 5) && (add (-1) 1 == 0)

testSubtract :: Bool
testSubtract = (subtract 5 3 == 2) && (subtract 0 5 == (-5))

testMultiply :: Bool
testMultiply = (multiply 2 3 == 6) && (multiply (-1) 4 == (-4)) && (multiply 0 5 == 0)

-- To run tests, you might define a main function or use a testing framework