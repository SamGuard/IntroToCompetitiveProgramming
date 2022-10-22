# Hello World
Hi and welcome to intro to competitive programming. This is a series of tutorials to help you get into the groove of things.
This will not teach any fancy algorithms really, it is mostly to give you a base to build more knowledge off (if you want to). 

This tutorial will be done mostly in Python as (with only a few exceptions) all problems are solveable in Python. We will leave writing solutions in C to the perfectionists who want to get the fastest time they can, this is not what we are here for.

All problems will be from open.kattis.com as this is what im familiar with, but the information here would be almost entirely the same if HackerRank was used.

Solutions to any problem mentioned can be found in the solutions folder. Each problem will be given a reference number [x], each file will be named with their reference number and the problem name.

## Section 1: Problems
Who doesn't love to solve problems? This section will outline how problems work in competitive programming generally. The different types of problems and common methods used to solve them will not be discussed here as it is a massive topic. This will be about just reading and understanding the questions.

Problems are generally split into three categories:
1. Problem outline
2. Input
3. Output
4. Sample Inputs/Outputs

The problem outline is used to set the scene and define what the problem is about. Some problems on Kattis just use this section (incorrectly) as a place to put flavour text to make the problem more fun but the vast majority uses this section to discuss the core of problem. This section is the most important and its very important you understand what it is trying to get at.

The second section, Input, defines what variables are given and in what ranges they will be in, **pay attention to the ranges**. These ranges are a key part of the question, it can decide how you approach a problem. If a range is defined with small numbers, it is likely a solution can be found in a quicker, dirtier way. For example, this can be the difference between brute forcing the solution and finding a more elegant solution. As you do more problems you will gain a sense of what problems can be brute forced and what can not. Part of solving a problem is not letting your program exceed the time limit (more on this later).

Outputs are usually the simplest section, telling you what information to output and in what format. More on this in the Input and Output section.

Finally, the Sample Input/Output sections are used to demonstrate what a correct solution. **These test inputs will not cover all possible inputs**. The sample inputs are often a tiny subsection of what your code will actually be tested on, making it harder for you to know if your code is correct and if not, why its not correct. Thats up to you as the programmer to figure out on your own (methods on this laters).



## Section 2: Input and Output
For every problem you are going to have to take some form of input and print an output. So below we are going to dedicate this section with how it works and best practices.
### Input
There is roughly three ways that input is done for problems:
1. The input length is given in the input or in the problem text
2. There is a word/number that means stop (often a 0, -1 or end)
3. An End of File character

The first method is the most common, and is simple to handle. An example of this can be seen in this problem: [aboveaverage](https://open.kattis.com/problems/aboveaverage)[0]. In the input section it says "*The first line of standard input contains an integer 1 <= **C** <= 50, the number of test cases*". In this problem, a test case refers to a single line of input. So we know there will be 50 lines after this. This means we can put are code in a simple for loop, that will loop **C** times. Next in the input description, it tells us what each line constists of: "*Each data set begins with an integer, **N**, the number of people in the class (1 <= N <= 1000)*". This now tells us on every line there will be N number of values. If you look at the sample inputs
