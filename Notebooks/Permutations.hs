module Permutations where

fact n = foldl (*) 1 [2..n]

del k xs = [x | x <- xs, x /= k]

count p xs = length [x | x <- xs, p x]

--The number of the permutation in lexicographical order. Usage example: lexNumOfPerm [2, 4, 3, 1]
lexNumOfPerm [] = 1
lexNumOfPerm (x:xs) = lexNumOfPerm xs + count (< x) xs * fact (length xs)

lexPerm' k acc [] = acc
lexPerm' k acc xs = lexPerm' (k `mod` nf) (mark:acc)(del mark xs) where
     mark = xs !! (k `div` nf)
     nf = fact (length xs - 1)

--The k-th permutation in lexicographical order. Usage example: lexPerm 12 [1, 2, 3, 4]
lexPerm k = reverse . lexPerm' (k - 1) []

--The k-th permutation in lexicographical order. Usage example: revLexPerm 12 [1, 2, 3, 4]
revLexPerm k xs = lexPerm' (k - 1) [] (reverse xs)

fikePlaceVals n = foldl (\(x:xs) p -> p*x : x : xs) [1] [n, n - 1.. 3]

dSeq k n = reverse $ tail $ foldl (\(x:xs) p -> (mod x p) : (div x p) : xs) [k - 1] (fikePlaceVals n)

fikeSeq k n = zipWith (-) [1..n] (dSeq k $ n)

swap i j list | i == j = list
         | i < j = hs ++ (y:xs) ++ (x:ys)
         | otherwise = swap j i list where
   (hs, zs) = splitAt i list
   (x:xs, y:ys) = splitAt (j - i) zs

--The k-th permutation in Fike's order. Usage example: fikePerm 12 [1, 2, 3, 4]
fikePerm k marks = snd (foldl (\(i, p) j -> (i + 1, swap i j p)) (1, marks) $ fikeSeq k (length marks))

--Powerset of a set. Usage example: powerSet [1, 2, 3, 4]
powerSet [] = [[]];
powerSet (x:xs) = pXs ++ [x:ys | ys <- pXs] where pXs = powerSet xs

setFromBits _ 0 = []; setFromBits (x:xs) bits = if (bits `mod` 2 == 0) then setFromBits xs (bits `div` 2) else x : setFromBits xs (bits `div` 2)

--Powerset of a set using setFromBits
powerSet' set = map (setFromBits set) [0.. 2^n -1] where n = length set

--nCr
comb n r = product [n, n - 1 .. n - r + 1] `div` product [2..r]
