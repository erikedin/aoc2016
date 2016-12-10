Feature: Decrypt room names


    Scenario: Decrypting a room name
     Given a room qzmt-zixmtkozy-ivhz-343
      When I decrypt the name
      Then the name should be "very encrypted name"

    Scenario: Decrypting dashes
     Given a character - and a sector id 343
      When I decrypt the character
      Then I should get the decrypted character " "

    Scenario Outline: Decrypting characters
     Given a character <Character> and a sector id <Sector id>
      When I decrypt the character
      Then I should get the decrypted character "<Decrypted>"
     
     Examples:
        | Character | Sector id | Decrypted |
        | q         | 343       | v         |
        | z         | 343       | e         |
        | m         | 343       | r         |
        | t         | 343       | y         |