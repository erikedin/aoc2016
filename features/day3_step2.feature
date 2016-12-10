Feature: Possible triangles by column

    Scenario: Triangles by column
     Given the column triangle input
        """
        10  5 30 
        10 10 31
        10 25 32
        """     
      When I count the number of possible triangles
      Then I should get 2 possible triangles