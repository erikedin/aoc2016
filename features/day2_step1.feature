Feature: Find the bathroom code
 In order to use the bathroom
 As an agent of Santa
 I want figure out the keycode
 So that I don't pee myself

 Background: I am at a keypad
    Given I am at a keypad 

 Scenario: Starting key
   Then I should be at 5

 Scenario: Example keycode
  Given I start at key 5
   When I follow the keypad instructions
    """
    ULL
    RRDDD
    LURDL
    UUUUD
    """
   Then I should get the bathroom code 1985
  
 Scenario: Stay if you can't move a direction
  Given I start at key 5
   When I follow the keypad instructions
    """
    ULL
    """
   Then I should be at 1
  
 Scenario Outline: Moving on the keypad
  Given I start at key <Start at>
   When I move according to instruction <Instruction>
   Then I should be at <New key>
  
  Examples: Movement on the keypad
   | Start at | Instruction | New key |
   | 1        | U           | 1       |
   | 1        | D           | 4       |
   | 1        | L           | 1       |
   | 1        | R           | 2       |
   | 5        | U           | 2       |
   | 5        | D           | 8       |
   | 5        | L           | 4       |
   | 5        | R           | 6       |
   

  