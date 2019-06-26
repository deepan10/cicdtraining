*** Settings ***
Documentation    Suite description

Library  library/CalcLib.py

*** Test Cases ***
Test Add
    [Tags]    add
    perform expr  add    1    1
    check result  2.0
    reset result

Test Sub
    [Tags]    sub
    perform expr  sub    1    1
    check result  0.0
    reset result

Test Sub with Negative
    [Tags]    sub
    perform expr  sub    1    2
    check result  -1.0
    reset result

Test Mul
    [Tags]    mul
    perform expr  mul    1    1
    check result  1.0
    reset result

Test Div
    [Tags]    div
    perform expr  div    1    1
    check result  1.0
    reset result

Test Div by Zero
    [Tags]    div
    ${result}=    Run Keyword And Expect Error  *  perform expr  div    1    0
    Log    ${result}
