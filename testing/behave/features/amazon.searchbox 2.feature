Feature: Searchbox correctly searches for items

Scenario Outline: Verify product category contains a specific brand name
  Given we have a browser looking at "https://www.amazon.com"
  When we search using "field-keywords" for "<product>"
  Then we get a "<brand>" message

  Examples: Appliances
    | product  | brand            |
    | blender  | Hamilton Beach   |
    | vacuum   | Dyson            |
    | vacuum   | Hoover           |

  Examples: Clothes
    | product   | brand  |
    | tee shirt | Hanes  |
