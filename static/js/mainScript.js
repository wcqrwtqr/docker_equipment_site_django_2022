'use strict';

//**********************************************************************************
//*******************Below code to change the filter labels ************************
//**********************************************************************************

const mainLabel = document.querySelector("#collapseMe > div > div > form > table > tbody > tr:nth-child(1) > th > label")
const mainCostLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(2) > th > label")
const mainDescLabel = document.querySelector("body > div > div > div > div > form > table > tbody > tr:nth-child(3) > th > label")

mainLabel.textContent= 'Maintenance Type'
mainCostLabel.textContent= 'Cost'
mainDescLabel.textContent= 'Description'
