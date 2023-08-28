import axios from "axios";

const state = {
  users: null,
  user: null,
};

const getters = {
  isAuthenticated: (state) => !!state.user,
  stateUser: (state) => state.user,
  stateUsers: (state) => state.users,
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
    await commit("setUser", data);
  },
  async viewUsers({ commit }) {
    let { data } = await axios.get(`users`);
    await commit("setUsers", data);
  },
  async viewUser({ commit }, id) {
    let { data } = await axios.get(`users/${id}`);
    await commit("setUser", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`users/${id}`);
  },
  async logOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setUsers(state, users) {
    state.users = users;
  },
  logout(state, user) {
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
