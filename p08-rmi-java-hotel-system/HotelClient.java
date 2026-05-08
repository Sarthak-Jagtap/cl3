import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {

    public static void main(String[] args) {
        try {
            HotelServiceInterface service =
                    (HotelServiceInterface) Naming.lookup("rmi://localhost/HotelService");

            Scanner sc = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Exit");

                int choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {

                    case 1:
                        System.out.print("Enter name: ");
                        String name = sc.nextLine();

                        System.out.print("Enter room number: ");
                        int room = sc.nextInt();

                        boolean booked = service.bookRoom(name, room);
                        System.out.println(booked ? "Booked Successfully" : "Booking Failed");
                        break;

                    case 2:
                        System.out.print("Enter name: ");
                        String cname = sc.nextLine();

                        boolean cancelled = service.cancelBooking(cname);
                        System.out.println(cancelled ? "Cancelled Successfully" : "Cancel Failed");
                        break;

                    case 3:
                        System.exit(0);

                    default:
                        System.out.println("Invalid choice");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
