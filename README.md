# Step-up Probability in FFBE

Expected values and probability calculations per lap of step-up banners in Final Fantasy Brave Exvius (FFBE)

* The very narrow focus of this project is odds on step-up summon banners where the only results we care about are on and off banner Rainbows (5* bases).
    * All calculations are in full laps of the step-up banner, where 1 lap = completing a set of steps on the banner
    * Calculations are also lapis-centric, meaning any extra goodies received from steps are ignored (e.g. 10%/30% tickets, UoC for limited units)

### Running Tests

* Tests are currently included [as part of application code](https://docs.pytest.org/en/latest/goodpractices.html#tests-as-part-of-application-code)
    * To run tests on project, first install package with pip (`pip install -e .`) then use: `pytest --pyargs pstepup`