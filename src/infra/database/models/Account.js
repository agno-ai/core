'use strict';

module.exports = function(sequelize, DataTypes) {
  const Account = sequelize.define('Account', {
    account_name: DataTypes.STRING
  }, {
    classMethods: {
      associate() {
        // associations can be defined here
      }
    }
  });

  return Account;
};
