const SequelizeAccountMapper = {
  toEntity({ dataValues }) {
    const {
      account_id,
      account_name,
      username,
      password_hash,
      mirror_id
    } = dataValues;

    return {
      account_id,
      account_name,
      username,
      password_hash,
      mirror_id
    };
  },

  toDatabase(survivor) {
    const {
      account_id,
      account_name,
      username,
      password_hash,
      mirror_id
    } = survivor;

    return {
      account_id,
      account_name,
      username,
      password_hash,
      mirror_id
    };
  }
};

module.exports = SequelizeAccountMapper;
