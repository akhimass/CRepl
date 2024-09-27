public abstract class ClothingItem implements Discountable{
    private String brand;
    private double price;
    private int stock;

    public ClothingItem(String brand, double price, int stock) {
        this.brand = brand;
        this.price = price;
        this.stock = stock;
    }

    public String getBrand() {
        return brand;
    }

    public double getPrice() {
        return price;
    }

    public int getStock() {
        return stock;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    @Override
    public abstract String toString();

    @Override
    public double getDiscountedPrice() {
        return price; // Default implementation returns the regular price
    }
}
