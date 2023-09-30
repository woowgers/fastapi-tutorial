import axios from "axios";

const state = {
  users: null,
  user: null,
  me: null,
};

const getters = {
  isAuthenticated: (state) => !!state.me,
  stateUser: (state) => state.user,
  stateUsers: (state) => state.users,
  stateMe: (state) => state.me,
};

const actions = {
  async register({ dispatch }, form) {
    await axios.post("register", form);
    let UserForm = new FormData();
    UserForm.append("username", form.username);
    UserForm.append("password", form.password);
    await dispatch("logIn", UserForm);
  },
  async logIn({ dispatch }, user) {
    await axios.post("login", user);
    await dispatch("viewMe");
  },
  async viewMe({ commit }) {
    let { data } = await axios.get(`users/me`);
    await commit("setMe", data);
  },
  async viewUsers({ commit }) {
    let { data } = await axios.get(`users`);
    await commit("setUsers", data);
  },
  async viewFriends({ commit }) {
    let user = await axios.get(`users/me`);
    let { data } = await axios.get(`users/${user.data.id}/friends`);
    await commit("setUsers", data);
  },
  async viewUser({ commit }, id) {
    let { data } = await axios.get(`users/${id}`);
    await commit("setUser", data);
  },
  async addFriend(_, me_id, id) {
    let Form = new FormData();
    Form.append("user_id", id);
    await axios.post(`users/${me_id}/make_friend`, Form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`users/${id}`);
  },
  async logOut({ commit }) {
    commit("logout");
  },
};

const mutations = {
  setMe(state, me) {
    state.me = me;
  },
  setUser(state, user) {
    state.user = user;
  },
  setUsers(state, users) {
    state.users = users;
  },
  logout(state) {
    state.me = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
