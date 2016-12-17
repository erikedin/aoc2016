Feature: Find password for security door

    Background: At a door with id abc
        Given a door with door id "abc"
          And that a hash must start with five zeroes
          And I want to find the 6th character in the hash
          And I want a eight-character password
          And I use MD5 as the hash function

    Scenario: Starting with index 0
        Then the current index should be 0

    Scenario: Finding a character in the password
        Given that the current hash index is 3231929
         When I hash door id and the index
         Then I should get the password character 1
    
    @slow
    Scenario: The first index
        Given that the current hash index is 0
         When I want to find the next valid index
         Then the current index should be 3231929

    @slow
    Scenario: The second index
        Given that the current hash index is 3231930
         When I want to find the next valid index
         Then the current index should be 5017308     

    @slow
    Scenario: Find a full password
         When I find the password for the door
         Then the password should be 18f47a30