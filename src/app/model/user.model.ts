export interface User {
    id: number;
    username: string;
    email: string;
  }
  
  export interface UserCreate {
    username: string;
    email: string;
    password: string;
  }
  
  // src/app/models/token.model.ts
  export interface Token {
    access_token: string;
    token_type: string;
  }