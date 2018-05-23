# Voting Application on HyperLedger Fabric Using Python 

This is a simple voting application on hyperledger Fabric using python. The purpose is to create the contesting candidates and the participants (Voters) to participate in the election. Candidate acquiring highest number of the votes will be declared as the winner.

## Professional Pre-Requisite

Knowledge in Hyperledger Fabric 
Python coding

## Technical Pre-Requisite

Visual Studio or Any editor
Node.js

## Developer Machine Setup for Hyperledger

Node version 8 (node version 9 does not work)
https://nodejs.org/en/download/ 
Check using node –v

Git client version 2.9 or higher 
https://www.atlassian.com/git/tutorials/install-git 
Check using git -v

Python 2.7. 
https://www.python.org/downloads/ 
Check using pyhon –v

Yeoman is an npm package for node
npm install –g yo

Composer command line interface
npm install –g composer-cli 
Check using composer –v

Composer REST Server
npm install –g composer-rest-server 
Check using composer-rest-server –v

Yeoman Generator for Network App
npm install –g generator-hyperledger-composer 
Check using yo --generators

## Creating a hyperLedger Network

Once the installation is done . Open  powershell and run the following command
Yo hyperledger-composer
Select the required network model/business network from the list and fill the question regarding the network.
The network is created .

## Developing the Network

Open the created network ,in this case it is Voting-application in the visual studio editor or any other editor of choice.
Under the model folder there are two .cto files  candidates.cto  and participants.cto.. In lib folder logic.py file  which contains the logic for the election procedure the code Is available in the repository.

## Testing 

In https://composer-playground.mybluemix.net/
Create a new network on composer playground and deploy it for testing.

## Contributors

Azharuddin

 ## Copyright © Azharuddin – dis.azhar@gmail.com 


