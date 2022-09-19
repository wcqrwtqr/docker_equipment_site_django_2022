'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const farEqLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const farSNLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const farBULabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")
const farBLLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(4) > th > label")

farEqLabel.textContent= 'Serial Number'
farBULabel.textContent= 'BU'
farBLLabel .textContent= 'BL'
farSNLabel.textContent= 'Desc'
