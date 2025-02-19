"""This module contains core variables for the exercise."""

CHALLANGE_URL = "https://pathfinder.automationanywhere.com/challenges/AutomationAnywhereLabs-Login.html?_gl=1*1hchg56*_gcl_au*ODc5NjQ2NDEwLjE3Mzk4NDg1MDI.*_ga*MTc3NzI0MTUwMi4xNzM5ODQ4NTAz*_ga_DG1BTLENXK*MTczOTg0ODUwMi4xLjAuMTczOTg0ODUwNS41Ny4wLjE0NjE5MTYwMDg."

CREDENTIALS = {
	'BASIC_LOGIN' : {
		'EMAIL' : 'user@automationanywhere.com',
		'PASSWORD' : 'Automation123'
	}
}

XPATHS = {
	'LANDING_PAGE' : {
		'ACCEPT_COOKIES' : '//*[contains(text(), "Aceitar cookies")]',
		'COMMUNITY_LOGIN' : '//*[@aria-label="Community login"]'
	},
	'COMMUNITY_LOGIN' : {
		'EMAIL' : '//*[@placeholder="*Email"]',
		'SUBMIT_EMAIL' : '//*[@placeholder="*Email"]/../../following-sibling::div[1]',
		'PASSWORD' : '//input[@placeholder="Password"]',
		'SUBMIT_FORM' : '//*[contains(text(), "Log in")]'
	},
	'EXERCISES' : {
		'BASIC_LOGIN' : {
			'LOGIN' : '//*[@id="inputEmail"]',
			'PASSWORD' : '//*[@id="inputPassword"]',
			'SIGN_IN' : '//*[contains(text(), "Sign in")]'
		}
	}
}