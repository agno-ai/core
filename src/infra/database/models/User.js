'use strict';

module.exports = function(sequelize, DataTypes) {
  const User = sequelize.define('User', {
    EntryNo: DataTypes.INTEGER,
    account_id: DataTypes.INTEGER,
    face_id: DataTypes.STRING,
    timestamp: DataTypes.DATE,
    emotion: DataTypes.STRING,
    image: DataTypes.BLOB
  }, {
    classMethods: {
      associate() {
        // associations can be defined here
      }
    }
  });

  return User;
};
