require('dotenv').load();

const fs = require('fs');
const path = require('path');

const ENV = process.env.NODE_ENV || 'development';

const envConfig = require(path.join(__dirname, 'environments', ENV));
console.log(envConfig);
const dbConfig = loadDbConfig();

const config = Object.assign({
  [ENV]: true,
  env: ENV,
  db: dbConfig
}, envConfig);
console.log(config);

module.exports = config;

function loadDbConfig() {
  if(fs.existsSync(path.join(__dirname, './database.js'))) {
    return require('./database')[ENV];
  }
}
