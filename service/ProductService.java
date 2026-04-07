package service;

import dao.ProductDAO;

public class ProductService {

    ProductDAO dao = new ProductDAO();

    public boolean addProduct(int id, String name, double price, int qty) {
        // Product class moved to model/, but to avoid package issues, create local
        // Note: Ideally, fix javac classpath, but for quick fix, implement directly
        return dao.addProduct(id, name, price, qty);
    }

    public void updateProduct(int id, String name, double price, int qty) {
        dao.updateProduct(id, name, price, qty);
    }

    public void deleteProduct(int id) {
        dao.deleteProduct(id);
    }
}
