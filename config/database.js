module.exports = {
  development: {
    username: 'root',
    password: '.....',
    database: 'mysql',
    host: '127.0.0.1',
    dialect: 'mysql'
  },
  test: {
    username: 'root',
    password: '.....',
    database: 'test',
    host: '127.0.0.1',
    dialect: 'mysql'
  },
  production: {
    username: process.env.RDS_USERNAME,
    password: process.env.RDS_PASSWORD,
    database: process.env.RDS_DB,
    host: process.env.RDS_HOSTNAME,
    port: process.env.RDS_PORT,
    dialect: 'mysql',
    ssl: 'Amazon RDS',
    dialectOptions: {
      ssl: 'Amazon RDS'
    }
  }
};
