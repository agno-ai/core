const { ModelsLoader } = require('src/infra/sequelize');
const Sequelize = require('sequelize');
const { db: config } = require('config');

if(config) {
  const sequelize = new Sequelize(config);
<<<<<<< HEAD

=======
>>>>>>> 3afb2ba0ba104886e5fa0f48d903d6a176401dbf
  module.exports = ModelsLoader.load({
    sequelize,
    baseFolder: __dirname
  });
} else {
  /* eslint-disable no-console */
  console.error('Database configuration not found, disabling database.');
  /* eslint-enable no-console */
}

