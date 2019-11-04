const { attributes } = require('structure');

const Account = attributes({
  account_name: {
    type: String
  },
  username: {
    type: String
  },
  password_hash: {
    type: String
  },
})(class Account {

});


module.exports = Account;
