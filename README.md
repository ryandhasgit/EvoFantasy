## Overview
This project is the back-end code for a fantasy baseball optimization app using the Genetic algorithm machine learning technique. It is written in Python.

The application runs an interpreter which provides a user with prompts. It is intended to be used during a live draft. The prompts allow a user to choose players that have been drafted and should be excluded from the algorithm. Each time a player is removed, the algorithm re-runs.

Lineups are optimized for the five main offensive categories used in standard Rotisserie fantasy baseball leagues. Those categories are: batting average, runs, home runs, RBIs, and stolen bases.

## Theory

### The problem
Rotisserie (known as Roto) leagues partly rank players by their standing in each offensive category. For example, if your league has 12 players and your team has compiled the most home runs, you receive the equivalent of 12 points for the home run category. Your ranking in each of the four additional statistical categories assigns a score in the same way. The sum of these dictates your overall standing.

The problem this app solves is one that plagues fantasy baseball players ubiquitously: how do I draft players to address all five categories simultaneously? Rarely is one hitter dominant in all stats, and quickly are those lost who are. A concentration of players with various skillsets remains, requiring a careful balancing act to maintain parity. 

Drafting good players isn't enough to account for all five stats, and drafting bad players who specialize in one or two stats hamstrings your team in other categories. 

### The solution
EvoFantasy is modeled after the Traveling Salesman Problem (TSP), whereby a salesman has a list of places they wish to visit and seeks the optimum route. The permutation of possible routes increases factorially and quickly outpaces brute-force simulations. 5 stops yields 120 routes. 10 stops yields 3,628,800. 20 stops creates over 2 billion billion unique routes. By 100 stops, every super-computer in existence could work as long as the universe has existed and not make a dent. 

Solutions to the TSP can only be approximated at scale. One method of doing so—Genetic algorithm–assigns each stop a letter, sequenced like a genome. ABCD, BCDA, CDAB (etc) are all uniquely sequenced routes. A large, fixed number of routes are randomly generated, their distances evaluated, and only an efficient few are retained (e.g. the top 10%). The "fittest" remaining routes are randomly combined as would be produced by mating, with a 50% chance of two parents passing on their genes. This combination process (mating) recurs until the population is replenished to its previous size, and the process iterates until a local maximum is reached.

EvoFantasy treats each randomly generated fantasy baseball lineup as a unique genome and follows the same methodology. 

## Results
EvoFantasy is able to consistently produce lineups with exceptionally high-yielding rankings based on player stats. Since there are no known "perfect" lineups, quantification of this is anecdotal. But EvoFantasy consistently outperforms hand-chosen lineups and does so dynamically, during a live draft.
