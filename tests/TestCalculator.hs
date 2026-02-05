module TestCalculator where

import Calculator
import Test.HUnit

-- Test suite for add function
testAdd :: Test
testAdd = TestList
  [ TestCase $ assertEqual "add 2 + 3" 5 (add 2 3)
  , TestCase $ assertEqual "add (-1) + 1" 0 (add (-1) 1)
  ]

-- Test suite for subtract function
testSubtract :: Test
testSubtract = TestList
  [ TestCase $ assertEqual "subtract 5 - 3" 2 (subtract 5 3)
  , TestCase $ assertEqual "subtract 0 - 5" (-5) (subtract 0 5)
  ]

-- Test suite for multiply function
testMultiply :: Test
testMultiply = TestList
  [ TestCase $ assertEqual "multiply 2 * 3" 6 (multiply 2 3)
  , TestCase $ assertEqual "multiply (-1) * 4" (-4) (multiply (-1) 4)
  , TestCase $ assertEqual "multiply 0 * 5" 0 (multiply 0 5)
  ]

-- Main function to run all tests
main :: IO ()
main = runTestTT (TestList [testAdd, testSubtract, testMultiply])