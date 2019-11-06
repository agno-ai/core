const { ModelsLoader } = require('src/infra/sequelize');
const Sequelize = require('sequelize');
const { db: config } = require('config');

let sequelize;
if(config) {
  if(config.ssl) {
    sequelize = new Sequelize(config.database, config.username, config.password, {
      host: 'agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
      port: 3306,
      logging: console.log,
      maxConcurrentQueries: 100,
      dialect: 'mysql',
      dialectOptions: {
        ssl:'Amazon RDS'
      },
      pool: { maxConnections: 5, maxIdleTime: 30},
      language: 'en'
    })
  } else {
    sequelize = new Sequelize(config);
  }
  console.log(sequelize);
  module.exports = ModelsLoader.load({
    sequelize,
    baseFolder: __dirname
  });
} else {
  /* eslint-disable no-console */
  console.error('Database configuration not found, disabling database.');
  /* eslint-enable no-console */
}

