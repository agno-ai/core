'use strict';

module.exports = function(sequelize, DataTypes) {
  const Account = sequelize.define('Account', {
    account_id:DataTypes.INTEGER,
    account_name: DataTypes.STRING,
    username: DataTypes.STRING,
    password_hash: DataTypes.STRING,
    mirror_id: DataTypes.STRING
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
