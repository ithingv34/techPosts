import { configureStore } from "@reduxjs/toolkit";
import storage from "redux-persist/lib/storage";
import authReducer from "@/features/auth/services/authSlice";
import darkModeReducer from "@/features/darkmode/services/darkModeSlice";
import postReducer from "@/features/post/services/postSlice";
import {
  persistReducer,
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from "redux-persist";

// Redux Persist 구성
const persistConfig = {
  key: "root", // 저장 키
  storage, // 사용할 스토리지 엔진 (로컬 스토리지),
  version: 1,
};

// Redux Persist 리듀서 생성
const persistedAuthReducer = persistReducer(persistConfig, authReducer);
const persistedDarkModeReducer = persistReducer(persistConfig, darkModeReducer);
const persistedPostReducer = persistReducer(persistConfig, postReducer);

const store = configureStore({
  reducer: {
    auth: persistedAuthReducer,
    darkMode: persistedDarkModeReducer,
    posts: persistedPostReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoreActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
});

export default store;
