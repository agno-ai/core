'use strict';

module.exports = function(sequelize, DataTypes) {
  const Account = sequelize.define('account', {
    account_name: DataTypes.STRING
  }, {
    timestamps: false,
    classMethods: {
      associate() {
        // associations can be defined here
      }
    }
  });

  return Account;
};
