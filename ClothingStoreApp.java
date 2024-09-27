import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ClothingStoreApp {
    private static List<ClothingItem> inventory = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Clothing Store Inventory Creation");
        boolean running = true;

        while (running) {
            System.out.println("1. Add Item");
            System.out.println("2. List Items");
            System.out.println("3. Apply Discount");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");

            int choice = getIntInput();
            scanner.nextLine(); // Consume the newline character
            switch (choice) {
                case 1:
                    addItem();
                    break;
                case 2:
                    listItems();
                    break;
                case 3:
                    applyDiscount();
                    break;
                case 4:
                    running = false;
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option. Please choose again.");
            }
        }

        scanner.close();
    }

    private static void addItem() {
        try {
            System.out.print("Enter clothing type (TShirt/Pants): ");
            String type = scanner.nextLine().trim();

            if (type.isEmpty()) {
                throw new IllegalArgumentException("Clothing type cannot be empty");
            }

            System.out.print("Enter brand: ");
            String brand = scanner.nextLine().trim();

            if (brand.isEmpty()) {
                throw new IllegalArgumentException("Brand cannot be empty");
            }

            System.out.print("Enter price: ");
            double price = getDoubleInput("Invalid number format for price");

            System.out.print("Enter stock quantity: ");
            int stock = getIntInput();

            ClothingItem item = null;

            if (type.equalsIgnoreCase("TShirt")) {
                System.out.print("Enter size: ");
                String size = scanner.nextLine().trim();

                if (size.isEmpty()) {
                    throw new IllegalArgumentException("Size cannot be empty");
                }

                item = new TShirt(brand, price, size, stock);
            } else if (type.equalsIgnoreCase("Pants")) {
                System.out.print("Enter fit (e.g., Slim, Regular): ");
                String fit = scanner.nextLine().trim();

                if (fit.isEmpty()) {
                    throw new IllegalArgumentException("Fit cannot be empty");
                }

                item = new Pants(brand, price, fit, stock);
            } else {
                throw new IllegalArgumentException("Invalid clothing type. Only TShirt and Pants are supported.");
            }

            inventory.add(item);
            System.out.println("Item added to inventory.");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    private static void listItems() {
        if (inventory.isEmpty()) {
            System.out.println("No items in inventory.");
        } else {
            for (ClothingItem item : inventory) {
                System.out.println(item);
            }
        }
    }

    private static void applyDiscount() {
        if (inventory.isEmpty()) {
            System.out.println("No items in inventory to apply a discount.");
            return;
        }

        System.out.print("Enter the index of the item to apply a discount (starting from 0): ");
        int index = getIntInput();
        scanner.nextLine(); // Consume newline character

        if (index < 0 || index >= inventory.size()) {
            System.out.println("Invalid index.");
            return;
        }

        ClothingItem item = inventory.get(index);

        System.out.print("Enter discount percentage: ");
        double percentage = getDoubleInput("Invalid number format for discount percentage");

        try {
            item.applyDiscount(percentage);
            System.out.println("Discount applied.");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    private static int getIntInput() {
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a number.");
            scanner.next(); // Clear the invalid input
        }
        int value = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        return value;
    }

    private static double getDoubleInput(String errorMessage) {
        while (!scanner.hasNextDouble()) {
            System.out.println(errorMessage);
            scanner.next(); // Clear the invalid input
        }
        double value = scanner.nextDouble();
        scanner.nextLine(); // Consume the newline character
        return value;
    }
}

