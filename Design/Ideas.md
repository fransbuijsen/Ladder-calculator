# NBB Ladder calculator - design ideas file

## Introduction

This document describes general ideas about the design and functions of the NBB Ladder Calculator.

## Overview - what does it do

The idea for this application comes out of my work as game director for the Bridgeclub Bodegraven-Reeuwijk. In this club, each of the 4 (or 5) playing moments has a ladder competition that determines the player or pair that can call themselves Champion of the season. 
This is determined by scoring Ladder points every evening that you play. The pair with the best average score becomes overall champion.
These scores were calculated mostly manually, with the help of a specially developed MS Excel spreadsheet that converted the result of an evening into a set of scores for the Ladder. 

The Ladder Calculator application does all this automatically. The envisioned functionality is this:

 1. The user supplies the input -- this can be a URL with the overall scores on the NBB club site, or possible just the cliub name or number.
 2. The application then goes and absorbs all the results found on the club site.
 3. It then aggregates this into Ladder scores.
    - A personal Ladder score that calculates each player's Ladder scores
    - A Ladder for all registered pairs.
 4. The application then outputs the Ladder scoring, either to an Excel spreadsheet, or as a web page.

## Inputs

The following inputs will have to be given or generated in some way:

 1. The URL or name (or whatever designator) for where to get the results of games
 2. The list of how to convert ending positions into Ladder scores
 3. (possible) List of pairs and/or players
 4. (possible) Output format

## Plan

So far the plan is to look at the following things:

 1. Python programming
 2. Get python libraries for
    - Excel sheet read and write
    - Web site read and parse
    - Web site write
 3. Possibly, look at deployment into an Azure/Bluemix container
    - Web site input building
    - Web handling
   