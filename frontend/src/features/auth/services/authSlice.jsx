import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
  name: "auth",
  initialState: {
    token: null,
    user: null,
  },
  reducers: {
    setLogin: (state, action) => {
      state.token = action.payload;
      state.user = action.payload;
    },
    setLogout: (state) => {
      state.token = null;
      state.user = null;
    },
    setCompanies: (state, action) => {
      if (state.user) {
        state.user.companies = action.payload.companies;
      } else {
        console.error("user companies non-existent");
      }
    },
  },
});

export const { setLogin, setLogout, setCompanies } = authSlice.actions;
export default authSlice.reducer;
