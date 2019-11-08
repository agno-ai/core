# core

**Quick start**

1. Setup the database on config/database.js (use example)

2. Install the dependencies with yarn (get it here https://yarnpkg.com/lang/en/docs/install/ if you don't have yarn installed)
3. Create the development and test databases you have setup on config/database.js
4. Run the database migrations with *yarn sequelize db:migrate*
5. Add some seed data to the development database with *yarn sequelize db:seed:all*
6. Run the application in development mode with *yarn dev*
Access http://localhost:3000/api/users for sample users data
7. In production, use http://agno-dev.eu-central-1.elasticbeanstalk.com/api/users for users api endpoint
