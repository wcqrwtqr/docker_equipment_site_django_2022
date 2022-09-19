'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const empIDLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const empNameLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const empBLLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")

empIDLabel.textContent= 'ID' 
empNameLabel.textContent= 'Name'
empBLLabel.textContent= 'BL' 

