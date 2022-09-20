'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const equipSNLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const equipBULabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")
const equipBLLabel =document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(4) > th > label")
const equipDesLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")

equipDesLabel.textContent= 'Description'
equipBULabel.textContent= 'BU'
equipBLLabel .textContent= 'BL'
equipSNLabel.textContent= 'Serial Number:'
