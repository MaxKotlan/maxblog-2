Feature: Searchbox correctly searches for items

Scenario: Verify Hamilton Beach is a blender on sale
  Given we have a browser looking at "https://www.amazon.com"
  When  we search using "field-keywords" for "blender"
  Then  we get a "Hamilton Beach" message

Scenario: Verify Hanes is a tee shirt on sale
  Given we have a browser looking at "https://www.amazon.com"
  When  we search using "field-keywords" for "tee shirt"
  Then  we get a "Hanes" message

Scenario: Verify Dyson is a vacuum on sale
  Given we have a browser looking at "https://www.amazon.com"
  When  we search using "field-keywords" for "vacuum"
  Then  we get a "Dyson" message
   And  we get a "Hoover" message
