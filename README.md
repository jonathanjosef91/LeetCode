# LeetCode

This repo contains python solutions for [Leet Code](https://leetcode.com/) problems 

You can find problems classified by two methods
1. Lexicographic order - Folder arranged in a lexicographic order by the same name you'll find in LeetCode.
2. Tags - Each problem will be tagged by one or more tags. Tags will be given based on the materials and technics needed for that specific solution, and based on the question level.


## Tags
### Materials based tags
Math - Problems that relay mostly on dynamic programming technics

DP - Problems that relay mostly on dynamic programming technics

Strings - Problems that requires modifications and understanding of strings

Searches - Including all kind of search algorithms 

Old - Problems that I solved in early stages of my career. 
The Solutions you'll find there are valid but can be lack of style, tests, and tagged poorly.

### Difficulty based tags
Beginners - Good place to start from. Not likely to be asked during an interview

Medium - Most of the interview questions fall under this bucket. You want to reach the level where you can come up with a solution in 5-15 minutes, and code it in another 5-15 minutes.

Hard - Very challenging problems. Can be asked during job interviews, but most likely, you're not expected to solve them completely. 

Extreme - Just for fun. Don't feel bad if you haven't solved them. Most of the interviewers can't solve them either.

### Mapping Problems by Tags:

You can find in `ProblemsByTags.json` a problem mapping by tags.
Running the `ProblemsByTags.py` will regenerate the json file.


## Write a solution
Create a new branch `git checkout -b <yourUserName>/<theProblemName>` 

For example : `git checkout -b jjosef/isPEqualNP`

Run `python newSolution.py myProblem`. 
The script will create a new template file under the right folder hierarchy and will print its location.

Please make sure to replace everything need to be replaced.

Add a few test cases, make sure they're running smoothly.

Run `build.ps1`.
If everything is OK, push it and open a PR.

## Troubleshooting
Found something wrong? Something that can be optimized? Feel free to [open an issue](https://github.com/jonathanjosef91/LeetCode/issues). *please make sure the issue doesn't already exist* 