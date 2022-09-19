'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const jobClientLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const jobWellLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const jobBLLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")

jobClientLabel.textContent= 'Client' 
jobWellLabel.textContent= 'Well'
jobBLLabel.textContent= 'BL' 

