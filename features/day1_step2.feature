Feature: Finding the Easter Bunny HQ at the first location I visit twice

    Background: Airdropped into the city
        Given that I have been airdropped into the city

    Scenario: The first location I visit twice
        Given that I am at 0 blocks E and 0 blocks N
          And that I am facing N
         When I follow the instructions "R8, R4, R4, R8" and stop at the first location I visit twice
         Then I should be at 4 blocks E and 0 blocks N
          And the distance should be 4

    Scenario: List all locations
        Given that I am at 0 blocks E and 0 blocks N
          And that I am facing N
         When I follow the instructions "R4" and stop at the first location I visit twice
         Then I should have visited the locations:
            | East | North |
            | 0    | 0     |
            | 1    | 0     |
            | 2    | 0     |
            | 3    | 0     |
            | 4    | 0     |
 