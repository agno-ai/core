module.exports = {
  development: {
    username: 'root',
    password: 'pw4agnodb',
    database: 'agno',
    host: '127.0.0.1',
    //dialect: 'postgres'
  },
  production: process.env.DATABASE_URL
};
