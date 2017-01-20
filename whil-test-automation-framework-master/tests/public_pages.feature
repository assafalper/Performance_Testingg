Feature: Public pages load tests

  Scenario Outline: Pages load
    When Opening the public <page>
    Then Make sure logo is present

    Examples:
    |page             |
    |individuals.html |
    |index.html       |
    |schools.html     |
    |terms.html       |
    |privacy.html     |
    |about.html       |
    |" "              |

  Scenario Outline: Users can click Sign In from public pages
    When Opening the public <page>
    Then User clicks Sign In

    Examples:
    |page             |
    |individuals.html |
    |index.html       |
    |schools.html     |
    |terms.html       |
    |privacy.html     |
    |about.html       |
