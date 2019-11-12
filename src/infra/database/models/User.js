'use strict';

module.exports = function(sequelize, DataTypes) {
<<<<<<< HEAD
  const User = sequelize.define('user', {
    face_id: DataTypes.STRING
=======
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
>>>>>>> 3afb2ba0ba104886e5fa0f48d903d6a176401dbf
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
