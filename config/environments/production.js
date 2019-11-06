module.exports = {
  web: {
    port: process.env.RDS_PORT
  },
  logging: {
    appenders: [
      { type: 'console', layout: { type: 'basic' } }
    ]
  }
};
