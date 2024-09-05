export const LOGIN = "http://localhost:5000/login"
export const REGISTER = "http://localhost:5000/register"
export const SLIPS = "http://localhost:5000/slips"
export const USER = "http://localhost:5000/user"

export const mountTokenHeader = (accessToken) => {
    return { 'headers': { 'Authorization': `Bearer ${accessToken}` } };
}