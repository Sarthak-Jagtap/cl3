import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {

    private Map<Integer, String> bookings;

    protected HotelServer() throws RemoteException {
        bookings = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {

        if (!bookings.containsKey(roomNumber)) {
            bookings.put(roomNumber, guestName);
            System.out.println("Room " + roomNumber + " booked for " + guestName);
            return true;
        } else {
            System.out.println("Room already booked!");
            return false;
        }
    }

    @Override
    public synchronized boolean cancelBooking(String guestName) throws RemoteException {

        for (Map.Entry<Integer, String> entry : bookings.entrySet()) {
            if (entry.getValue().equals(guestName)) {
                bookings.remove(entry.getKey());
                System.out.println("Booking cancelled for " + guestName);
                return true;
            }
        }
        System.out.println("No booking found!");
        return false;
    }

    public static void main(String[] args) {
        try {
            HotelServer server = new HotelServer();

            java.rmi.registry.LocateRegistry.createRegistry(1099);

            Naming.rebind("HotelService", server);

            System.out.println("Hotel Server is running...");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
