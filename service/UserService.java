package service;

import dao.UserDAO;

public class UserService {

    UserDAO dao = new UserDAO();

    public boolean login(String username, String password) {

        return dao.validateUser(username, password);
    }

}