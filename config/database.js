module.exports = {
  development: {
    username: 'root',
    password: 'pw4agnodb',
    database: 'agno',
    host: '127.0.0.1',
    //dialect: 'postgres'
  },
  production: {
    username: process.env.RDS_USERNAME,
    password: process.env.RDS_PASSWORD,
    database: process.env.RDS_DB_NAME,
    host: process.env.RDS_HOSTNAME,
    port: process.env.RDS_PORT,
    dialect: 'mysql',
    ssl: 'Amazon RDS',
    dialectOptions: {
      ssl: 'Amazon RDS'
    }
  }
};
