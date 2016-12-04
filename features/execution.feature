Feature: Executing the puzzle for each day
 In order to solve the puzzle each day
 As a developer
 I want to run each puzzle with ease and consistency
 So that I don't have to work a bunch of unnecessary code

 Scenario: Solving the puzzles for day 1
  Given I have solved both puzzles for day 1
   When I execute the script for day 1
   Then I get the results for both puzzles
  
 Scenario: Solving the puzzle for only part 1
  Given I have solved only puzzle 1 for day 1
   When I execute the script for day 1
   Then I get only the result for puzzle 1
  
 Scenario: Reading input for a given day
    Given I want to solve the puzzle for day 1
     When I look for the module "day1"
     Then I can parse the input by sending in a list of lines