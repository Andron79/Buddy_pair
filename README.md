 Тестовое задание


Buddy pairs
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"


// the return is `nil` if there is no buddy pair
func Buddy(start, limit int) []int {
  // your code

* На русском

Пары приятелей
Вы знаете, что такое делители числа. Делители положительного целого числа n считаются правильными, когда вы рассматриваете только делители, отличные от самого n. В следующем описании делители будут означать правильные делители. Например за 100 они стоят 1, 2, 4, 5, 10, 20, 25, и 50.

Пусть s (n) - сумма этих собственных делителей n. назовем два положительных целых числа такими, что сумма собственных делителей каждого числа на единицу больше другого числа:

(n, m) - пара приятелей, если s (m) = n + 1 и s (n) = m + 1

Например, 48 и 75 - это такая пара:

Делители 48 являются: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> сумма: 76 = 75 + 1
Делители 75 являются: 1, 3, 5, 15, 25 --> сумма: 49 = 48 + 1
* Задача

Учитывая два положительных целых числа start и limit, функция buddy (start, limit) должна возвращать первую пару (n m) пар buddy, таких что n (положительное целое число) находится между start (inclusive) и limit (inclusive); m может быть больше предела и должно быть больше n

Если нет пары приятелей, удовлетворяющей этим условиям, то верните "ничего" или (для Go lang) ноль
