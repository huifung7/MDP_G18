/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author FUNG
 */
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.util.*;

public class MDP_PC {

    /**
     * @param args the command line arguments
     */
    public static final InetSocketAddress RPI_ADDR = new InetSocketAddress("192.168.18.21", 5143);
    public static byte[] in_buffer, out_buffer;
    public static DatagramSocket clientSocket;
    private static InetSocketAddress targetAddr;

    public static void main(String[] args) throws SocketException, IOException {
        // TODO code application logic here
        System.out.println("MDP PC Start...");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter: ...\t");
        String inputStr;
        int choice;
        buildSocket();

        //call the send method..
        while (true) {
            //Run at start up..
            System.out.println("Run at Start up...");
            send("Starting... WiFi");
            System.out.println("send(1) or receive(0): ");
            choice = sc.nextInt();
            if (choice > 0) {
                System.out.println("Say Something: ");
                inputStr = sc.next();
                send(inputStr);
            } else {
                System.out.println(receive());
            }
            //send ("sent from pc\n");
        }

    }

    public static void buildSocket() throws SocketException {
        clientSocket = new DatagramSocket();
        targetAddr = RPI_ADDR;
        in_buffer = new byte[1024];
        out_buffer = new byte[1024];
    }

    protected static void send(String sendStr) throws SocketException, IOException {
        out_buffer = sendStr.getBytes();
        //Constructs a DatagramPacket for send packets of length length, 
        //specifying an offset into the buffer.

        DatagramPacket dgpkt = new DatagramPacket(out_buffer, out_buffer.length, targetAddr);
        clientSocket.send(dgpkt);
    }

    protected static String receive() throws IOException {
        DatagramPacket dgpkt = new DatagramPacket(in_buffer, in_buffer.length);
        String rnStr = "";
        clientSocket.receive(dgpkt);
        if (rnStr.isEmpty()) {
            rnStr = new String(dgpkt.getData(), dgpkt.getOffset(), dgpkt.getLength());
            return rnStr;
        } else {
            return null;
        }
    }

}
