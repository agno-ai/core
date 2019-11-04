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

    return new User({ account_id, face_id, emotion, timestamp, image });
  },

  toDatabase(survivor) {
    const { face_id } = survivor;

    return { face_id };
  }
};

module.exports = SequelizeUserMapper;
