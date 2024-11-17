*** Settings ***
Library  ../CounterLibrary.py

*** Keywords ***
Increase Counter Three Times
    Increase Counter
    Increase Counter
    Increase Counter

*** Test Cases ***
Increase Counter Once
    Counter Value Should Be  0
    Increase Counter
    Counter Value Should Be  1

Increase Counter Many Times
    Counter Value Should Be  0
    Increase Counter
    Increase Counter
    Increase Counter
    Counter Value Should Be  3

Increment Counter By Amount
    Counter Value Should Be  0
    Increment Counter By  5
    Counter Value Should Be  5
