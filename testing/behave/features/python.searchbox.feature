Feature: Searchbox correctly searches for items

Scenario: Display a no result message when there are no results
  Given we have a browser looking at "http://www.python.org"
   And  the browser title contains "Python"
  When  we search for "lksjf;lsjhu3r"
  Then  we get a "No results" message

Scenario: Display a no result message when there are no results
  Given we have a browser looking at "http://www.python.org"
   And  the browser title contains "Python"
  When  we search for "lksjf;lsjhu3r"
  Then  we get a "No results" message

Scenario: Display a no result message when there are no results
  Given we have a browser looking at "http://www.python.org"
   And  the browser title contains "Python"
  When  we search for "x$12asdfg345"
  Then  we get a "No results" message

Scenario: Display a no result message when there are no results
  Given we have a browser looking at "http://www.python.org"
  When  we search for "slkdjflskdjflsd"
  Then  we get a "No results" message

Scenario: Don't display no result message when there are results
  Given we have a browser looking at "http://www.python.org"
  When  we search for "pycon"
  Then  we don't get a "No results" message
