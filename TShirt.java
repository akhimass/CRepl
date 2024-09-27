public class TShirt extends ClothingItem {
    private String size;
    private double discount;

    public TShirt(String brand, double price, String size, int stock) {
        super(brand, price, stock);
        this.size = size;
        this.discount = 0;
    }

    @Override
    public String toString() {
        return "TShirt [Brand=" + getBrand() + ", Price=" + getPrice() + ", Size=" + size + ", Stock=" + getStock() + "]";
    }

    @Override
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
