'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const jobClientLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const jobWellLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const jobBULabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")
const jobBLLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(4) > th > label")
const jobIDLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(5) > th > label")
jobClientLabel.textContent= 'Client'
jobWellLabel.textContent= 'Well'
jobBULabel.textContent= 'BU'
jobBLLabel.textContent= 'BL'
jobIDLabel.textContent= 'JobID'
