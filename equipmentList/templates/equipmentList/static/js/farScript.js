'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const farSNLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const farEqLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const farBULabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")
const farCurLabel =document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(4) > th > label")
const farBLLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(5) > th > label")

farEqLabel.textContent= 'Equipment' 
farBULabel.textContent= 'BU'
farCurLabel.textContent= 'Location' 
farBLLabel .textContent= 'BL'
farSNLabel.textContent= 'Serial Number:'

