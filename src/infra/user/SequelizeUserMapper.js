const User = require('src/domain/user/User');

const SequelizeUserMapper = {
  toEntity({ dataValues }) {
    const {
      account_id,
      face_id,
      emotion,
      timestamp,
      image
    } = dataValues;

    return { account_id, face_id, emotion, timestamp, image };
  },

  toDatabase(survivor) {
    const { account_id, face_id, emotion, timestamp, image } = survivor;

    return { account_id, face_id, emotion, timestamp, image };
  }
};

module.exports = SequelizeUserMapper;
