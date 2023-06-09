*** Settings ***

Library   SeleniumLibrary
*** Variables ***


*** Test Cases ***

Test
    Open Browser    url=https://www.google.com/    browser=chrome    options=add_experimental_option("detach", True)