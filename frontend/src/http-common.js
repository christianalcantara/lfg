import axios from 'axios';

const baseURL = process.env.BASE_URL || 'http://localhost:8000';
export default axios.create({
  baseURL: `${baseURL}/api`,
  headers: {
    'Content-type': 'application/json',
  },
});
