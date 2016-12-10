Feature: Mark impossible triangles

    Scenario: Impossible triangle
     Given a triangle with sides 5 10 25
      When I test if it is possible
      Then I should find that it is impossible

    Scenario: Permuting side lengths
     Given a triangle with sides 5 10 25
      When I change the order of the sides
      Then I all possibilities should all be impossible or all be possible
    
    Scenario: Counting possible triangles
     Given the triangle input
        """
        4   21  894
        2  628  436
        10 10   10
        5  10   25         
        """
      When I count the number of possible triangles
      Then I should get 1 possible triangles
     
     
     
 