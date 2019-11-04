const { attributes } = require('structure');

const User = attributes({
  account_id: {
    type: Number
  },
  face_id: {
    type: String
  },
  timestamp: {
    type: String
  },
  emotion: {
    type: String
  },
  image: {
    type: Number
  }
})(class User {

});

module.exports = User;
