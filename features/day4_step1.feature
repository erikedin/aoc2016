Feature: Finding real rooms

    Scenario Outline: Room properties
     Given a room <Room>
      Then the sector id is <Sector id>
       And the checksum is <Checksum>
     
     Examples:
       | Room                | Sector id | Checksum |
       | aaaaa-bbb-z-y-x-123 | 123       | abxyz    | 
       | a-b-c-d-e-f-g-h-987 | 987       | abcde    | 
       | not-a-real-room-404 | 404       | oarel    |
     
     
    Scenario: Sum sector ids
     Given the rooms
        | Room                |
        | aaaaa-bbb-z-y-x-123 | 
        | a-b-c-d-e-f-g-h-987 |  
        | not-a-real-room-404 | 
      When I sum the sector ids
      Then I should get the sector id sum 1514
     
    Scenario: Calculating common letters
     Given a room aaaaa-bbb-z-y-x-123
      When I calculate the letter frequencies
      Then I should get the frequencies
        """
        {"a": 5, "b": 3, "x": 1, "y": 1, "z": 1}
        """
    
    Scenario Outline: Defining a complete ordering
      Given letters <L1> and <L2>, with respective frequencies <F1> and <F2>
       When I order them by frequency first and lexical order second
       Then the first in order should be <First>

      Examples:
      | L1 | F1 | L2 | F2 | First |
      | a  | 1  | b  | 2  | b     |
      | a  | 2  | b  | 2  | a     |
     
    Scenario Outline: Room with expected checksum
     Given a checksum and room <Room> and <Checksum> 
      When I check if it is a real room
      Then I find that it is <Real or decoy>

     Examples:
        | Room                  | Checksum | Real or decoy |
        | aaaaa-bbb-z-y-x-123   | abxyz    | real          | 
        | a-b-c-d-e-f-g-h-987   | abcde    | real          |
        | not-a-real-room-404   | oarel    | real          |
        | totally-real-room-200 | decoy    | decoy         |
     
    Scenario: Sector id of real rooms
     Given the rooms and checksums
        """
        aaaaa-bbb-z-y-x-123[abxyz]
        a-b-c-d-e-f-g-h-987[abcde]
        not-a-real-room-404[oarel]
        totally-real-room-200[decoy]
        """
      When I calculate the sum of sector ids of the real rooms
      Then I should get the sector id sum 1514