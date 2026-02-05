module TestCalculator where

import Calculator
import Test.HUnit

testAdd :: Test
testAdd = TestCase $ do
    assertEqual "add 2 + 3" 5 (add 2 3)
    assertEqual "add (-1) + 1" 0 (add (-1) 1)

testSubtract :: Test
testSubtract = TestCase $ do
    assertEqual "subtract 5 - 3" 2 (subtract 5 3)
    assertEqual "subtract 0 - 5" (-5) (subtract 0 5)

testMultiply :: Test
testMultiply = TestCase $ do
    assertEqual "multiply 2 * 3" 6 (multiply 2 3)
    assertEqual "multiply (-1) * 4" (-4) (multiply (-1) 4)
    assertEqual "multiply 0 * 5" 0 (multiply 0 5)

tests :: Test
tests = TestList [TestLabel "testAdd" testAdd, TestLabel "testSubtract" testSubtract, TestLabel "testMultiply" testMultiply]

main :: IO ()
main = runTestTT tests