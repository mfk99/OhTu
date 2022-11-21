*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  testi  test1salasana
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  testi  test1salasana
    Input New Command And Create User  testi  test1salasana
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  te  test1salasana
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command And Create User  testi  lyhyt
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  testi  testisalasana
    Output Should Contain  Password can't be only characters