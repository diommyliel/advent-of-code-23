module Main where

import Distribution.ModuleName (main)
import Data.Char (isDigit, digitToInt)

fileName = "/home/diommy/Documents/dev/advent-of-code-23/1/input.txt"

main :: IO()
main = do
        content <- getInputTest fileName
        let input = lines content
        let ans1 = sum [calcDoubleDigit (filterNonDigit str) | str <- input]
        putStrLn ("The answer to part 1 is " ++ show ans1)


filterNonDigit :: String -> String
filterNonDigit = filter isDigit

getInputTest :: FilePath -> IO String
getInputTest file_name = do
    readFile file_name

calcDoubleDigit :: String -> Int
calcDoubleDigit str = digitToInt (head str ) * 10 + digitToInt (last str)
