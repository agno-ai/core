const UserSerializer = {
  serialize({ EntryNo, face_id, account_id, timestamp, emotion, image  }) {
    return {
      EntryNo,
      face_id,
      account_id,
      timestamp,
      emotion,
      image
    };
  }
};

module.exports = UserSerializer;
