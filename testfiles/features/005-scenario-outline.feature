Feature: Addition
    This will the test our new
    tool to add numbers

    Scenario: Test
        Given I have the number 1
        When I add this to 10
        Then I see the sum 11

    Scenario Outline: Some Additions
        Given I have the numbers <number1> and <number2>
        When I sum these numbers
        Then I see the sum <result>

    Examples:
        | number1 | number2 | result |
        | 1       | 1       | 2      |
        | 2       | 3       | 5      |
        | 2       | 3       | 6      |
        | 7       | 1       | 8      |

    Scenario: Test
        Given I have the number 2
        When I add this to 10
        Then I see the sum 12
