'use strict';

module.exports = function(sequelize, DataTypes) {
  const User = sequelize.define('User', {
    EntryNo: {
      type: DataTypes.INTEGER,
      primaryKey: true
    },
    account_id: DataTypes.INTEGER,
    face_id: DataTypes.STRING,
    timestamp: DataTypes.DATE,
    emotion: DataTypes.STRING,
    image: DataTypes.BLOB
  }, {
    timestamps: false,
    classMethods: {
      associate() {
        // associations can be defined here
      }
    }
  });

  return User;
};
