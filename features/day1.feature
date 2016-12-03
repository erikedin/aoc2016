Feature: Walking in a city
    In order to find all 50 stars for Santa, I need to find
    the Easter Bunny Headquarters in the city I was airdropped into.

    Background: Airdropped into the city
        Given that I have been airdropped into the city

    Scenario Outline: Turning
        Given that I am facing <Direction>
         When I turn <Turn>
         Then I should be facing <New direction>
    
      Examples: Turning right
        | Direction | Turn  | New direction |
        | N         | R     | E             |
        | E         | R     | S             |
        | S         | R     | W             |
        | W         | R     | N             |

      Examples: Turning left
        | Direction | Turn  | New direction |
        | N         | L     | W             |
        | E         | L     | N             |
        | S         | L     | E             |
        | W         | L     | S             |

    Scenario Outline: Walking
        Given that I am at <From E> blocks E and <From N> blocks N
          And that I am facing <Direction>
         When I walk <Distance> blocks
         Then I should be at <New E> blocks E and <New N> blocks N
      
      Examples: Walking different directions
        | From E | From N | Direction | Distance | New E | New N |
        | 0      | 0      | E         | 2        |  2    | 0     |
        | 2      | 0      | N         | 3        |  2    | 3     |
        | 2      | 3      | W         | 7        | -5    | 3     |
        | -5     | 3      | S         | 1        | -5    | 2     |

    
    Scenario: Following instructions, example 1
        Given that I am at 0 blocks E and 0 blocks N
          And that I am facing N
         When I follow the instructions "R2, L3"
         Then I should be at 2 blocks E and 3 blocks N
          And the distance should be 5
    
    Scenario: Following instructions, example 2
        Given that I am at 0 blocks E and 0 blocks N
          And that I am facing N
         When I follow the instructions "R2, R2, R2"
         Then I should be at 0 blocks E and -2 blocks N
          And the distance should be 2

    Scenario: Following instructions, example 3
        Given that I am at 0 blocks E and 0 blocks N
          And that I am facing N
         When I follow the instructions "R5, L5, R5, R3"
         Then the distance should be 12

    Scenario: Default position and direction
        Then I should be at 0 blocks E and 0 blocks N
         And I should be facing N
    
    Scenario: Reading instructions
        When I read the instructions "R2, L50"
        Then I should get the turns and distances:
            | Turn  | Distance |
            | R     | 2        |
            | L     | 50       |
    
    Scenario Outline: Taxi distance
        Given that I am at <E> blocks E and <N> blocks N
         Then the distance should be <Distance>

      Examples: Blocks and what their distances are from origin
        | E  | N | Distance |
        |  0 | 0 | 0        |
        |  2 | 3 | 5        |
        | -2 | 3 | 5        |
