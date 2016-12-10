Feature: Find the bathroom code
 In order to use the bathroom
 As an agent of Santa
 I want figure out the keycode
 So that I don't pee myself

 Background: I am at a keypad
    Given I am at a keypad like
      """
        1  
       234 
      56789
       ABC 
        D  
      """

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
   Then I should get the bathroom code 5DB3
  
 Scenario: Stay if you can't move a direction
  Given I start at key 5
   When I follow the keypad instructions
    """
    ULL
    """
   Then I should be at 5
  
 Scenario Outline: Moving on the keypad
  Given I start at key <Start at>
   When I move according to instruction <Instruction>
   Then I should be at <New key>
  
  Examples: Movement on the keypad
   | Start at | Instruction | New key |
   | 1        | U           | 1       |
   | 1        | D           | 3       |
   | 1        | L           | 1       |
   | 1        | R           | 1       |
   | 5        | U           | 5       |
   | 5        | D           | 5       |
   | 5        | L           | 5       |
   | 5        | R           | 6       |
   | 7        | U           | 3       |
   | 7        | D           | B       |
   | 7        | L           | 6       |
   | 7        | R           | 8       |
   

  