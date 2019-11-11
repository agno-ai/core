const UserSerializer = {
  serialize({ face_id, account_id }) {
    return {
      face_id,
      account_id
    };
  }
};

module.exports = UserSerializer;
