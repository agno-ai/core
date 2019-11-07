const { attributes } = require('structure');

const User = attributes({
  EntryNo: {
    type: Number
  },
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
    type: String
  }
})(class User {

});

module.exports = User;
