package service;

import dao.StockDAO;

public class StockService {

    StockDAO dao = new StockDAO();

    public void stockIn(int productId, int quantity) {

        dao.stockIn(productId, quantity);
    }

    public void stockOut(int productId, int quantity) {

        dao.stockOut(productId, quantity);
    }

}