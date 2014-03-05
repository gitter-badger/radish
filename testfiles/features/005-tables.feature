Feature: Support for tables
    In order to manage complex data, i want that
    radish supports tables.

    Scenario: Use a table as a single object where attributes are accessed by property names
        Given I have a address card
            | Name     | Hans            |
            | Lastname | Dampf           |
            | Street   | In allen Gassen |
            | ZIP      | 4242            |
            | City     | Buxdehude       |

        Given I have a address table
            | Name   | Lastname | Street          | ZIP  | City        |
            | Hans   | Dampf    | In allen Gassen | 4242 | Buxdehude   |
            | Donald | Duck     | I don't know    | 1234 | Entenhausen |

