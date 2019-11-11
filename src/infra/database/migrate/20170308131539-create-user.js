'use strict';
module.exports = {
  up: function(queryInterface, Sequelize) {
    return queryInterface.createTable('Users', {
      EntryNo: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      account_id: {
        type: Sequelize.INTEGER
      },
      face_id: {
        type: Sequelize.STRING
      },
      timestamp: {
        type: Sequelize.DATETIME
      },
      emotion: {
        type: Sequelize.STRING
      },
      image: {
        type: Sequelize.BLOB
      }
    });
  },
  down: function(queryInterface) {
    return queryInterface.dropTable('Users');
  }
};
