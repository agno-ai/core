'use strict';

const dataFaker = require('src/infra/support/dataFaker');

module.exports = {
  up: function (queryInterface) {
    const testUsers = [];

    for(let i = 0; i < 20; i++) {
      testUsers.push({
        face_id: dataFaker.name(),
        createdAt: new Date(),
        updatedAt: new Date()
      });
    }

    return queryInterface.bulkInsert('Users', testUsers, {});
  },

  down: function (queryInterface) {
    return queryInterface.bulkDelete('Users', null, {});
  }
};
