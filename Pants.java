public class Pants extends ClothingItem {
    private String fit;
    private double discount;

    public Pants(String brand, double price, String fit, int stock) {
        super(brand, price, stock);
        this.fit = fit;
        this.discount = 0;
    }

    @Override
    public String toString() {
        return "Pants [Brand=" + getBrand() + ", Price=" + getPrice() + ", Fit=" + fit + ", Stock=" + getStock() + "]";
    }

    public void applyDiscount(double percentage) {
        if (percentage > 0 && percentage <= 100) {
            discount = percentage;
        } else {
            throw new IllegalArgumentException("Discount percentage must be between 0 and 100.");
        }
    }

    @Override
    public double getDiscountedPrice() {
        return getPrice() * (1 - discount / 100);
    }
}
