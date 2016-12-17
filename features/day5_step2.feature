Feature: Find password for the second security door

    Background: At a door with id abc
        Given a second door with door id "abc"
          And that a hash must start with five zeroes
          And I want the position and char from the 6th and 7th positions with a password length of eight
          And I want a eight-character password
          And I use MD5 as the hash function

    Scenario: Finding a character in the password for the second door
        Given that the current hash index is 3231929
         When I hash door id and the index
         Then I should get the password character 5
          And the password position should be 1 
    
    @slow
    Scenario: Find a full password for the second door
         When I find the password for the door
         Then the password should be 05ace8e3

    Scenario: Ignore invalid positions
        Given that the current hash index is 5017308
         When I hash door id and the index
         Then I should ignore the password character, because it is an invalid position
    
    Scenario: Ignore filled character positions
        Given a position in the password has been filled
         When I try to fill the same position
         Then I should keep the existing password character
     
     