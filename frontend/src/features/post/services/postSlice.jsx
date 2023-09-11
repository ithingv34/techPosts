import { createSlice } from "@reduxjs/toolkit";

const postSlice = createSlice({
  name: "post",
  initialState: {
    posts: [],
  },
  reducers: {
    setPosts: (state, action) => {
      state.posts = action.payload.posts;
    },
    setPost: (state, action) => {
      const { post_id, post } = action.payload;
      const updatedPosts = state.posts.map((existingPost) =>
        existingPost._id === post_id ? post : existingPost
      );
      state.posts = updatedPosts;
    },
  },
});

export const { setPosts, setPost } = postSlice.actions;
export default postSlice.reducer;
